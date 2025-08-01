# Gemini CLI Auto Complement Tool

这是一个独立的代码补全工具，用于将 Gemini CLI 相关代码自动补全到 Roo-Code 项目中。

## 目录结构

```
Roo-Code-GeminiCli-Create/
├── gemini_cli_auto_complement.py  # 主要的 Python 补全脚本
├── run.bat                       # 批处理脚本（包含 Git 清理和用户确认）
├── z-geminicli-install/          # 补全源文件和指导文档
├── requirements.txt              # Python 依赖
├── config.py                     # 配置文件
├── README.md                     # 中文文档（本文件）
└── README_EN.md                  # 英文文档
```

## 使用方法

### 方法 1：直接运行 Python 脚本

```bash
cd Roo-Code-GeminiCli-Create
python gemini_cli_auto_complement.py
```

### 方法 2：使用批处理脚本（推荐）

```bash
cd Roo-Code-GeminiCli-Create
.\run.bat
```

`run.bat` 提供了完整的自动化流程：
1. **环境检查**：验证 Python 环境和目录结构
2. **Git 集成**：检查 Git 仓库状态，清理未提交的更改
3. **用户确认**：在丢弃更改前询问用户确认
4. **代码补全**：执行完整的 Gemini CLI 代码补全
5. **结果验证**：验证补全结果并显示完成状态

> **注意**：`run.bat` 现在包含了所有高级功能，包括 Git 清理、用户交互和安全保护。

## 补全内容

该工具会自动补全以下内容：

### 1. 核心文件
- `packages/types/src/providers/gemini-cli.ts`
- `src/api/providers/gemini-cli.ts`
- `webview-ui/src/components/settings/providers/GeminiCli.tsx`

### 2. 代码补全
- `packages/types/src/providers/index.ts` - 添加 gemini-cli 导出
- `src/api/index.ts` - 添加 GeminiCliHandler 导入和 case 分支
- `src/api/providers/index.ts` - 添加 GeminiCliHandler 导出
- `src/shared/checkExistApiConfig.ts` - 添加 gemini-cli 配置
- `webview-ui/src/utils/validate.ts` - 添加 gemini-cli case
- `webview-ui/src/components/settings/ApiOptions.tsx` - 添加 GeminiCli 组件和配置
- `webview-ui/src/components/settings/constants.ts` - 添加 gemini-cli 到提供商列表
- `webview-ui/src/components/settings/providers/index.ts` - 添加 GeminiCli 导出
- `webview-ui/src/components/ui/hooks/useSelectedModel.ts` - 添加 gemini-cli case

### 3. 国际化文件
- 所有 `webview-ui/src/i18n/locales/*/settings.json` 文件 - 添加 geminiCli 配置
- 所有 `src/i18n/locales/*/common.json` 文件 - 添加 geminiCli 错误信息

## 目录结构说明

### 相对路径配置
```
E:\_projects\Roo-Code-combine\
├── Roo-Code-GeminiCli-Create/          # 补全工具目录
│   ├── gemini_cli_auto_complement.py   # 主脚本
│   ├── run.bat                         # 批处理脚本
│   └── z-geminicli-install/            # 补全源文件
└── Roo-Code/                           # 目标项目目录
    ├── packages/
    ├── src/
    └── webview-ui/
```

### 路径配置
- **源目录**: `z-geminicli-install` (相对于补全工具目录)
- **目标目录**: `../Roo-Code` (相对于补全工具目录)

## 注意事项

1. **独立工具**：此工具独立于目标项目，避免了 Git 清理时意外删除补全代码的风险。

2. **相对路径**：使用相对路径，便于在不同环境中使用。

3. **安全操作**：脚本遵循严格的操作规范，不会删除任何现有代码，只会添加缺失的内容。

4. **Git 集成**：`run.bat` 包含 Git 清理功能，确保在干净的环境中执行补全。

## 故障排除

如果遇到问题，请检查：
1. Python 是否正确安装
2. 目录结构是否正确
3. 目标项目是否为 Git 仓库
4. 查看 `gemini_cli_complement.log` 日志文件

## OAuth 设置

Gemini CLI 集成需要 Google OAuth 凭据来访问 Google Cloud Code Assist API。请参考以下文档了解详细的设置步骤：

- 🇨🇳 **中文说明**: `oauth-setup.md`
- 🇺🇸 **English Guide**: `oauth-setup-en.md`

### 重要安全提示

⚠️ **安全注意事项**：
- 代码中已使用占位符替换了真实的 OAuth 凭据
- 请勿将真实的 Client ID 和 Client Secret 提交到版本控制系统
- 项目已配置 `.gitignore` 文件来防止意外提交敏感信息

## 版本信息

- 工具版本：1.0
- 支持的目标项目：Roo-Code
- 最后更新：2025-07-31

---

## 语言选择 / Language Selection

- 🇨🇳 **中文文档**: `README.md` (当前文件)
- 🇺🇸 **English Documentation**: `README_EN.md`

For English users, please refer to `README_EN.md` for complete documentation.