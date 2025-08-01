@echo off
chcp 65001 >nul

:: Get current directory name for returning later
set "CURRENT_DIR=%CD%"
for %%i in ("%CURRENT_DIR%") do set "CURRENT_DIR_NAME=%%~nxi"

echo ========================================
echo Gemini CLI Auto Complement Script
echo ========================================
echo.

echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    pause
    exit /b 1
)

echo Checking directories...
if not exist "z-geminicli-install" (
    echo ERROR: z-geminicli-install directory not found
    pause
    exit /b 1
)

if not exist "..\Roo-Code" (
    echo ERROR: Target directory not found
    pause
    exit /b 1
)

echo.
echo ========================================
echo Git Cleanup and Preparation
echo ========================================

echo Checking if target directory is a Git repository...
cd /d "..\Roo-Code"
git status >nul 2>&1
if errorlevel 1 (
    echo WARNING: Target directory is not a Git repository
    echo Skipping Git cleanup...
    goto :start_complement
)

echo Target directory is a Git repository
echo.

echo Checking for uncommitted changes...
git diff --quiet
if errorlevel 1 (
    echo WARNING: There are uncommitted changes in the repository
    echo.
    set /p confirm="Do you want to continue? This will discard uncommitted changes. (Y/n): "
    if /i "%confirm%"=="" goto :continue_cleanup
    if /i "%confirm%"=="y" goto :continue_cleanup
    if /i "%confirm%"=="Y" goto :continue_cleanup
    echo Operation cancelled by user
    pause
    exit /b 1
) else (
    echo No uncommitted changes found
)

:continue_cleanup
echo.
echo Discarding uncommitted changes...
git checkout -- .
if errorlevel 1 (
    echo ERROR: Failed to discard uncommitted changes
    pause
    exit /b 1
)
echo Successfully discarded uncommitted changes

echo.
echo Cleaning untracked files and directories...
git clean -fd
if errorlevel 1 (
    echo WARNING: Failed to clean untracked files
) else (
    echo Successfully cleaned untracked files
)

echo.
echo Resetting to last commit...
git reset --hard HEAD
if errorlevel 1 (
    echo ERROR: Failed to reset to last commit
    pause
    exit /b 1
)
echo Successfully reset to last commit

:start_complement
echo.
echo ========================================
echo Starting Code Complement
echo ========================================

echo Returning to script directory...
cd /d "..\%CURRENT_DIR_NAME%"

echo Starting complement...
python gemini_cli_auto_complement.py

echo.
echo ========================================
echo Complement Completed
echo ========================================

echo Done!
echo.
echo Note: You can now review the changes and commit them to Git if needed.
pause 