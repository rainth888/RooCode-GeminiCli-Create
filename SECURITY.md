# Security Policy

## Supported Versions

We actively maintain security updates for the following versions:

| Version | Supported |
| ------- | --------- |
| 1.0.x   | ✅ Yes    |

## Reporting a Vulnerability

We take security issues very seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Disclose Publicly

**Important**: Please do not report security vulnerabilities in public Issues. This could put other users at risk.

### 2. Private Reporting

Please report security vulnerabilities privately through:

- **Email**: rainth888@gmail.com
- **Subject**: `[SECURITY] Security Vulnerability Report`

### 3. Report Content

Please include the following information in your report:

```
Subject: [SECURITY] Security Vulnerability Report

## Vulnerability Description
Brief description of the discovered vulnerability

## Impact Scope
Description of potential impact of the vulnerability

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Environment Information
- Operating System:
- Python Version:
- Tool Version:

## Suggested Fix
If you have suggestions for fixes, please provide them

## Contact Information
Your contact information (optional)
```

### 4. Response Time

We commit to responding to security reports within:
- **24 hours**: Acknowledge receipt of the report
- **72 hours**: Provide initial assessment
- **7 days**: Provide fix plan or solution

## Security Best Practices

### 1. Credential Management

- **Never** commit real OAuth credentials to version control
- Use environment variables or secure credential storage
- Rotate credentials regularly

### 2. File Permissions

- Ensure sensitive files have appropriate permission settings
- Use `.gitignore` to exclude sensitive files

### 3. Dependency Management

- Regularly update dependency packages
- Monitor known security vulnerabilities
- Use trusted package sources

### 4. Code Review

- All code changes require review
- Pay special attention to code involving file system operations
- Validate input data legitimacy

## Known Security Issues

### Fixed

Currently no known security issues.

### Pending

Currently no pending security issues.

## Security Updates

### v1.0.0 (2025-07-31)

- ✅ Removed hardcoded OAuth credentials
- ✅ Added `.gitignore` to protect sensitive files
- ✅ Implemented secure credential management mechanism
- ✅ Added security documentation and best practices guide

## Security Contact

- **Security Email**: rainth888@gmail.com
- **Project Homepage**: [GitHub](https://github.com/rainth888/RooCode-GeminiCli-Create)
- **Issue Reports**: [Issues](https://github.com/rainth888/RooCode-GeminiCli-Create/issues)

## Acknowledgments

Thank you to all researchers and users who responsibly report security issues!

---

## Language Selection

- 🇨🇳 **Chinese**: `SECURITY_CN.md`
- 🇺🇸 **English**: `SECURITY.md` (current file)

For Chinese users, please refer to `SECURITY_CN.md` for Chinese documentation. 