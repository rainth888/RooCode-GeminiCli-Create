# Gemini CLI OAuth 设置指南

## 概述

Gemini CLI 集成需要 Google OAuth 凭据来访问 Google Cloud Code Assist API。本指南详细说明如何设置必要的凭据。

## 前置要求

1. Google Cloud 账户
2. 访问 Google Cloud Console 的权限
3. 基本的 OAuth 2.0 知识

## 逐步设置

### 1. 创建 Google Cloud 项目

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建新项目或选择现有项目
3. 记录您的项目 ID

### 2. 启用必要的 API

1. 在 Google Cloud Console 中，转到"API 和服务" > "库"
2. 搜索并启用以下 API：
   - **Google Cloud Code Assist API**
   - **Google OAuth2 API**（通常默认已启用）

### 3. 创建 OAuth 2.0 凭据

1. 转到"API 和服务" > "凭据"
2. 点击"创建凭据" > "OAuth 2.0 客户端 ID"
3. 如果提示，首先配置 OAuth 同意屏幕：
   - 选择"外部"用户类型
   - 填写必需信息（应用名称、用户支持电子邮件、开发者联系信息）
   - 添加范围：`https://www.googleapis.com/auth/cloud-platform`
   - 如需要，添加测试用户

4. 创建 OAuth 2.0 客户端 ID：
   - 应用类型："桌面应用程序"
   - 名称："Gemini CLI 集成"
   - 点击"创建"

5. 记录**客户端 ID**和**客户端密钥**

### 4. 配置应用程序

1. 打开文件：`z-geminicli-install/src/api/providers/gemini-cli.ts`
2. 替换占位符值：
   ```typescript
   const OAUTH_CLIENT_ID = "您的实际客户端ID"
   const OAUTH_CLIENT_SECRET = "您的实际客户端密钥"
   ```

### 5. 设置 OAuth 凭据文件

应用程序期望 OAuth 凭据存储在 JSON 文件中。默认情况下，它查找：
- `~/.gemini/oauth_creds.json`（Linux/macOS）
- `%USERPROFILE%\.gemini\oauth_creds.json`（Windows）

您也可以使用 `geminiCliOAuthPath` 选项指定自定义路径。

## 安全注意事项

⚠️ **重要安全考虑**：

1. **切勿将真实凭据提交到版本控制**
   - 当前代码使用占位符值
   - 真实凭据应保持私密
   - 使用环境变量或安全的凭据存储

2. **使用 .gitignore**
   - 项目包含 `.gitignore` 文件来排除敏感文件
   - 自动忽略 `oauth_creds.json`、`*.key`、`*.pem` 等文件

3. **定期轮换凭据**
   - 定期更改您的 OAuth 凭据
   - 监控任何未授权使用

## 故障排除

### 常见问题

1. **"无效客户端"错误**
   - 验证您的客户端 ID 和客户端密钥是否正确
   - 确保 OAuth 同意屏幕配置正确

2. **"重定向 URI 不匹配"错误**
   - 应用程序使用 `http://localhost:45289` 作为重定向 URI
   - 确保这已添加到您的 OAuth 客户端的授权重定向 URI 中

3. **"API 未启用"错误**
   - 确保在您的项目中启用了 Google Cloud Code Assist API
   - 检查您是否有必要的权限

### 获取帮助

如果遇到问题：
1. 检查 Google Cloud Console 中的错误消息
2. 验证您的项目是否启用了计费（某些 API 需要）
3. 确保您的账户有必要的权限

## 配置示例

您的 OAuth 凭据文件应如下所示：

```json
{
  "access_token": "您的访问令牌",
  "refresh_token": "您的刷新令牌",
  "token_type": "Bearer",
  "expiry_date": 1234567890000
}
```

**注意**：当您首次进行身份验证时，此文件会自动生成。您无需手动创建它。

## 其他资源

- [Google Cloud Console](https://console.cloud.google.com/)
- [OAuth 2.0 文档](https://developers.google.com/identity/protocols/oauth2)
- [Google Cloud Code Assist API 文档](https://cloud.google.com/code-assist)

---

## 语言选择 / Language Selection

- 🇨🇳 **中文文档**: `oauth-setup.md` (当前文件)
- 🇺🇸 **English Documentation**: `oauth-setup-en.md`

For English users, please refer to `oauth-setup-en.md` for complete documentation.

## Overview

The Gemini CLI integration requires Google OAuth credentials to authenticate with the Google Cloud Code Assist API. This guide explains how to set up the necessary credentials.

## Prerequisites

1. A Google Cloud account
2. Access to Google Cloud Console
3. Basic understanding of OAuth 2.0

## Step-by-Step Setup

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Note down your Project ID

### 2. Enable Required APIs

1. In the Google Cloud Console, go to "APIs & Services" > "Library"
2. Search for and enable the following APIs:
   - **Google Cloud Code Assist API**
   - **Google OAuth2 API** (usually enabled by default)

### 3. Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. If prompted, configure the OAuth consent screen first:
   - Choose "External" user type
   - Fill in the required information (App name, User support email, Developer contact information)
   - Add scopes: `https://www.googleapis.com/auth/cloud-platform`
   - Add test users if needed

4. Create the OAuth 2.0 Client ID:
   - Application type: "Desktop application"
   - Name: "Gemini CLI Integration"
   - Click "Create"

5. Note down the **Client ID** and **Client Secret**

### 4. Configure the Application

1. Open the file: `z-geminicli-install/src/api/providers/gemini-cli.ts`
2. Replace the placeholder values:
   ```typescript
   const OAUTH_CLIENT_ID = "YOUR_ACTUAL_CLIENT_ID"
   const OAUTH_CLIENT_SECRET = "YOUR_ACTUAL_CLIENT_SECRET"
   ```

### 5. Set Up OAuth Credentials File

The application expects OAuth credentials to be stored in a JSON file. By default, it looks for:
- `~/.gemini/oauth_creds.json` (Linux/macOS)
- `%USERPROFILE%\.gemini\oauth_creds.json` (Windows)

You can also specify a custom path using the `geminiCliOAuthPath` option.

## Security Notes

⚠️ **Important Security Considerations:**

1. **Never commit real credentials to version control**
   - The current code uses placeholder values
   - Real credentials should be kept private
   - Use environment variables or secure credential storage

2. **Use .gitignore**
   - The project includes a `.gitignore` file that excludes sensitive files
   - Files like `oauth_creds.json`, `*.key`, `*.pem` are automatically ignored

3. **Rotate credentials regularly**
   - Change your OAuth credentials periodically
   - Monitor for any unauthorized usage

## Troubleshooting

### Common Issues

1. **"Invalid client" error**
   - Verify your Client ID and Client Secret are correct
   - Ensure the OAuth consent screen is properly configured

2. **"Redirect URI mismatch" error**
   - The application uses `http://localhost:45289` as the redirect URI
   - Make sure this is added to your OAuth client's authorized redirect URIs

3. **"API not enabled" error**
   - Ensure the Google Cloud Code Assist API is enabled in your project
   - Check that you have the necessary permissions

### Getting Help

If you encounter issues:
1. Check the Google Cloud Console for error messages
2. Verify your project has billing enabled (required for some APIs)
3. Ensure your account has the necessary permissions

## Example Configuration

Here's what your OAuth credentials file should look like:

```json
{
  "access_token": "your_access_token_here",
  "refresh_token": "your_refresh_token_here",
  "token_type": "Bearer",
  "expiry_date": 1234567890000
}
```

**Note**: This file is automatically generated when you first authenticate. You don't need to create it manually.

## Additional Resources

- [Google Cloud Console](https://console.cloud.google.com/)
- [OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)
- [Google Cloud Code Assist API Documentation](https://cloud.google.com/code-assist) 