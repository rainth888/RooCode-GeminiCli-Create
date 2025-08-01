# 多语言文档末尾补全策略

## 概述

为了保持多语言文档的完整性和便于 Git 比对，所有多语言文档的补全都采用**末尾补全策略**。这种策略确保新增内容不会影响现有代码结构，同时便于版本控制和维护。

## 策略原则

### 1. 末尾补全原则
- **不插入到中间位置**：避免影响现有代码结构
- **在对象末尾添加新配置**：保持代码完整性
- **便于 Git 比对差异**：新增内容清晰可见
- **保持现有顺序**：不改变现有配置的顺序

### 2. 优势
- ✅ **代码完整性**：不影响现有配置的结构和顺序
- ✅ **Git 友好**：新增内容在文件末尾，便于比对
- ✅ **维护性**：后续更新和维护更加容易
- ✅ **可读性**：新增内容清晰可见，便于理解

## 具体实现

### 1. settings.json 补全策略

#### 1.1 补全位置
在 `providers` 对象的末尾添加 `geminiCli` 配置。

#### 1.2 补全前
```json
{
  "providers": {
    "anthropic": {
      "description": "Anthropic Claude API provider"
    },
    "claudeCode": {
      "description": "Claude Code CLI provider"
    },
    "browser": {
      "description": "Browser-based provider"
    }
  }
}
```

#### 1.3 补全后
```json
{
  "providers": {
    "anthropic": {
      "description": "Anthropic Claude API provider"
    },
    "claudeCode": {
      "description": "Claude Code CLI provider"
    },
    "browser": {
      "description": "Browser-based provider"
    },
    "geminiCli": {
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
  }
}
```

### 2. common.json 补全策略

#### 2.1 补全位置
在 `errors` 对象的末尾添加 `geminiCli` 错误配置。

#### 2.2 补全前
```json
{
  "errors": {
    "anthropic": {
      "apiKeyMissing": "API key is required"
    },
    "claudeCode": {
      "pathNotFound": "Claude Code CLI not found"
    },
    "otherErrors": {
      "general": "An error occurred"
    }
  }
}
```

#### 2.3 补全后
```json
{
  "errors": {
    "anthropic": {
      "apiKeyMissing": "API key is required"
    },
    "claudeCode": {
      "pathNotFound": "Claude Code CLI not found"
    },
    "otherErrors": {
      "general": "An error occurred"
    },
    "geminiCli": {
      "oauthLoadFailed": "Failed to load OAuth credentials. Please authenticate first: {{error}}",
      "tokenRefreshFailed": "Failed to refresh OAuth token: {{error}}",
      "onboardingTimeout": "Onboarding operation timed out after 60 seconds. Please try again later.",
      "projectDiscoveryFailed": "Could not discover project ID. Make sure you're authenticated with 'gemini auth'.",
      "rateLimitExceeded": "Rate limit exceeded. Free tier limits have been reached.",
      "badRequest": "Bad request: {{details}}",
      "apiError": "Gemini CLI API error: {{error}}",
      "completionError": "Gemini CLI completion error: {{error}}"
    }
  }
}
```

## 自动化脚本支持

### Python 脚本实现
```python
def _complement_single_settings_json(self, file_path: Path, locale: str) -> None:
    """Complement single settings.json file - append at end"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if geminiCli already exists
        if 'providers' in data and 'geminiCli' in data['providers']:
            logger.info(f"{locale} geminiCli configuration already exists, skipping")
            return
        
        # Get geminiCli configuration
        gemini_cli_config = self._get_gemini_cli_settings_config(locale)
        
        # Add geminiCli configuration to providers section at the end
        if 'providers' in data:
            # Simply add to the end of providers object
            data['providers']['geminiCli'] = gemini_cli_config
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Added geminiCli to {locale} settings.json at the end")
        else:
            logger.warning(f"{locale} settings.json providers section not found")
            
    except Exception as e:
        logger.error(f"Error complementing {locale} settings.json: {e}")
```

### 关键特点
- **简单添加**：直接使用 `data['providers']['geminiCli'] = gemini_cli_config`
- **末尾位置**：JSON 对象会自动将新键值对添加到末尾
- **保持格式**：使用 `json.dump` 保持正确的格式和缩进

## Git 比对优势

### 1. 清晰的差异显示
```diff
{
  "providers": {
    "anthropic": { ... },
    "claudeCode": { ... },
    "browser": { ... },
+   "geminiCli": {
+     "description": "This provider uses OAuth authentication...",
+     "oauthPath": "OAuth Credentials Path (optional)",
+     // ... 其他配置
+   }
  }
}
```

### 2. 易于审查
- 新增内容在文件末尾，一目了然
- 不影响现有代码的比对
- 便于代码审查和合并

### 3. 冲突减少
- 减少与现有代码的冲突
- 降低合并冲突的可能性
- 便于自动化处理

## 验证检查

### 1. 结构完整性检查
- [ ] 现有配置的顺序保持不变
- [ ] 新增配置在对象末尾
- [ ] JSON 格式正确

### 2. 内容完整性检查
- [ ] 所有必要的配置项都已添加
- [ ] 翻译内容正确
- [ ] 没有遗漏任何语言

### 3. Git 比对检查
- [ ] 差异显示清晰
- [ ] 新增内容易于识别
- [ ] 没有意外的修改

## 注意事项

1. **严格遵循末尾策略**：绝对不在中间位置插入内容
2. **保持现有结构**：不改变现有配置的顺序和结构
3. **格式一致性**：保持与现有代码相同的格式和缩进
4. **测试验证**：补全后必须验证功能正常
5. **文档更新**：及时更新相关文档说明

---

**总结**：末尾补全策略是保持代码完整性和便于版本控制的最佳实践，必须严格遵循。