#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini CLI 自动补全配置文件
包含各种语言的翻译配置
"""

# Gemini CLI Settings 配置
GEMINI_CLI_SETTINGS_CONFIG = {
    "en": {
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
    },
    "zh-CN": {
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
    },
    "zh-TW": {
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
}

# Gemini CLI Errors 配置
GEMINI_CLI_ERRORS_CONFIG = {
    "en": {
        "oauthLoadFailed": "Failed to load OAuth credentials. Please authenticate first: {{error}}",
        "tokenRefreshFailed": "Failed to refresh OAuth token: {{error}}",
        "onboardingTimeout": "Onboarding operation timed out after 60 seconds. Please try again later.",
        "projectDiscoveryFailed": "Could not discover project ID. Make sure you're authenticated with 'gemini auth'.",
        "rateLimitExceeded": "Rate limit exceeded. Free tier limits have been reached.",
        "badRequest": "Bad request: {{details}}",
        "apiError": "Gemini CLI API error: {{error}}",
        "completionError": "Gemini CLI completion error: {{error}}"
    },
    "zh-CN": {
        "oauthLoadFailed": "加载 OAuth 凭据失败。请先进行身份验证：{{error}}",
        "tokenRefreshFailed": "刷新 OAuth 令牌失败：{{error}}",
        "onboardingTimeout": "引导操作在 60 秒后超时。请稍后重试。",
        "projectDiscoveryFailed": "无法发现项目 ID。请确保您已使用 'gemini auth' 进行身份验证。",
        "rateLimitExceeded": "超出速率限制。已达到免费层级限制。",
        "badRequest": "错误请求：{{details}}",
        "apiError": "Gemini CLI API 错误：{{error}}",
        "completionError": "Gemini CLI 完成错误：{{error}}"
    },
    "zh-TW": {
        "oauthLoadFailed": "載入 OAuth 憑證失敗。請先進行身份驗證：{{error}}",
        "tokenRefreshFailed": "重新整理 OAuth 權杖失敗：{{error}}",
        "onboardingTimeout": "引導操作在 60 秒後逾時。請稍後重試。",
        "projectDiscoveryFailed": "無法發現專案 ID。請確保您已使用 'gemini auth' 進行身份驗證。",
        "rateLimitExceeded": "超出速率限制。已達到免費層級限制。",
        "badRequest": "錯誤請求：{{details}}",
        "apiError": "Gemini CLI API 錯誤：{{error}}",
        "completionError": "Gemini CLI 完成錯誤：{{error}}"
    }
}

# 直接复制的文件列表
DIRECT_COPY_FILES = [
    "packages/types/src/providers/gemini-cli.ts",
    "src/api/providers/__tests__/gemini-cli.spec.ts",
    "src/api/providers/gemini-cli.ts",
    "webview-ui/src/components/settings/providers/GeminiCli.tsx",
    "webview-ui/src/components/settings/providers/__tests__/GeminiCli.spec.tsx"
]

# 需要补全的文件列表
COMPLEMENT_FILES = [
    "packages/types/src/providers/index.ts",
    "src/api/index.ts",
    "src/api/providers/index.ts",
    "src/shared/checkExistApiConfig.ts"
]

# 严格操作规范
STRICT_RULES = {
    "NO_DELETE": "绝对不允许删除任何现有代码",
    "ONLY_ADD": "只能进行新增操作，不能进行删除或替换操作",
    "PRESERVE_ALL": "保留所有现有代码，即使看起来与 gemini-cli 相关"
}