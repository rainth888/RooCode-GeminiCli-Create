# Contributing Guide

Thank you for your interest in the Gemini CLI Auto Complement Tool! We welcome all forms of contributions.

## 🤝 How to Contribute

### 1. Fork the Project

1. Visit the [project homepage](https://github.com/rainth888/RooCode-GeminiCli-Create)
2. Click the "Fork" button in the top right corner
3. Select your GitHub account as the target

### 2. Clone Your Fork

```bash
git clone https://github.com/your-username/RooCode-GeminiCli-Create.git
cd RooCode-GeminiCli-Create
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/AmazingFeature
```

### 4. Make Changes

- Write code
- Add tests
- Update documentation
- Ensure code follows project standards

### 5. Commit Changes

```bash
git add .
git commit -m "Add some AmazingFeature"
```

### 6. Push to Branch

```bash
git push origin feature/AmazingFeature
```

### 7. Create a Pull Request

1. Visit your fork page
2. Click the "Pull Request" button
3. Select the target branch (usually `main`)
4. Fill in the title and description
5. Submit the Pull Request

## 📋 Types of Contributions

We welcome the following types of contributions:

### 🐛 Bug Fixes

- Fix errors in existing functionality
- Improve error handling
- Enhance stability

### ✨ New Features

- Add new completion features
- Support new file types
- Add configuration options

### 📝 Documentation Improvements

- Update README files
- Add usage examples
- Improve error messages

### 🎨 Code Optimization

- Refactor existing code
- Improve performance
- Enhance code readability

### ⚡ Performance Improvements

- Optimize algorithms
- Reduce memory usage
- Improve execution speed

## 🔧 Development Environment Setup

### Requirements

- Python 3.7+
- Git
- Text editor (VS Code recommended)

### Install Dependencies

```bash
# Clone the project
git clone https://github.com/rainth888/RooCode-GeminiCli-Create.git
cd RooCode-GeminiCli-Create

# Check Python version
python --version

# Run tests
python gemini_cli_auto_complement.py
```

## 📝 Code Standards

### Python Code Standards

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add appropriate comments
- Keep functions concise

### Commit Message Standards

Use clear commit messages:

```
type(scope): short description

detailed description (optional)

- feature point 1
- feature point 2
```

Types include:
- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation
- `style`: formatting
- `refactor`: refactoring
- `test`: testing
- `chore`: build

### Example

```
feat(completion): add support for new file types

- Support .vue file completion
- Add corresponding test cases
- Update documentation
```

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific tests
python -m pytest tests/test_completion.py

# Generate coverage report
python -m pytest --cov=gemini_cli_auto_complement tests/
```

### Testing Requirements

- All new features must have tests
- Test coverage should be maintained above 80%
- Tests should be independent and repeatable

## 📚 Documentation

### Documentation Requirements

- All new features must have documentation
- Update README files
- Add usage examples
- Update API documentation

### Documentation Format

- Use Markdown format
- Keep it concise and clear
- Include code examples
- Use both Chinese and English

## 🔍 Code Review

### Review Process

1. Submit Pull Request
2. Automatic checks (CI/CD)
3. Code review
4. Merge to main branch

### Review Criteria

- Code quality
- Feature completeness
- Test coverage
- Documentation updates
- Performance impact

## 🐛 Reporting Issues

### Issue Report Template

```markdown
## Issue Description

Brief description of the issue

## Steps to Reproduce

1. Step 1
2. Step 2
3. Step 3

## Expected Behavior

Describe expected behavior

## Actual Behavior

Describe actual behavior

## Environment Information

- Operating System:
- Python Version:
- Tool Version:

## Additional Information

Any other relevant information
```

## 💡 Feature Suggestions

### Suggestion Template

```markdown
## Feature Description

Brief description of the new feature

## Use Cases

Describe use cases

## Implementation Suggestions

Provide implementation suggestions

## Priority

High/Medium/Low
```

## 📞 Contact Us

- **Project Homepage**: [GitHub](https://github.com/rainth888/RooCode-GeminiCli-Create)
- **Issue Reports**: [Issues](https://github.com/rainth888/RooCode-GeminiCli-Create/issues)
- **Discussions**: [Discussions](https://github.com/rainth888/RooCode-GeminiCli-Create/discussions)

## 🙏 Acknowledgments

Thank you to all developers who have contributed to the project!

---

## Language Selection

- 🇨🇳 **Chinese**: `CONTRIBUTING_CN.md`
- 🇺🇸 **English**: `CONTRIBUTING.md` (current file)

For Chinese users, please refer to `CONTRIBUTING_CN.md` for Chinese documentation. 