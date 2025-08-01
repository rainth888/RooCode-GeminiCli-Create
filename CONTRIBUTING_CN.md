# 贡献指南

感谢您对 Gemini CLI 自动补全工具的关注！我们欢迎所有形式的贡献。

## 🤝 如何贡献

### 1. Fork 项目

1. 访问 [项目主页](https://github.com/rainth888/RooCode-GeminiCli-Create)
2. 点击右上角的 "Fork" 按钮
3. 选择您的 GitHub 账户作为目标

### 2. 克隆您的 Fork

```bash
git clone https://github.com/您的用户名/RooCode-GeminiCli-Create.git
cd RooCode-GeminiCli-Create
```

### 3. 创建功能分支

```bash
git checkout -b feature/AmazingFeature
```

### 4. 进行更改

- 编写代码
- 添加测试
- 更新文档
- 确保代码符合项目规范

### 5. 提交更改

```bash
git add .
git commit -m "Add some AmazingFeature"
```

### 6. 推送到分支

```bash
git push origin feature/AmazingFeature
```

### 7. 创建 Pull Request

1. 访问您的 Fork 页面
2. 点击 "Pull Request" 按钮
3. 选择目标分支（通常是 `main`）
4. 填写标题和描述
5. 提交 Pull Request

## 📋 贡献类型

我们欢迎以下类型的贡献：

### 🐛 Bug 修复

- 修复现有功能中的错误
- 改进错误处理
- 增强稳定性

### ✨ 新功能

- 添加新的补全功能
- 支持新的文件类型
- 增加配置选项

### 📝 文档改进

- 更新 README 文件
- 添加使用示例
- 改进错误信息

### 🎨 代码优化

- 重构现有代码
- 提高性能
- 改进代码可读性

### ⚡ 性能提升

- 优化算法
- 减少内存使用
- 提高执行速度

## 🔧 开发环境设置

### 环境要求

- Python 3.7+
- Git
- 文本编辑器（推荐 VS Code）

### 安装依赖

```bash
# 克隆项目
git clone https://github.com/rainth888/RooCode-GeminiCli-Create.git
cd RooCode-GeminiCli-Create

# 检查 Python 版本
python --version

# 运行测试
python gemini_cli_auto_complement.py
```

## 📝 代码规范

### Python 代码规范

- 遵循 PEP 8 规范
- 使用有意义的变量名
- 添加适当的注释
- 保持函数简洁

### 提交信息规范

使用清晰的提交信息：

```
类型(范围): 简短描述

详细描述（可选）

- 功能点1
- 功能点2
```

类型包括：
- `feat`: 新功能
- `fix`: 修复
- `docs`: 文档
- `style`: 格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建

### 示例

```
feat(completion): 添加对新的文件类型的支持

- 支持 .vue 文件的补全
- 添加相应的测试用例
- 更新文档说明
```

## 🧪 测试

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试
python -m pytest tests/test_completion.py

# 生成覆盖率报告
python -m pytest --cov=gemini_cli_auto_complement tests/
```

### 测试要求

- 所有新功能必须有测试
- 测试覆盖率应保持在 80% 以上
- 测试应该独立且可重复

## 📚 文档

### 文档要求

- 所有新功能必须有文档
- 更新 README 文件
- 添加使用示例
- 更新 API 文档

### 文档格式

- 使用 Markdown 格式
- 保持简洁明了
- 包含代码示例
- 使用中文和英文双语

## 🔍 代码审查

### 审查流程

1. 提交 Pull Request
2. 自动检查（CI/CD）
3. 代码审查
4. 合并到主分支

### 审查标准

- 代码质量
- 功能完整性
- 测试覆盖
- 文档更新
- 性能影响

## 🐛 报告问题

### 问题报告模板

```markdown
## 问题描述

简要描述问题

## 重现步骤

1. 步骤1
2. 步骤2
3. 步骤3

## 预期行为

描述期望的行为

## 实际行为

描述实际的行为

## 环境信息

- 操作系统：
- Python 版本：
- 工具版本：

## 附加信息

任何其他相关信息
```

## 💡 功能建议

### 建议模板

```markdown
## 功能描述

简要描述新功能

## 使用场景

描述使用场景

## 实现建议

提供实现建议

## 优先级

高/中/低
```

## 📞 联系我们

- **项目主页**: [GitHub](https://github.com/rainth888/RooCode-GeminiCli-Create)
- **问题反馈**: [Issues](https://github.com/rainth888/RooCode-GeminiCli-Create/issues)
- **讨论区**: [Discussions](https://github.com/rainth888/RooCode-GeminiCli-Create/discussions)

## 🙏 致谢

感谢所有为项目做出贡献的开发者！

---

## Language Selection

- 🇨🇳 **Chinese**: `CONTRIBUTING_CN.md` (current file)
- 🇺🇸 **English**: `CONTRIBUTING.md`

For English users, please refer to `CONTRIBUTING.md` for English documentation. 