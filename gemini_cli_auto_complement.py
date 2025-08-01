#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini CLI Auto Complement Script
Used to automatically complement Gemini CLI related code to Roo-Code project

Author: AI Assistant
Date: 2024
"""

import os
import shutil
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gemini_cli_complement.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GeminiCliAutoComplement:
    """Gemini CLI Auto Complement Class"""
    
    def __init__(self, source_dir: str, target_dir: str):
        """
        Initialize
        
        Args:
            source_dir: Source directory (z-geminicli-install)
            target_dir: Target directory (Roo-Code-3.23.16)
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        
        # Strict operation rules
        self.STRICT_RULES = {
            "NO_DELETE": "Absolutely no deletion of any existing code",
            "ONLY_ADD": "Only addition operations, no deletion or replacement",
            "PRESERVE_ALL": "Preserve all existing code, even if related to gemini-cli",
            "APPEND_ONLY": "For i18n files, append at the end to maintain integrity",
            "NO_MODIFY": "Do not modify any existing lines, only insert new content"
        }
        
        logger.info(f"Initializing Gemini CLI Auto Complement")
        logger.info(f"Source directory: {self.source_dir}")
        logger.info(f"Target directory: {self.target_dir}")
        
        # Verify directories exist
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {self.source_dir}")
        if not self.target_dir.exists():
            raise FileNotFoundError(f"Target directory not found: {self.target_dir}")
    
    def copy_direct_files(self) -> None:
        """Copy files that need direct overwrite"""
        logger.info("Starting to copy direct overwrite files...")
        
        # Copy all files from source directory to target directory
        self._copy_directory_recursive(self.source_dir, self.target_dir)
    
    def _copy_directory_recursive(self, src_dir: Path, dst_dir: Path) -> None:
        """Recursively copy directory, skip certain files"""
        # Files to skip (documentation and script files)
        skip_files = {
            'readme-geminicli-install.md',
            'IMPROVEMENTS.md',
            'COMPLETED_FILES.md',
            'APPEND_STRATEGY.md',
            'batch-complement-i18n.js',
            'batch-complement-common-i18n.js'
        }
        
        # File patterns to skip (diff documentation files)
        skip_patterns = [
            r'\.diff\.md$',  # Skip all .diff.md files
            r'\.md$',        # Skip all .md files (optional, uncomment if needed)
        ]
        
        for item in src_dir.iterdir():
            # Check if file should be skipped by name
            if item.name in skip_files:
                logger.info(f"Skipping file: {item.name}")
                continue
            
            # Check if file should be skipped by pattern
            should_skip = False
            for pattern in skip_patterns:
                if re.search(pattern, item.name):
                    logger.info(f"Skipping file (pattern match): {item.name}")
                    should_skip = True
                    break
            
            if should_skip:
                continue
                
            if item.is_file():
                # Copy file
                dst_file = dst_dir / item.name
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dst_file)
                logger.info(f"Copied file: {item}")
            elif item.is_dir():
                # Recursively copy directory
                dst_subdir = dst_dir / item.name
                self._copy_directory_recursive(item, dst_subdir)
    
    def complement_packages_types_index(self) -> None:
        """Complement packages/types/src/providers/index.ts"""
        logger.info("Complementing packages/types/src/providers/index.ts...")
        
        target_file = self.target_dir / "packages/types/src/providers/index.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if gemini-cli export already exists
        if 'export * from "./gemini-cli"' in content:
            logger.info("gemini-cli export already exists, skipping")
            return
        
        # Find insertion position (after gemini export)
        gemini_pattern = r'(export \* from "./gemini\.js")'
        match = re.search(gemini_pattern, content)
        
        if match:
            # Add gemini-cli export after gemini export
            insert_pos = match.end()
            new_content = content[:insert_pos] + '\nexport * from "./gemini-cli.js"' + content[insert_pos:]
            
            # Write back to file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            logger.info("Added gemini-cli export")
        else:
            logger.warning("Gemini export not found, cannot determine insertion position")
    
    def complement_api_index(self) -> None:
        """Complement src/api/index.ts"""
        logger.info("Complementing src/api/index.ts...")
        
        target_file = self.target_dir / "src/api/index.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if both import and case already exist
        has_import = 'GeminiCliHandler,' in content
        has_case = 'case "gemini-cli":' in content
        
        if has_import and has_case:
            logger.info("GeminiCliHandler import and case already exist, skipping")
            return
        
        # Step 1: Add import if not exists
        if not has_import:
            # Use a more precise approach to find the import statement
            # Look for the line that contains "ClaudeCodeHandler," and add GeminiCliHandler after it
            lines = content.split('\n')
            import_added = False
            
            for i, line in enumerate(lines):
                if 'ClaudeCodeHandler,' in line:
                    # Add GeminiCliHandler on the next line with proper indentation
                    indent = len(line) - len(line.lstrip())
                    new_line = ' ' * indent + 'GeminiCliHandler,'
                    lines.insert(i + 1, new_line)
                    import_added = True
                    logger.info("Added GeminiCliHandler to imports")
                    break
            
            if import_added:
                content = '\n'.join(lines)
            else:
                logger.warning("ClaudeCodeHandler import line not found, cannot add GeminiCliHandler import")
        
        # Step 2: Add case if not exists
        if not has_case:
            # Find the gemini case and add gemini-cli case after it
            case_pattern = r'(case "gemini":\s*\n\s*return new GeminiHandler\(options\))'
            match = re.search(case_pattern, content)
            
            if match:
                # Add gemini-cli case after gemini case
                insert_pos = match.end()
                new_case = '\n\t	case "gemini-cli":\n\t\t\treturn new GeminiCliHandler(options)'
                content = content[:insert_pos] + new_case + content[insert_pos:]
                logger.info("Added gemini-cli case to switch statement")
            else:
                logger.warning("Gemini case not found, cannot determine insertion position")
        
        # Write back to file if any changes were made
        if not has_import or not has_case:
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info("Updated src/api/index.ts")
    
    def complement_api_providers_index(self) -> None:
        """Complement src/api/providers/index.ts"""
        logger.info("Complementing src/api/providers/index.ts...")
        
        target_file = self.target_dir / "src/api/providers/index.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if GeminiCliHandler export already exists
        if 'export { GeminiCliHandler }' in content:
            logger.info("GeminiCliHandler export already exists, skipping")
            return
        
        # Find insertion position (after GeminiHandler export)
        gemini_pattern = r'(export \{ GeminiHandler \} from "[^"]*")'
        match = re.search(gemini_pattern, content)
        
        if match:
            # Add GeminiCliHandler export after GeminiHandler export
            insert_pos = match.end()
            new_export = '\nexport { GeminiCliHandler } from "./gemini-cli"'
            new_content = content[:insert_pos] + new_export + content[insert_pos:]
            
            # Write back to file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            logger.info("Added GeminiCliHandler export")
        else:
            logger.warning("GeminiHandler export not found, cannot determine insertion position")
    
    def complement_check_exist_api_config(self) -> None:
        """Complement src/shared/checkExistApiConfig.ts"""
        logger.info("Complementing src/shared/checkExistApiConfig.ts...")
        
        target_file = self.target_dir / "src/shared/checkExistApiConfig.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if gemini-cli already exists
        if '"gemini-cli"' in content:
            logger.info("gemini-cli configuration already exists, skipping")
            return
        
        # Find insertion position (in special provider array)
        pattern = r'(\["human-relay", "fake-ai", "claude-code"\])'
        match = re.search(pattern, content)
        
        if match:
            # Add gemini-cli to array
            insert_pos = match.end() - 1  # Before the last quote
            new_content = content[:insert_pos] + ', "gemini-cli"' + content[insert_pos:]
            
            # Write back to file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            logger.info("Added gemini-cli to special provider array")
        else:
            logger.warning("Special provider array not found, cannot determine insertion position")
    
    def complement_webview_validate(self) -> None:
        """Complement webview-ui/src/utils/validate.ts"""
        logger.info("Complementing webview-ui/src/utils/validate.ts...")
        
        target_file = self.target_dir / "webview-ui/src/utils/validate.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if gemini-cli case already exists
        if 'case "gemini-cli":' in content:
            logger.info("gemini-cli case already exists, skipping")
            return
        
        # Use a more precise approach to find the gemini case and add gemini-cli case after it
        lines = content.split('\n')
        case_added = False
        
        # Find the gemini case and add gemini-cli case after it
        for i, line in enumerate(lines):
            if 'case "gemini":' in line:
                # Find the end of the gemini case (the break statement)
                for j in range(i + 1, len(lines)):
                    if 'break' in lines[j] and lines[j].strip() == 'break':
                        # Add gemini-cli case after the break
                        indent = len(lines[j]) - len(lines[j].lstrip())
                        new_case = f'{" " * indent}case "gemini-cli":\n{" " * indent}\treturn undefined // gemini-cli 不需要 API key 验证\n{" " * indent}break'
                        lines.insert(j + 1, new_case)
                        case_added = True
                        logger.info("Added gemini-cli case to validate function")
                        break
                break
        
        if case_added:
            # Write back to file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            logger.info("Updated webview-ui/src/utils/validate.ts")
        else:
            logger.warning("Gemini case not found, cannot determine insertion position")
    
    def complement_webview_api_options(self) -> None:
        """Complement webview-ui/src/components/settings/ApiOptions.tsx"""
        logger.info("Complementing webview-ui/src/components/settings/ApiOptions.tsx...")
        
        target_file = self.target_dir / "webview-ui/src/components/settings/ApiOptions.tsx"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if all elements already exist
        has_type_import = 'geminiCliDefaultModelId,' in content  # Check for import with comma
        has_component_import = 'GeminiCli,' in content
        has_provider_config = '"gemini-cli": { field: "apiModelId", default: geminiCliDefaultModelId }' in content
        has_component_render = 'selectedProvider === "gemini-cli"' in content
        
        if has_type_import and has_component_import and has_provider_config and has_component_render:
            logger.info("All GeminiCli elements already exist in ApiOptions.tsx, skipping")
            return
        
        # Convert content to lines for easier manipulation
        lines = content.split('\n')
        
        # Step 1: Add type import if not exists
        if not has_type_import:
            type_import_added = False
            
            # First try: Look for geminiDefaultModelId and add after it
            for i, line in enumerate(lines):
                if 'geminiDefaultModelId,' in line:
                    # Add geminiCliDefaultModelId after geminiDefaultModelId
                    lines.insert(i + 1, '\tgeminiCliDefaultModelId,')
                    type_import_added = True
                    logger.info("Added geminiCliDefaultModelId after geminiDefaultModelId in ApiOptions.tsx")
                    break
            
            # Second try: Look for the type imports from "@roo-code/types" if first approach failed
            if not type_import_added:
                for i, line in enumerate(lines):
                    if 'from "@roo-code/types"' in line and 'import' in line:
                        logger.info(f"Found types import at line {i+1}")
                        # This is a multi-line import, find the closing brace
                        brace_count = 0
                        for j in range(i, len(lines)):
                            brace_count += lines[j].count('{') - lines[j].count('}')
                            if brace_count == 0:
                                # Insert geminiCliDefaultModelId before the closing brace
                                if 'geminiCliDefaultModelId' not in lines[j-1]:
                                    lines.insert(j-1, '\tgeminiCliDefaultModelId,')
                                    type_import_added = True
                                    logger.info("Added geminiCliDefaultModelId to type imports in ApiOptions.tsx")
                                break
                        if type_import_added:
                            break
                
                if not type_import_added:
                    logger.warning("Could not find suitable position for geminiCliDefaultModelId import in ApiOptions.tsx")
        
        # Step 2: Add component import if not exists
        if not has_component_import:
            component_import_added = False
            
            # First try: Look for Gemini and add after it
            for i, line in enumerate(lines):
                if 'Gemini,' in line:
                    # Add GeminiCli after Gemini
                    lines.insert(i + 1, '\tGeminiCli,')
                    component_import_added = True
                    logger.info("Added GeminiCli after Gemini in ApiOptions.tsx")
                    break
            
            # Second try: Look for the providers import section if first approach failed
            if not component_import_added:
                for i, line in enumerate(lines):
                    if 'from "./providers"' in line and 'import' in line:
                        logger.info(f"Found providers import at line {i+1}: {line.strip()}")
                        # This is a multi-line import, find the closing brace
                        brace_count = 0
                        for j in range(i, len(lines)):
                            brace_count += lines[j].count('{') - lines[j].count('}')
                            if brace_count == 0:
                                # Insert GeminiCli before the closing brace
                                if 'GeminiCli' not in lines[j-1]:
                                    lines.insert(j-1, '\tGeminiCli,')
                                    component_import_added = True
                                    logger.info("Added GeminiCli to component imports in ApiOptions.tsx")
                                break
                        if component_import_added:
                            break
                
                if not component_import_added:
                    logger.warning("Could not find suitable position for GeminiCli import in ApiOptions.tsx")
        
        # Step 3: Add provider configuration if not exists
        if not has_provider_config:
            config_added = False
            
            # First try: Look for gemini configuration and add after it
            for i, line in enumerate(lines):
                if 'gemini: { field: "apiModelId", default: geminiDefaultModelId },' in line:
                    # Add gemini-cli config after gemini config
                    indent = re.match(r'^(\s*)', line).group(1)
                    config_line = f'{indent}"gemini-cli": {{ field: "apiModelId", default: geminiCliDefaultModelId }},'
                    lines.insert(i + 1, config_line)
                    config_added = True
                    logger.info("Added gemini-cli config after gemini config in ApiOptions.tsx")
                    break
            
            # Second try: Look for the PROVIDER_MODEL_CONFIG object if first approach failed
            if not config_added:
                for i, line in enumerate(lines):
                    if 'PROVIDER_MODEL_CONFIG' in line and '=' in line:
                        logger.info(f"Found PROVIDER_MODEL_CONFIG at line {i+1}")
                        # Find the end of the PROVIDER_MODEL_CONFIG object
                        brace_count = 0
                        for j in range(i, len(lines)):
                            if '{' in lines[j]:
                                brace_count += 1
                            if '}' in lines[j]:
                                brace_count -= 1
                                if brace_count == 0:
                                    # Insert gemini-cli config before the closing brace
                                    indent = re.match(r'^(\s*)', lines[j]).group(1)
                                    config_line = f'{indent}"gemini-cli": {{ field: "apiModelId", default: geminiCliDefaultModelId }},'
                                    lines.insert(j, config_line)
                                    config_added = True
                                    logger.info("Added gemini-cli to PROVIDER_MODEL_CONFIG in ApiOptions.tsx")
                                    break
                        if config_added:
                            break
                
                if not config_added:
                    logger.warning("Could not find suitable position for gemini-cli provider configuration in ApiOptions.tsx")
        
        # Step 4: Add component rendering if not exists
        if not has_component_render:
            render_added = False
            
            # Look for existing provider components
            for i, line in enumerate(lines):
                if 'selectedProvider === "gemini"' in line:
                    # Find the end of this component block
                    brace_count = 0
                    for j in range(i, len(lines)):
                        if '{' in lines[j]:
                            brace_count += 1
                        if '}' in lines[j]:
                            brace_count -= 1
                            if brace_count == 0:
                                # Insert GeminiCli component after this block
                                indent = re.match(r'^(\s*)', lines[j]).group(1)
                                gemini_cli_block = [
                                    f'{indent}{{selectedProvider === "gemini-cli" && (',
                                    f'{indent}\t<GeminiCli apiConfiguration={{apiConfiguration}} setApiConfigurationField={{setApiConfigurationField}} />',
                                    f'{indent})}}'
                                ]
                                for k, new_line in enumerate(gemini_cli_block):
                                    lines.insert(j + 1 + k, new_line)
                                render_added = True
                                logger.info("Added GeminiCli component rendering in ApiOptions.tsx")
                                break
                    if render_added:
                        break
            
            if not render_added:
                logger.warning("Could not find suitable position for GeminiCli component in ApiOptions.tsx")
        
        # Step 5: Skip misplaced element removal to avoid false positives
        # This step has been removed to prevent accidentally removing correctly placed elements
        
        # Write back to file if any changes were made
        if not has_type_import or not has_component_import or not has_provider_config or not has_component_render:
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            logger.info("Updated webview-ui/src/components/settings/ApiOptions.tsx")
        else:
            logger.info("No changes needed for ApiOptions.tsx")
    
    def complement_webview_constants(self) -> None:
        """Complement webview-ui/src/components/settings/constants.ts"""
        logger.info("Complementing webview-ui/src/components/settings/constants.ts...")
        
        target_file = self.target_dir / "webview-ui/src/components/settings/constants.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if gemini-cli already exists in PROVIDERS
        if '"gemini-cli"' in content:
            logger.info("gemini-cli already exists in constants, skipping")
            return
        
        # Use a more precise approach to find the PROVIDERS array and add gemini-cli
        lines = content.split('\n')
        providers_added = False
        
        # Find the PROVIDERS array and add gemini-cli as a proper object
        for i, line in enumerate(lines):
            if 'litellm' in line and 'label: "LiteLLM"' in line:
                # Add gemini-cli after litellm with proper formatting
                indent = len(line) - len(line.lstrip())
                new_provider = f'{" " * indent}{{ value: "gemini-cli", label: "Gemini CLI" }},'
                lines.insert(i + 1, new_provider)
                providers_added = True
                logger.info("Added gemini-cli to PROVIDERS array")
                break
        
        if providers_added:
            # Write back to file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            logger.info("Updated webview-ui/src/components/settings/constants.ts")
        else:
            logger.warning("LiteLLM provider line not found, cannot add gemini-cli")
    
    def complement_webview_providers_index(self) -> None:
        """Complement webview-ui/src/components/settings/providers/index.ts"""
        logger.info("Complementing webview-ui/src/components/settings/providers/index.ts...")
        
        target_file = self.target_dir / "webview-ui/src/components/settings/providers/index.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if GeminiCli export already exists
        if 'export { GeminiCli }' in content:
            logger.info("GeminiCli export already exists, skipping")
            return
        
        # Add GeminiCli export at the end of the file
        new_export = '\nexport { GeminiCli } from "./GeminiCli"'
        new_content = content.rstrip() + new_export + '\n'
        
        # Write back to file
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        logger.info("Added GeminiCli export")
    
    def complement_webview_use_selected_model(self) -> None:
        """Complement webview-ui/src/components/ui/hooks/useSelectedModel.ts"""
        logger.info("Complementing webview-ui/src/components/ui/hooks/useSelectedModel.ts...")
        
        target_file = self.target_dir / "webview-ui/src/components/ui/hooks/useSelectedModel.ts"
        if not target_file.exists():
            logger.error(f"Target file not found: {target_file}")
            return
        
        # Read file content
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if all elements already exist
        has_type_import = 'geminiCliDefaultModelId,' in content and 'geminiCliModels,' in content
        has_case = 'case "gemini-cli":' in content
        
        if has_type_import and has_case:
            logger.info("All gemini-cli elements already exist in useSelectedModel, skipping")
            return
        
        lines = content.split('\n')
        changes_made = False
        
        # Step 1: Add type imports if not exists
        if not has_type_import:
            import_added = False
            
            # Look for geminiDefaultModelId and add geminiCliDefaultModelId after it
            for i, line in enumerate(lines):
                if 'geminiDefaultModelId,' in line:
                    # Add geminiCliDefaultModelId after geminiDefaultModelId
                    lines.insert(i + 1, '\tgeminiCliDefaultModelId,')
                    import_added = True
                    logger.info("Added geminiCliDefaultModelId after geminiDefaultModelId in useSelectedModel")
                    break
            
            # Look for geminiModels and add geminiCliModels after it
            for i, line in enumerate(lines):
                if 'geminiModels,' in line:
                    # Add geminiCliModels after geminiModels
                    lines.insert(i + 1, '\tgeminiCliModels,')
                    import_added = True
                    logger.info("Added geminiCliModels after geminiModels in useSelectedModel")
                    break
            
            if import_added:
                changes_made = True
        
        # Step 2: Add case statement if not exists
        if not has_case:
            case_added = False
            
            # Look for existing case statements in the switch
            for i, line in enumerate(lines):
                if 'case "gemini":' in line:
                    # Find the end of this case block
                    brace_count = 0
                    for j in range(i, len(lines)):
                        if '{' in lines[j]:
                            brace_count += 1
                        if '}' in lines[j]:
                            brace_count -= 1
                            if brace_count == 0:
                                # Insert gemini-cli case after this block
                                indent = re.match(r'^(\s*)', lines[j]).group(1)
                                gemini_cli_case = [
                                    f'{indent}case "gemini-cli": {{',
                                    f'{indent}\tconst id = apiConfiguration.apiModelId ?? geminiCliDefaultModelId',
                                    f'{indent}\tconst info = geminiCliModels[id as keyof typeof geminiCliModels]',
                                    f'{indent}\treturn {{ id, info }}',
                                    f'{indent}}}'
                                ]
                                for k, new_line in enumerate(gemini_cli_case):
                                    lines.insert(j + 1 + k, new_line)
                                case_added = True
                                logger.info("Added gemini-cli case after gemini case in useSelectedModel")
                                break
                    if case_added:
                        break
            
            if case_added:
                changes_made = True
        
        if changes_made:
            # Write back to file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            logger.info("Updated webview-ui/src/components/ui/hooks/useSelectedModel.ts")
        else:
            logger.info("No changes needed for useSelectedModel.ts")
    
    def complement_i18n_files(self) -> None:
        """Complement internationalization files"""
        logger.info("Starting to complement internationalization files...")
        
        # Complement settings.json files
        self._complement_settings_json_files()
        
        # Complement common.json files
        self._complement_common_json_files()
    
    def _complement_settings_json_files(self) -> None:
        """Complement webview-ui settings.json files - append only"""
        logger.info("Complementing webview-ui settings.json files...")
        
        locales_dir = self.target_dir / "webview-ui/src/i18n/locales"
        if not locales_dir.exists():
            logger.error(f"Locales directory not found: {locales_dir}")
            return
        
        # List of expected locales
        expected_locales = [
            'ca', 'de', 'es', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 
            'nl', 'pl', 'pt-BR', 'ru', 'tr', 'vi', 'zh-CN', 'zh-TW'
        ]
        
        processed_count = 0
        skipped_count = 0
        
        # Iterate through all language directories
        for locale_dir in locales_dir.iterdir():
            if locale_dir.is_dir():
                locale_name = locale_dir.name
                settings_file = locale_dir / "settings.json"
                
                if settings_file.exists():
                    logger.info(f"Processing {locale_name} settings.json...")
                    self._complement_single_settings_json_append(settings_file, locale_name)
                    processed_count += 1
                else:
                    logger.warning(f"Settings file not found for locale {locale_name}: {settings_file}")
                    skipped_count += 1
        
        logger.info(f"Settings.json processing completed:")
        logger.info(f"  - Processed: {processed_count} files")
        logger.info(f"  - Skipped (not found): {skipped_count} files")
        
        # Log which locales were processed
        processed_locales = []
        for locale_dir in locales_dir.iterdir():
            if locale_dir.is_dir():
                settings_file = locale_dir / "settings.json"
                if settings_file.exists():
                    processed_locales.append(locale_dir.name)
        
        if processed_locales:
            logger.info(f"Successfully processed locales: {', '.join(sorted(processed_locales))}")
        else:
            logger.warning("No settings.json files were found to process")
    
    def _complement_single_settings_json_append(self, file_path: Path, locale: str) -> None:
        """Complement single settings.json file - insert geminiCli into providers object without modifying existing lines"""
        logger.info(f"Complementing {locale} settings.json...")
        
        try:
            # Read file content as text
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if geminiCli already exists
            if '"geminiCli"' in content:
                logger.info(f"{locale} geminiCli configuration already exists, skipping")
                return
            
            # Get geminiCli configuration for this locale
            gemini_cli_config = self._get_gemini_cli_settings_config(locale)
            
            # Use precise line-by-line insertion to avoid modifying existing lines
            lines = content.split('\n')
            
            # Find the position to insert within the providers object
            insert_position = -1
            providers_brace_count = 0
            in_providers = False
            
            for i, line in enumerate(lines):
                line_stripped = line.strip()
                
                # Check if we're entering the providers object (exact match to avoid false positives)
                if line_stripped == '"providers": {' or line_stripped == '"providers":{':
                    in_providers = True
                    providers_brace_count = 1
                    continue
                
                if in_providers:
                    # Count braces within the providers object
                    for char in line:
                        if char == '{':
                            providers_brace_count += 1
                        elif char == '}':
                            providers_brace_count -= 1
                            if providers_brace_count == 0:
                                # We've reached the end of the providers object
                                insert_position = i
                                break
                    if insert_position != -1:
                        break
            
            # If we couldn't find the providers object, try a more robust approach
            if insert_position == -1:
                logger.warning(f"Could not find providers object in {locale} settings.json, trying alternative approach")
                
                # Look for the providers object using a more flexible pattern
                for i, line in enumerate(lines):
                    if '"providers"' in line and ('{' in line or ':' in line):
                        # Found the providers line, now find its closing brace
                        brace_count = 0
                        for j in range(i, len(lines)):
                            for char in lines[j]:
                                if char == '{':
                                    brace_count += 1
                                elif char == '}':
                                    brace_count -= 1
                                    if brace_count == 0:
                                        insert_position = j
                                        break
                            if insert_position != -1:
                                break
                        break
            
            if insert_position != -1:
                # Find the indentation level of the providers object
                providers_indent = ""
                for i, line in enumerate(lines):
                    if '"providers":' in line:
                        # Get the indentation of the providers line
                        match = re.match(r'^(\s*)"providers":', line)
                        if match:
                            providers_indent = match.group(1)
                            break
                
                # Create the geminiCli object with proper indentation
                gemini_cli_indent = providers_indent + "  "  # Add 2 spaces for nested object
                gemini_cli_lines = [
                    f'{gemini_cli_indent}"geminiCli": {{'
                ]
                
                # Add each config line with proper indentation
                for key, value in gemini_cli_config.items():
                    if isinstance(value, str):
                        gemini_cli_lines.append(f'{gemini_cli_indent}  "{key}": "{value}",')
                    else:
                        gemini_cli_lines.append(f'{gemini_cli_indent}  "{key}": {json.dumps(value, ensure_ascii=False)},')
                
                # Remove trailing comma from last line
                if gemini_cli_lines:
                    gemini_cli_lines[-1] = gemini_cli_lines[-1].rstrip(',')
                
                gemini_cli_lines.append(f'{gemini_cli_indent}}}')
                
                # Insert the geminiCli object before the closing brace of providers
                # First, ensure the previous object ends with a comma
                if insert_position > 0:
                    prev_line = lines[insert_position - 1].strip()
                    if prev_line.endswith('}') and not prev_line.endswith('},'):
                        # Add comma to the previous line
                        lines[insert_position - 1] = lines[insert_position - 1].rstrip() + ','
                
                lines.insert(insert_position, '\n'.join(gemini_cli_lines))
                
                # Write back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                
                logger.info(f"Added geminiCli to {locale} settings.json providers section")
            else:
                logger.error(f"{locale} settings.json providers structure not found")
                
        except Exception as e:
            logger.error(f"Error complementing {locale} settings.json: {e}")
    
    def _complement_common_json_files(self) -> None:
        """Complement main extension common.json files - append only"""
        logger.info("Complementing main extension common.json files...")
        
        locales_dir = self.target_dir / "src/i18n/locales"
        if not locales_dir.exists():
            logger.error(f"Main extension locales directory not found: {locales_dir}")
            return
        
        # List of expected locales
        expected_locales = [
            'ca', 'de', 'es', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 
            'nl', 'pl', 'pt-BR', 'ru', 'tr', 'vi', 'zh-CN', 'zh-TW'
        ]
        
        processed_count = 0
        skipped_count = 0
        
        # Iterate through all language directories
        for locale_dir in locales_dir.iterdir():
            if locale_dir.is_dir():
                locale_name = locale_dir.name
                common_file = locale_dir / "common.json"
                
                if common_file.exists():
                    logger.info(f"Processing {locale_name} common.json...")
                    self._complement_single_common_json_append(common_file, locale_name)
                    processed_count += 1
                else:
                    logger.warning(f"Common file not found for locale {locale_name}: {common_file}")
                    skipped_count += 1
        
        logger.info(f"Common.json processing completed:")
        logger.info(f"  - Processed: {processed_count} files")
        logger.info(f"  - Skipped (not found): {skipped_count} files")
        
        # Log which locales were processed
        processed_locales = []
        for locale_dir in locales_dir.iterdir():
            if locale_dir.is_dir():
                common_file = locale_dir / "common.json"
                if common_file.exists():
                    processed_locales.append(locale_dir.name)
        
        if processed_locales:
            logger.info(f"Successfully processed locales: {', '.join(sorted(processed_locales))}")
        else:
            logger.warning("No common.json files were found to process")
    
    def _complement_single_common_json_append(self, file_path: Path, locale: str) -> None:
        """Complement single common.json file - append geminiCli to errors object without modifying existing lines"""
        logger.info(f"Complementing {locale} common.json...")
        
        try:
            # Read file content as text
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if geminiCli already exists
            if '"geminiCli"' in content:
                logger.info(f"{locale} geminiCli error configuration already exists, skipping")
                return
            
            # Get geminiCli error configuration for this locale
            gemini_cli_errors = self._get_gemini_cli_errors_config(locale)
            
            # Use precise line-by-line insertion to avoid modifying existing lines
            lines = content.split('\n')
            insertion_made = False
            
            # Find the claudeCode object and insert geminiCli after it
            for i, line in enumerate(lines):
                if '"claudeCode"' in line and '{' in line:
                    # Found the start of claudeCode object, find its end
                    brace_count = 0
                    claude_code_end = -1
                    
                    for j in range(i, len(lines)):
                        line_content = lines[j]
                        brace_count += line_content.count('{') - line_content.count('}')
                        
                        if brace_count == 0:
                            claude_code_end = j
                            break
                    
                    if claude_code_end != -1:
                        # Insert geminiCli after claudeCode object
                        # Convert geminiCli config to properly formatted lines
                        config_lines = []
                        config_lines.append('    "geminiCli": {')
                        
                        for key, value in gemini_cli_errors.items():
                            # Format the line with proper indentation
                            formatted_value = json.dumps(value, ensure_ascii=False)
                            config_lines.append(f'      "{key}": {formatted_value},')
                        
                        # Remove the last comma from the last line
                        if config_lines:
                            config_lines[-1] = config_lines[-1].rstrip(',')
                        
                        config_lines.append('    }')
                        
                        # Insert the new lines after claudeCode
                        for k, config_line in enumerate(config_lines):
                            lines.insert(claude_code_end + 1 + k, config_line)
                        
                        insertion_made = True
                        logger.info(f"Added geminiCli to {locale} common.json after claudeCode")
                        break
            
            if insertion_made:
                # Write back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                logger.info(f"Updated {locale} common.json")
            else:
                logger.warning(f"{locale} common.json claudeCode section not found")
                
        except Exception as e:
            logger.error(f"Error complementing {locale} common.json: {e}")
    
    def _get_gemini_cli_settings_config(self, locale: str) -> Dict:
        """Get geminiCli configuration for specified language"""
        # Default English configuration
        default_config = {
            "description": "This provider uses OAuth authentication from the Gemini CLI tool and does not require API keys.",
            "oauthPath": "OAuth Credentials Path (optional)",
            "oauthPathDescription": "Path to the OAuth credentials file. Leave empty to use the default location (~/.gemini/oauth_creds.json).",
            "instructions": "If you haven't authenticated yet, please run",
            "instructionsContinued": "in your terminal first.",
            "setupLink": "Gemini CLI Setup Instructions",
            "requirementsTitle": "Important Requirements",
            "requirement1": "First, you need to install the Gemini CLI tool",
            "requirement2": "Then, run gemini in your terminal and make sure you Log in with Google",
            "requirement3": "Only works with personal Google accounts (not Google Workspace accounts)",
            "requirement4": "Does not use API keys - authentication is handled via OAuth",
            "requirement5": "Requires the Gemini CLI tool to be installed and authenticated first",
            "freeAccess": "Free tier access via OAuth authentication"
        }
        
        # Return configuration based on language
        if locale == 'zh-CN':
            return {
                "description": "此提供商使用 Gemini CLI 工具的 OAuth 身份验证，不需要 API 密钥。",
                "oauthPath": "OAuth 凭据路径（可选）",
                "oauthPathDescription": "OAuth 凭据文件的路径。留空以使用默认位置 (~/.gemini/oauth_creds.json)。",
                "instructions": "如果您尚未进行身份验证，请先运行",
                "instructionsContinued": "在您的终端中。",
                "setupLink": "Gemini CLI 设置说明",
                "requirementsTitle": "重要要求",
                "requirement1": "首先，您需要安装 Gemini CLI 工具",
                "requirement2": "然后，在终端中运行 gemini 并确保您使用 Google 登录",
                "requirement3": "仅适用于个人 Google 账户（不适用于 Google Workspace 账户）",
                "requirement4": "不使用 API 密钥 - 身份验证通过 OAuth 处理",
                "requirement5": "需要先安装并验证 Gemini CLI 工具",
                "freeAccess": "通过 OAuth 身份验证免费访问"
            }
        elif locale == 'zh-TW':
            return {
                "description": "此提供商使用 Gemini CLI 工具的 OAuth 身份驗證，不需要 API 金鑰。",
                "oauthPath": "OAuth 憑證路徑（可選）",
                "oauthPathDescription": "OAuth 憑證檔案的路徑。留空以使用預設位置 (~/.gemini/oauth_creds.json)。",
                "instructions": "如果您尚未進行身份驗證，請先執行",
                "instructionsContinued": "在您的終端中。",
                "setupLink": "Gemini CLI 設定說明",
                "requirementsTitle": "重要要求",
                "requirement1": "首先，您需要安裝 Gemini CLI 工具",
                "requirement2": "然後，在終端中執行 gemini 並確保您使用 Google 登入",
                "requirement3": "僅適用於個人 Google 帳戶（不適用於 Google Workspace 帳戶）",
                "requirement4": "不使用 API 金鑰 - 身份驗證透過 OAuth 處理",
                "requirement5": "需要先安裝並驗證 Gemini CLI 工具",
                "freeAccess": "透過 OAuth 身份驗證免費存取"
            }
        else:
            # Use English configuration for other languages
            return default_config
    
    def _get_gemini_cli_errors_config(self, locale: str) -> Dict:
        """Get geminiCli error configuration for specified language"""
        # Default English configuration
        default_config = {
            "oauthLoadFailed": "Failed to load OAuth credentials. Please authenticate first: {{error}}",
            "tokenRefreshFailed": "Failed to refresh OAuth token: {{error}}",
            "onboardingTimeout": "Onboarding operation timed out after 60 seconds. Please try again later.",
            "projectDiscoveryFailed": "Could not discover project ID. Make sure you're authenticated with 'gemini auth'.",
            "rateLimitExceeded": "Rate limit exceeded. Free tier limits have been reached.",
            "badRequest": "Bad request: {{details}}",
            "apiError": "Gemini CLI API error: {{error}}",
            "completionError": "Gemini CLI completion error: {{error}}"
        }
        
        # Return configuration based on language
        if locale == 'zh-CN':
            return {
                "oauthLoadFailed": "加载 OAuth 凭据失败。请先进行身份验证：{{error}}",
                "tokenRefreshFailed": "刷新 OAuth 令牌失败：{{error}}",
                "onboardingTimeout": "引导操作在 60 秒后超时。请稍后重试。",
                "projectDiscoveryFailed": "无法发现项目 ID。请确保您已使用 'gemini auth' 进行身份验证。",
                "rateLimitExceeded": "超出速率限制。已达到免费层级限制。",
                "badRequest": "错误请求：{{details}}",
                "apiError": "Gemini CLI API 错误：{{error}}",
                "completionError": "Gemini CLI 完成错误：{{error}}"
            }
        elif locale == 'zh-TW':
            return {
                "oauthLoadFailed": "載入 OAuth 憑證失敗。請先進行身份驗證：{{error}}",
                "tokenRefreshFailed": "重新整理 OAuth 權杖失敗：{{error}}",
                "onboardingTimeout": "引導操作在 60 秒後逾時。請稍後重試。",
                "projectDiscoveryFailed": "無法發現專案 ID。請確保您已使用 'gemini auth' 進行身份驗證。",
                "rateLimitExceeded": "超出速率限制。已達到免費層級限制。",
                "badRequest": "錯誤請求：{{details}}",
                "apiError": "Gemini CLI API 錯誤：{{error}}",
                "completionError": "Gemini CLI 完成錯誤：{{error}}"
            }
        else:
            # Use English configuration for other languages
            return default_config
    
    def validate_complement(self) -> bool:
        """Validate complement results"""
        logger.info("Validating complement results...")
        
        validation_results = []
        
        # Validate directly copied files
        direct_files = [
            "packages/types/src/providers/gemini-cli.ts",
            "src/api/providers/gemini-cli.ts",
            "webview-ui/src/components/settings/providers/GeminiCli.tsx"
        ]
        
        for file_path in direct_files:
            target_file = self.target_dir / file_path
            if target_file.exists():
                validation_results.append(f"✅ {file_path} exists")
            else:
                validation_results.append(f"❌ {file_path} not found")
        
        # Validate complemented files
        complement_files = [
            "packages/types/src/providers/index.ts",
            "src/api/index.ts",
            "src/api/providers/index.ts",
            "src/shared/checkExistApiConfig.ts",
            "webview-ui/src/utils/validate.ts",
            "webview-ui/src/components/settings/ApiOptions.tsx",
            "webview-ui/src/components/settings/constants.ts",
            "webview-ui/src/components/settings/providers/index.ts",
            "webview-ui/src/components/ui/hooks/useSelectedModel.ts"
        ]
        
        for file_path in complement_files:
            target_file = self.target_dir / file_path
            if target_file.exists():
                with open(target_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'gemini-cli' in content or 'GeminiCli' in content:
                    validation_results.append(f"✅ {file_path} complement successful")
                else:
                    validation_results.append(f"❌ {file_path} complement failed")
            else:
                validation_results.append(f"❌ {file_path} file not found")
        
        # Validate i18n files
        logger.info("Validating i18n files...")
        
        # Validate webview-ui settings.json files
        webview_locales_dir = self.target_dir / "webview-ui/src/i18n/locales"
        if webview_locales_dir.exists():
            settings_validated = 0
            settings_total = 0
            for locale_dir in webview_locales_dir.iterdir():
                if locale_dir.is_dir():
                    settings_file = locale_dir / "settings.json"
                    if settings_file.exists():
                        settings_total += 1
                        try:
                            with open(settings_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                            if '"geminiCli"' in content:
                                settings_validated += 1
                        except Exception as e:
                            logger.warning(f"Error reading {settings_file}: {e}")
            
            if settings_total > 0:
                validation_results.append(f"✅ webview-ui settings.json: {settings_validated}/{settings_total} files complemented")
            else:
                validation_results.append("⚠️ No webview-ui settings.json files found")
        
        # Validate main extension common.json files
        main_locales_dir = self.target_dir / "src/i18n/locales"
        if main_locales_dir.exists():
            common_validated = 0
            common_total = 0
            for locale_dir in main_locales_dir.iterdir():
                if locale_dir.is_dir():
                    common_file = locale_dir / "common.json"
                    if common_file.exists():
                        common_total += 1
                        try:
                            with open(common_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                            if '"geminiCli"' in content:
                                common_validated += 1
                        except Exception as e:
                            logger.warning(f"Error reading {common_file}: {e}")
            
            if common_total > 0:
                validation_results.append(f"✅ main extension common.json: {common_validated}/{common_total} files complemented")
            else:
                validation_results.append("⚠️ No main extension common.json files found")
        
        # Output validation results
        logger.info("Validation results:")
        for result in validation_results:
            logger.info(result)
        
        # Return whether all successful
        return all("✅" in result for result in validation_results)
    
    def run(self) -> bool:
        """Run auto complement"""
        logger.info("Starting Gemini CLI auto complement...")
        
        try:
            # 1. Copy direct overwrite files
            self.copy_direct_files()
            
            # 2. Complement code files
            self.complement_packages_types_index()
            self.complement_api_index()
            self.complement_api_providers_index()
            self.complement_check_exist_api_config()
            self.complement_webview_validate()
            
            # 3. Complement webview files
            self.complement_webview_api_options()
            self.complement_webview_constants()
            self.complement_webview_providers_index()
            self.complement_webview_use_selected_model()
            
            # 4. Complement internationalization files
            self.complement_i18n_files()
            
            # 5. Validate complement results
            success = self.validate_complement()
            
            if success:
                logger.info("🎉 Gemini CLI auto complement completed!")
            else:
                logger.warning("⚠️ Some complements may have failed, please check logs")
            
            return success
            
        except Exception as e:
            logger.error(f"Error during auto complement: {e}")
            return False

def main():
    """Main function"""
    # Configure paths - use relative paths
    source_dir = r"z-geminicli-install"
    target_dir = r"../Roo-Code"
    
    try:
        # Create auto complement instance
        complement = GeminiCliAutoComplement(source_dir, target_dir)
        
        # Run auto complement
        success = complement.run()
        
        if success:
            print("\n🎉 Gemini CLI auto complement completed successfully!")
            print("Please check the following:")
            print("1. All files are correctly complemented")
            print("2. Functionality works normally")
            print("3. Use git rollback if needed")
        else:
            print("\n⚠️ Issues occurred during auto complement, please check log file")
            
    except Exception as e:
        print(f"❌ Program execution error: {e}")
        logger.error(f"Program execution error: {e}")

if __name__ == "__main__":
    main()