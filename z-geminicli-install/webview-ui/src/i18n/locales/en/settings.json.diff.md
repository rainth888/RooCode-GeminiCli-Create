# webview-ui/src/i18n/locales/en/settings.json 补全说明

## 目标文件路径

`webview-ui/src/i18n/locales/en/settings.json`

## 补全位置

在 `providers` 部分的 `claudeCode` 配置之后，`browser` 部分之前插入 `geminiCli` 字段

## 精确补全指导

### 方法一：手动补全（推荐）

1. **定位插入位置**：
   - 在文件中搜索 `"claudeCode": {`
   - 找到 `claudeCode` 配置的结束位置（通常在 `}` 之后）

2. **插入位置示例**：
   ```json
   "claudeCode": {
       "pathLabel": "Claude Code Path",
       "description": "Optional path to your Claude Code CLI. Defaults to 'claude' if not set.",
       "placeholder": "Default: claude",
       "maxTokensLabel": "Max Output Tokens",
       "maxTokensDescription": "Maximum output tokens for Claude Code responses. Default is 8000."
   },
   "geminiCli": {
       // 在这里插入 geminiCli 配置
   },
   "browser": {
       // browser 配置开始
   ```

### 方法二：自动化补全

如果使用自动化工具，请使用以下精确的上下文匹配：

#### 旧字符串（old_string）
```json
		"claudeCode": {
			"pathLabel": "Claude Code Path",
			"description": "Optional path to your Claude Code CLI. Defaults to 'claude' if not set.",
			"placeholder": "Default: claude",
			"maxTokensLabel": "Max Output Tokens",
			"maxTokensDescription": "Maximum output tokens for Claude Code responses. Default is 8000."
		}
	},
	"browser": {
```

#### 新字符串（new_string）
```json
		"claudeCode": {
			"pathLabel": "Claude Code Path",
			"description": "Optional path to your Claude Code CLI. Defaults to 'claude' if not set.",
			"placeholder": "Default: claude",
			"maxTokensLabel": "Max Output Tokens",
			"maxTokensDescription": "Maximum output tokens for Claude Code responses. Default is 8000."
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
	},
	"browser": {
```

## 补全内容

```json
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
```

## 操作说明

1. **检查现有内容**：确保 `geminiCli` 配置尚未存在
2. **精确定位**：在 `claudeCode` 配置结束后，`browser` 部分开始前插入
3. **格式验证**：确保 JSON 格式正确，包括逗号分隔
4. **保持一致性**：保持与现有代码相同的缩进风格

## 错误处理

如果遇到 `Failed to edit, could not find the string to replace` 错误：

1. **重新读取文件**：获取最新的文件内容
2. **检查格式差异**：确认空格、换行符和标点符号完全匹配
3. **扩大上下文**：在 `old_string` 中包含更多上下文内容
4. **手动验证**：手动检查目标位置是否存在
5. **使用手动方法**：如果自动替换失败，使用手动编辑方法

## 验证步骤

补全完成后，请验证：

1. **JSON 格式正确性**：使用 JSON 验证工具检查
2. **功能测试**：确保 Gemini CLI 功能正常工作
3. **UI 显示**：检查设置界面中是否正确显示 Gemini CLI 选项
