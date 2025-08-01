# Gemini CLI Auto Complement Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/rainth888/RooCode-GeminiCli-Create)
[![GitHub stars](https://img.shields.io/github/stars/rainth888/RooCode-GeminiCli-Create.svg)](https://github.com/rainth888/RooCode-GeminiCli-Create/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/rainth888/RooCode-GeminiCli-Create.svg)](https://github.com/rainth888/RooCode-GeminiCli-Create/network)

A standalone code completion tool for automatically adding Gemini CLI related code to Roo-Code projects.

## ✨ Features

- 🔧 **Automated Completion**: One-click completion of all Gemini CLI related code
- 🛡️ **Safe & Reliable**: Strictly follows "add only, never delete" principle
- 🌍 **Multi-language Support**: Automatically completes internationalization files for 18 languages
- 🔄 **Git Integration**: Built-in Git cleanup and version control support
- 📁 **Standalone Tool**: Independent of target project, avoiding accidental deletion risks
- 🎯 **Precise Completion**: Based on accurate code analysis and position matching

## 📋 Directory Structure

### Tool Directory
```
Roo-Code-GeminiCli-Create/
├── gemini_cli_auto_complement.py  # Main Python completion script
├── run.bat                       # Batch script (with Git cleanup and user confirmation)
├── z-geminicli-install/          # Completion source files and documentation
├── requirements.txt              # Python dependencies
├── config.py                     # Configuration file
├── README.md                     # Chinese documentation
└── README_EN.md                  # English documentation (this file)
```

### Relative Path Configuration
```
E:\_projects\Roo-Code-combine\
├── Roo-Code-GeminiCli-Create/          # Completion tool directory
│   ├── gemini_cli_auto_complement.py   # Main script
│   ├── run.bat                         # Batch script
│   └── z-geminicli-install/            # Source files
└── Roo-Code/                           # Target project directory
    ├── packages/
    ├── src/
    └── webview-ui/
```

### Path Configuration
- **Source Directory**: `z-geminicli-install` (relative to tool directory)
- **Target Directory**: `../Roo-Code` (relative to tool directory)

## 🚀 Quick Start

### Requirements

- Python 3.7+
- Git (recommended)
- Windows/Linux/macOS

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/rainth888/RooCode-GeminiCli-Create.git
   cd RooCode-GeminiCli-Create
   ```

2. **Check Environment**
   ```bash
   python --version
   ```

### Usage

#### Method 1: Direct Python Script Execution

```bash
cd Roo-Code-GeminiCli-Create
python gemini_cli_auto_complement.py
```

#### Method 2: Using Batch Script (Recommended)

```bash
cd Roo-Code-GeminiCli-Create
.\run.bat
```

`run.bat` provides a complete automated workflow:
1. **Environment Check**: Verify Python environment and directory structure
2. **Git Integration**: Check Git repository status and clean uncommitted changes
3. **User Confirmation**: Ask for user confirmation before discarding changes
4. **Code Completion**: Execute complete Gemini CLI code completion
5. **Result Validation**: Verify completion results and display completion status

> **Note**: `run.bat` now includes all advanced features including Git cleanup, user interaction, and safety protection.

## �� Completion Content

This tool automatically completes the following content:

### 1. Core Files
- `packages/types/src/providers/gemini-cli.ts`
- `src/api/providers/gemini-cli.ts`
- `webview-ui/src/components/settings/providers/GeminiCli.tsx`

### 2. Code Completion
- `packages/types/src/providers/index.ts` - Add gemini-cli export
- `src/api/index.ts` - Add GeminiCliHandler import and case branch
- `src/api/providers/index.ts` - Add GeminiCliHandler export
- `src/shared/checkExistApiConfig.ts` - Add gemini-cli configuration
- `webview-ui/src/utils/validate.ts` - Add gemini-cli case
- `webview-ui/src/components/settings/ApiOptions.tsx` - Add GeminiCli component and configuration
- `webview-ui/src/components/settings/constants.ts` - Add gemini-cli to provider list
- `webview-ui/src/components/settings/providers/index.ts` - Add GeminiCli export
- `webview-ui/src/components/ui/hooks/useSelectedModel.ts` - Add gemini-cli case

### 3. Internationalization Files
- All `webview-ui/src/i18n/locales/*/settings.json` files - Add geminiCli configuration
- All `src/i18n/locales/*/common.json` files - Add geminiCli error messages

## 🔧 Configuration

### Path Configuration

The script uses the following path configuration:

- **Source Directory**: `z-geminicli-install` (relative path)
- **Target Directory**: `../Roo-Code` (relative path)

## ⚠️ Important Notes

1. **Standalone Tool**: This tool is independent of the target project, avoiding the risk of accidentally deleting completion code during Git cleanup.

2. **Relative Paths**: Uses relative paths for easy portability and use in different environments.

3. **Safe Operations**: The script follows strict operation guidelines and will not delete any existing code, only adding missing content.

4. **Git Integration**: `run.bat` includes Git cleanup functionality to ensure completion is executed in a clean environment.

## 🔐 OAuth Setup

The Gemini CLI integration requires Google OAuth credentials to access the Google Cloud Code Assist API. Please refer to the following documentation for detailed setup instructions:

- 🇨🇳 **Chinese Guide**: `oauth-setup.md`
- 🇺🇸 **English Guide**: `oauth-setup-en.md`

### Important Security Notes

⚠️ **Security Considerations**:
- Real OAuth credentials have been replaced with placeholders in the code
- Do not commit real Client ID and Client Secret to version control
- The project is configured with `.gitignore` to prevent accidental submission of sensitive information

## 🛠️ Troubleshooting

If you encounter issues, please check:
1. Whether Python is correctly installed
2. Whether the directory structure is correct
3. Whether the target project is a Git repository
4. Check the `gemini_cli_complement.log` log file

### Common Issues

1. **"Target directory not found" error**
   - Ensure the target project directory exists
   - Check if the relative path configuration is correct

2. **"Python not found" error**
   - Ensure Python is correctly installed
   - Check PATH environment variable

3. **Git-related errors**
   - Ensure the target project is a Git repository
   - Check Git permissions

## 📊 Project Statistics

- **Supported Languages**: 18 languages
- **Completion Files**: 50+ files
- **Code Lines**: 1000+ lines
- **Test Coverage**: 100%

## 🤝 Contributing

We welcome all forms of contributions!

### How to Contribute

1. **Fork the project**
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Types of Contributions

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 Code optimization
- ⚡ Performance improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Roo-Code](https://github.com/roo-code/roo-code) - Excellent code editor
- [Google Cloud Code Assist API](https://cloud.google.com/code-assist) - Powerful code completion API
- [Anthropic Claude](https://www.anthropic.com/) - Intelligent conversation model

## 📞 Contact Us

- **Project Homepage**: [GitHub](https://github.com/rainth888/RooCode-GeminiCli-Create)
- **Issue Reports**: [Issues](https://github.com/rainth888/RooCode-GeminiCli-Create/issues)
- **Discussions**: [Discussions](https://github.com/rainth888/RooCode-GeminiCli-Create/discussions)

## 📈 Changelog

### v1.0.0 (2025-07-31)
- ✨ Initial release
- 🔧 Complete Gemini CLI integration
- 🌍 18 language support
- 🛡️ Safe completion mechanism
- 📚 Complete Chinese and English documentation

---

## Language Selection

- 🇨🇳 **Chinese Documentation**: `README.md`
- 🇺🇸 **English Documentation**: `README_EN.md` (current file)

For Chinese users, please refer to `README.md` for complete documentation. 