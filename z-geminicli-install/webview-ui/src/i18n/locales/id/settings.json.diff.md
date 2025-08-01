# webview-ui/src/i18n/locales/id/settings.json 补全说明

## 目标文件路径

`webview-ui/src/i18n/locales/id/settings.json`

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
       "pathLabel": "Jalur Kode Claude",
       "description": "Jalur opsional ke Claude Code CLI Anda. Defaultnya adalah 'claude' jika tidak diatur.",
       "placeholder": "Default: claude",
       "maxTokensLabel": "Token Output Maks",
       "maxTokensDescription": "Jumlah maksimum token output untuk respons Claude Code. Default adalah 8000."
   },
   "geminiCli": {
       // 在这里插入 geminiCli 配置
   },
   "browser": {
       // browser 配置开始
   ```

### 方法二：自动化补全（精确匹配）

如果使用自动化工具，请使用以下**精确的上下文匹配**：

#### 旧字符串（old_string）- 必须完全匹配
```json
		"setReasoningLevel": "Aktifkan Upaya Reasoning",
		"claudeCode": {
			"pathLabel": "Jalur Kode Claude",
			"description": "Jalur opsional ke Claude Code CLI Anda. Defaultnya adalah 'claude' jika tidak diatur.",
			"placeholder": "Default: claude",
			"maxTokensLabel": "Token Output Maks",
			"maxTokensDescription": "Jumlah maksimum token output untuk respons Claude Code. Default adalah 8000."
		}
	},
	"browser": {
```

#### 新字符串（new_string）- 包含 geminiCli 配置
```json
		"setReasoningLevel": "Aktifkan Upaya Reasoning",
		"claudeCode": {
			"pathLabel": "Jalur Kode Claude",
			"description": "Jalur opsional ke Claude Code CLI Anda. Defaultnya adalah 'claude' jika tidak diatur.",
			"placeholder": "Default: claude",
			"maxTokensLabel": "Token Output Maks",
			"maxTokensDescription": "Jumlah maksimum token output untuk respons Claude Code. Default adalah 8000."
		},
		"geminiCli": {
			"description": "Provider ini menggunakan autentikasi OAuth dari alat Gemini CLI dan tidak memerlukan kunci API.",
			"oauthPath": "Jalur Kredensial OAuth (opsional)",
			"oauthPathDescription": "Jalur ke file kredensial OAuth. Biarkan kosong untuk menggunakan lokasi default (~/.gemini/oauth_creds.json).",
			"instructions": "Jika Anda belum mengautentikasi, silakan jalankan",
			"instructionsContinued": "di terminal Anda terlebih dahulu.",
			"setupLink": "Instruksi Setup Gemini CLI",
			"requirementsTitle": "Persyaratan Penting",
			"requirement1": "Pertama, Anda perlu menginstal alat Gemini CLI",
			"requirement2": "Kemudian, jalankan gemini di terminal Anda dan pastikan Anda Masuk dengan Google",
			"requirement3": "Hanya bekerja dengan akun Google pribadi (bukan akun Google Workspace)",
			"requirement4": "Tidak menggunakan kunci API - autentikasi ditangani melalui OAuth",
			"requirement5": "Memerlukan alat Gemini CLI untuk diinstal dan diautentikasi terlebih dahulu",
			"freeAccess": "Akses tier gratis melalui autentikasi OAuth"
		}
	},
	"browser": {
```

### 方法三：备用匹配策略

如果上述匹配失败，尝试使用更小的上下文：

#### 备用旧字符串
```json
		"claudeCode": {
			"pathLabel": "Jalur Kode Claude",
			"description": "Jalur opsional ke Claude Code CLI Anda. Defaultnya adalah 'claude' jika tidak diatur.",
			"placeholder": "Default: claude",
			"maxTokensLabel": "Token Output Maks",
			"maxTokensDescription": "Jumlah maksimum token output untuk respons Claude Code. Default adalah 8000."
		}
	},
	"browser": {
```

#### 备用新字符串
```json
		"claudeCode": {
			"pathLabel": "Jalur Kode Claude",
			"description": "Jalur opsional ke Claude Code CLI Anda. Defaultnya adalah 'claude' jika tidak diatur.",
			"placeholder": "Default: claude",
			"maxTokensLabel": "Token Output Maks",
			"maxTokensDescription": "Jumlah maksimum token output untuk respons Claude Code. Default adalah 8000."
		},
		"geminiCli": {
			"description": "Provider ini menggunakan autentikasi OAuth dari alat Gemini CLI dan tidak memerlukan kunci API.",
			"oauthPath": "Jalur Kredensial OAuth (opsional)",
			"oauthPathDescription": "Jalur ke file kredensial OAuth. Biarkan kosong untuk menggunakan lokasi default (~/.gemini/oauth_creds.json).",
			"instructions": "Jika Anda belum mengautentikasi, silakan jalankan",
			"instructionsContinued": "di terminal Anda terlebih dahulu.",
			"setupLink": "Instruksi Setup Gemini CLI",
			"requirementsTitle": "Persyaratan Penting",
			"requirement1": "Pertama, Anda perlu menginstal alat Gemini CLI",
			"requirement2": "Kemudian, jalankan gemini di terminal Anda dan pastikan Anda Masuk dengan Google",
			"requirement3": "Hanya bekerja dengan akun Google pribadi (bukan akun Google Workspace)",
			"requirement4": "Tidak menggunakan kunci API - autentikasi ditangani melalui OAuth",
			"requirement5": "Memerlukan alat Gemini CLI untuk diinstal dan diautentikasi terlebih dahulu",
			"freeAccess": "Akses tier gratis melalui autentikasi OAuth"
		}
	},
	"browser": {
```

## 补全内容

```json
"geminiCli": {
    "description": "Provider ini menggunakan autentikasi OAuth dari alat Gemini CLI dan tidak memerlukan kunci API.",
    "oauthPath": "Jalur Kredensial OAuth (opsional)",
    "oauthPathDescription": "Jalur ke file kredensial OAuth. Biarkan kosong untuk menggunakan lokasi default (~/.gemini/oauth_creds.json).",
    "instructions": "Jika Anda belum mengautentikasi, silakan jalankan",
    "instructionsContinued": "di terminal Anda terlebih dahulu.",
    "setupLink": "Instruksi Setup Gemini CLI",
    "requirementsTitle": "Persyaratan Penting",
    "requirement1": "Pertama, Anda perlu menginstal alat Gemini CLI",
    "requirement2": "Kemudian, jalankan gemini di terminal Anda dan pastikan Anda Masuk dengan Google",
    "requirement3": "Hanya bekerja dengan akun Google pribadi (bukan akun Google Workspace)",
    "requirement4": "Tidak menggunakan kunci API - autentikasi ditangani melalui OAuth",
    "requirement5": "Memerlukan alat Gemini CLI untuk diinstal dan diautentikasi terlebih dahulu",
    "freeAccess": "Akses tier gratis melalui autentikasi OAuth"
}
```

## 操作说明

1. **检查现有内容**：确保 `geminiCli` 配置尚未存在
2. **精确定位**：在 `claudeCode` 配置结束后，`browser` 部分开始前插入
3. **格式验证**：确保 JSON 格式正确，包括逗号分隔
4. **保持一致性**：保持与现有代码相同的缩进风格

## 错误处理

### 如果遇到 `Failed to edit, could not find the string to replace` 错误：

1. **重新读取文件**：获取最新的文件内容
2. **检查格式差异**：确认空格、换行符和标点符号完全匹配
3. **尝试备用匹配策略**：使用更小的上下文范围
4. **手动验证**：手动检查目标位置是否存在
5. **使用手动方法**：如果自动替换失败，使用手动编辑方法

### 如果遇到 `A potential loop was detected` 警告：

1. **立即停止自动操作**：避免无限循环
2. **切换到手动方法**：使用手动补全方法
3. **检查文件状态**：确认文件是否已被修改
4. **重新开始**：从手动补全开始

## 自动化工具使用建议

### 推荐的工作流程：

1. **首先尝试方法二**：使用精确匹配
2. **如果失败，尝试方法三**：使用备用匹配策略
3. **如果仍然失败，切换到方法一**：手动补全
4. **设置最大重试次数**：避免无限循环

### 关键注意事项：

- **精确匹配**：确保 `old_string` 完全匹配文件中的内容
- **包含足够上下文**：在匹配字符串中包含前后的内容
- **保持格式一致**：包括所有空格、换行符和缩进
- **错误处理**：设置合理的重试次数和超时时间

## 验证步骤

补全完成后，请验证：

1. **JSON 格式正确性**：使用 JSON 验证工具检查
2. **功能测试**：确保 Gemini CLI 功能正常工作
3. **UI 显示**：检查设置界面中是否正确显示 Gemini CLI 选项
4. **文件完整性**：确认没有破坏其他配置项
