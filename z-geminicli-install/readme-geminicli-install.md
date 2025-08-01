# Gemini CLI 补全说明文档

## 概述

本文档用于指导在 Roo-Code 新版本中补全 Gemini CLI 相关代码。采用"逆向补全"策略，从旧版本（3.22.4）中提取 `geminicli` 相关代码，补全到新版本（3.22.5+）中。

## 严格操作规范（必须遵循）

### 12.1 绝对禁止删除原则
- **绝对不允许删除任何现有代码**，包括看起来与 gemini-cli 相关的代码
- **只能进行新增操作**，不能进行删除或替换操作
- **保留所有现有代码**，即使看起来与 gemini-cli 相关

### 12.2 逆向补全的严格定义
- **逆向补全** = 只添加缺失的代码，绝对不删除现有代码
- **具体示例**：在 `src/api/index.ts` 中，添加 `GeminiCliHandler` 导入和 `case "gemini-cli"` 是正确的，但删除 `apiProvider satisfies "gemini-cli" | undefined` 是错误的，必须保留

### 12.2.1 具体示例
```typescript
// 在 src/api/index.ts 中
// ✅ 正确操作：添加导入
import { GeminiCliHandler } from "./providers/gemini-cli"

// ✅ 正确操作：添加 case 分支
case "gemini-cli":
  return new GeminiCliHandler(options)

// ❌ 错误操作：删除现有代码
// 这行代码必须保留，不能删除：
apiProvider satisfies "gemini-cli" | undefined
```

### 12.3 验证检查清单
- [ ] 所有原始代码都保留
- [ ] 只添加必要的 gemini-cli 代码
- [ ] 没有删除任何现有功能
- [ ] 新功能正常工作

## 文件复制策略（重要）

### 13.1 需要复制的文件
以下文件会被直接复制到目标项目中：
- `packages/types/src/providers/gemini-cli.ts`
- `src/api/providers/gemini-cli.ts`
- `src/api/providers/__tests__/gemini-cli.spec.ts`
- `webview-ui/src/components/settings/providers/GeminiCli.tsx`
- `webview-ui/src/components/settings/providers/__tests__/GeminiCli.spec.tsx`
- 其他所有相关的代码文件

### 13.2 不复制到项目的文件
以下文件**不会**被复制到目标项目中，它们只是补全指导文档：
- `readme-geminicli-install.md` - 本说明文档
- `IMPROVEMENTS.md` - 改进说明文档
- `COMPLETED_FILES.md` - 已完成文件列表
- `APPEND_STRATEGY.md` - 末尾补全策略文档
- `batch-complement-i18n.js` - 批处理脚本
- `batch-complement-common-i18n.js` - 批处理脚本
- **所有 `.diff.md` 文件** - 补全指导文档，如：
  - `src/api/providers/index.ts.diff.md`
  - `src/i18n/locales/ca/common.json.diff.md`
  - `src/i18n/locales/de/common.json.diff.md`
  - `src/i18n/locales/en/common.json.diff.md`
  - `src/i18n/locales/es/common.json.diff.md`
  - `webview-ui/src/utils/validate.ts.diff.md`
  - 等等...

### 13.3 自动化脚本过滤规则
Python 自动化脚本会自动过滤以下文件：
```python
# 按文件名过滤
skip_files = {
    'readme-geminicli-install.md',
    'IMPROVEMENTS.md',
    'COMPLETED_FILES.md',
    'APPEND_STRATEGY.md',
    'batch-complement-i18n.js',
    'batch-complement-common-i18n.js'
}

# 按文件模式过滤
skip_patterns = [
    r'\.diff\.md$',  # 跳过所有 .diff.md 文件
]
```

## 多语言文档补全策略（重要更新）

### 14.1 末尾补全原则
为了保持多语言文档的完整性和便于 Git 比对，所有多语言文档的补全都采用**末尾补全策略**：

- **不插入到中间位置**，避免影响现有代码结构
- **在对象末尾添加新配置**，保持代码完整性
- **便于 Git 比对差异**，新增内容清晰可见

### 14.2 settings.json 补全策略

#### 14.2.1 补全位置
在 `providers` 对象的末尾添加 `geminiCli` 配置，而不是插入到 `claudeCode` 之后。

#### 14.2.2 补全示例
```json
{
  "providers": {
    "anthropic": { ... },
    "claudeCode": { ... },
    "browser": { ... },
    // 在末尾添加 geminiCli 配置
    "geminiCli": {
      "description": "This provider uses OAuth authentication...",
      "oauthPath": "OAuth Credentials Path (optional)",
      // ... 其他配置
    }
  }
}
```

#### 14.2.3 优势
- ✅ 不影响现有配置的顺序和结构
- ✅ Git 比对时新增内容清晰可见
- ✅ 便于后续维护和更新
- ✅ 保持代码的完整性

### 14.3 common.json 补全策略

#### 14.3.1 补全位置
在 `errors` 对象的末尾添加 `geminiCli` 错误配置。

#### 14.3.2 补全示例
```json
{
  "errors": {
    "anthropic": { ... },
    "claudeCode": { ... },
    "otherErrors": { ... },
    // 在末尾添加 geminiCli 错误配置
    "geminiCli": {
      "oauthLoadFailed": "Failed to load OAuth credentials...",
      "tokenRefreshFailed": "Failed to refresh OAuth token...",
      // ... 其他错误配置
    }
  }
}
```

### 14.4 自动化脚本支持
Python 自动化脚本已更新，支持末尾补全策略：
- 自动在对象末尾添加新配置
- 不插入到中间位置
- 保持现有代码结构完整

## 补全文件列表

### 1. 直接复制的文件（会被复制到项目）
- `packages/types/src/providers/gemini-cli.ts`
- `src/api/providers/gemini-cli.ts`
- `src/api/providers/__tests__/gemini-cli.spec.ts`
- `webview-ui/src/components/settings/providers/GeminiCli.tsx`
- `webview-ui/src/components/settings/providers/__tests__/GeminiCli.spec.tsx`

### 2. 需要补全的文件

#### 2.1 packages/types/src/providers/index.ts
```typescript
// 添加导出
export * from "./gemini-cli.js"
```

#### 2.2 src/api/index.ts
```typescript
// 添加导入
import { GeminiCliHandler } from "./providers/gemini-cli"

// 添加 case 分支
case "gemini-cli":
  return new GeminiCliHandler(options)
```

#### 2.3 src/api/providers/index.ts
```typescript
// 添加导出
export { GeminiCliHandler } from "./gemini-cli"
```

#### 2.4 src/shared/checkExistApiConfig.ts
```typescript
// 添加到特殊 provider 数组
["human-relay", "fake-ai", "claude-code", "gemini-cli"]
```

#### 2.5 webview-ui/src/utils/validate.ts
```typescript
// 在 validateModelsAndKeysProvided 函数的 switch 语句中添加
case "gemini-cli":
  return true; // gemini-cli 不需要 API key 验证
```

#### 2.6 多语言文件（末尾补全）

##### 2.6.1 webview-ui/src/i18n/locales/*/settings.json
在 `providers` 对象末尾添加：
```json
"geminiCli": {
  "description": "This provider uses OAuth authentication...",
  "oauthPath": "OAuth Credentials Path (optional)",
  "oauthPathDescription": "Path to the OAuth credentials file...",
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

##### 2.6.2 src/i18n/locales/*/common.json
在 `errors` 对象末尾添加：
```json
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
```

## 多语言翻译内容

### 中文简体 (zh-CN)

#### settings.json
```json
"geminiCli": {
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
```

#### common.json
```json
"geminiCli": {
  "oauthLoadFailed": "加载 OAuth 凭据失败。请先进行身份验证：{{error}}",
  "tokenRefreshFailed": "刷新 OAuth 令牌失败：{{error}}",
  "onboardingTimeout": "引导操作在 60 秒后超时。请稍后重试。",
  "projectDiscoveryFailed": "无法发现项目 ID。请确保您已使用 'gemini auth' 进行身份验证。",
  "rateLimitExceeded": "超出速率限制。已达到免费层级限制。",
  "badRequest": "错误请求：{{details}}",
  "apiError": "Gemini CLI API 错误：{{error}}",
  "completionError": "Gemini CLI 完成错误：{{error}}"
}
```

### 中文繁体 (zh-TW)

#### settings.json
```json
"geminiCli": {
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
```

#### common.json
```json
"geminiCli": {
  "oauthLoadFailed": "載入 OAuth 憑證失敗。請先進行身份驗證：{{error}}",
  "tokenRefreshFailed": "重新整理 OAuth 權杖失敗：{{error}}",
  "onboardingTimeout": "引導操作在 60 秒後逾時。請稍後重試。",
  "projectDiscoveryFailed": "無法發現專案 ID。請確保您已使用 'gemini auth' 進行身份驗證。",
  "rateLimitExceeded": "超出速率限制。已達到免費層級限制。",
  "badRequest": "錯誤請求：{{details}}",
  "apiError": "Gemini CLI API 錯誤：{{error}}",
  "completionError": "Gemini CLI 完成錯誤：{{error}}"
}
```

## 验证检查

### 1. 文件存在性检查
- [ ] `packages/types/src/providers/gemini-cli.ts` 存在
- [ ] `src/api/providers/gemini-cli.ts` 存在
- [ ] `webview-ui/src/components/settings/providers/GeminiCli.tsx` 存在

### 2. 代码补全检查
- [ ] `packages/types/src/providers/index.ts` 包含导出
- [ ] `src/api/index.ts` 包含导入和 case 分支
- [ ] `src/api/providers/index.ts` 包含导出
- [ ] `src/shared/checkExistApiConfig.ts` 包含配置
- [ ] `webview-ui/src/utils/validate.ts` 包含 gemini-cli case

### 3. 多语言补全检查
- [ ] 所有语言的 `settings.json` 在末尾包含 `geminiCli` 配置
- [ ] 所有语言的 `common.json` 在末尾包含 `geminiCli` 错误配置
- [ ] 没有破坏现有多语言配置的结构

### 4. 功能验证
- [ ] Gemini CLI 选项在设置中可见
- [ ] 错误信息正确显示
- [ ] 功能正常工作

### 5. 文档文件检查
- [ ] 没有 `.diff.md` 文件被复制到项目中
- [ ] 没有说明文档被复制到项目中
- [ ] 只有必要的代码文件被复制

## 注意事项

1. **严格遵循末尾补全策略**：所有多语言文档都在末尾添加新配置
2. **保持代码完整性**：不插入到中间位置，避免影响现有结构
3. **便于 Git 比对**：新增内容清晰可见，便于版本控制
4. **绝对不删除代码**：即使看起来与 gemini-cli 相关，也不能删除
5. **测试验证**：补全完成后必须进行功能测试
6. **文档文件过滤**：确保 `.diff.md` 等文档文件不会被复制到项目中

---

**重要提醒**：本文档是补全操作的唯一指导文件，必须严格按照文档要求执行，确保代码的完整性和功能的正确性。