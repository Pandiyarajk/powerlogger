# 🚀 GitHub Actions Workflows for PowerLogger (Windows)

This document explains how to use the automated GitHub Actions workflows for building, testing, and publishing the PowerLogger package on Windows platforms.

## 📋 Available Workflows

### **Simple Test Job Structure**
All workflows include a basic test job that provides quick validation:

```yaml
jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python -m pytest tests/ -v
```

This job runs first and provides immediate feedback on basic functionality.

### 1. 🚀 **Publish to PyPI (Windows)** (`publish.yml`)
**Triggers**: 
- GitHub Release published
- Manual workflow dispatch

**What it does**:
- **Simple Test Job**: Basic dependency installation and test execution
- Builds package for latest Python versions (3.11-3.13) on Windows
- Runs comprehensive Windows-specific tests
- Publishes to PyPI automatically
- Tests installation from PyPI on Windows
- Provides Windows-optimized build summaries

### 2. 🧪 **Test & Quality (Windows)** (`test.yml`)
**Triggers**:
- Push to main/develop branches
- Pull requests
- Manual workflow dispatch

**What it does**:
- **Simple Test Job**: Basic dependency installation and test execution
- Runs tests on Windows platform only
- Tests latest Python versions (3.11-3.13) on Windows
- Code quality checks (linting, formatting) on Windows
- Security analysis on Windows
- Windows-specific coverage reporting

### 3. 🪟 **Windows-Only Build & Test** (`build-exe.yml`)
**Triggers**:
- Push to main/develop branches
- Pull requests
- Manual workflow dispatch

**What it does**:
- **Simple Test Job**: Basic dependency installation and test execution
- Comprehensive Windows-only testing
- Tests Windows file handling and rotation features
- Security analysis and vulnerability scanning on Windows
- Performance testing on Windows
- Detailed Windows coverage reporting

### 4. 🐛 **Debug Dependencies** (`debug-deps.yml`)
**Triggers**:
- Push to main/develop branches
- Manual workflow dispatch

**What it does**:
- **Simple Test Job**: Basic dependency installation and test execution
- Troubleshoots dependency and file location issues
- Verifies repository structure and file existence
- Tests Python imports and package building
- Provides detailed debugging information
- Helps resolve CI/CD configuration problems

## 🔧 Setup Requirements

### **PyPI API Token**
To enable automatic publishing, you need to add your PyPI API token to GitHub Secrets:

1. **Get PyPI API Token**:
   - Go to [PyPI Account Settings](https://pypi.org/manage/account/token/)
   - Create new API token with scope "Entire account (all projects)"
   - Copy the token (starts with `pypi-`)

2. **Add to GitHub Secrets**:
   - Go to your GitHub repository
   - **Settings** → **Secrets and variables** → **Actions**
   - Click **New repository secret**
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI API token

### **Repository Settings**
Ensure your repository has:
- **Actions enabled** (Settings → Actions → General)
- **Branch protection** for main branch (recommended)
- **Required status checks** for workflows (optional)

## 🚀 How to Use

### **Automatic Publishing (Recommended)**

1. **Create a GitHub Release**:
   ```bash
   # Tag your release
   git tag v1.0.6
   git push origin v1.0.6
   
   # Create release on GitHub
   # Go to: https://github.com/Pandiyarajk/powerlogger/releases
   # Click "Create a new release"
   # Select the tag and publish
   ```

2. **Workflow Automatically Runs**:
   - Builds package for latest Python versions (3.11-3.13) on Windows
   - Runs comprehensive Windows-specific tests
   - Publishes to PyPI
   - Tests installation from PyPI on Windows
   - Provides Windows-optimized build summaries

### **Manual Publishing**

1. **Go to Actions Tab**:
   - Navigate to your repository's Actions tab
   - Select "🚀 Publish PowerLogger to PyPI"

2. **Run Workflow**:
   - Click "Run workflow"
   - Select branch (usually main)
   - Enter version number
   - Choose dry run or full publish
   - Click "Run workflow"

### **Testing Only**

1. **Push to Main/Develop**:
   - Any push triggers automatic Windows testing
   - Tests run on Windows platform only
   - Windows-specific quality checks performed

2. **Pull Request**:
   - Tests run automatically on Windows
   - Ensures Windows compatibility before merge

## 📊 Workflow Outputs

### **Build Summary**
Each workflow provides detailed Windows-specific summaries including:
- Build status for each Python version on Windows
- Windows test results and compatibility
- Package file information for Windows
- Windows installation test results

### **Coverage Reports**
- Code coverage metrics
- Uploaded to Codecov (if configured)
- Available in workflow artifacts

### **Security Analysis**
- Dependency vulnerability checks
- Code security analysis
- Detailed security reports

## 🔍 Monitoring Workflows

### **Workflow Status**
- **Green Check**: All tests passed
- **Red X**: Some tests failed
- **Yellow Circle**: Workflow in progress

### **Detailed Logs**
- Click on any workflow run
- Expand individual steps
- View detailed logs and outputs

### **Artifacts**
- Download build artifacts
- Access coverage reports
- Review security analysis

## 🛠️ Customization

### **Modify Python Versions**
Edit the workflow files to change supported Python versions on Windows:
```yaml
strategy:
  matrix:
    python-version: ["3.11", "3.12", "3.13"]
```

### **Windows-Specific Customization**
Add new Windows-specific test configurations:
```yaml
# Test different Windows versions
runs-on: [windows-latest, windows-2022, windows-2019]
```

### **Custom Windows Test Commands**
Modify test steps to run additional Windows-specific checks:
```yaml
- name: 🧪 Custom Windows Tests
  shell: powershell
  run: |
    python -m pytest tests/ -v -m "windows"
    python -m pytest tests/ -v -m "file_handling"
```

## 🚨 Troubleshooting

### **Common Issues**

1. **PyPI Authentication Failed**:
   - Check `PYPI_API_TOKEN` secret is set correctly
   - Verify token has proper scope
   - Ensure token hasn't expired

2. **Tests Failing**:
   - Check test logs for specific errors
   - Verify dependencies are correct
   - Check for platform-specific issues

3. **Build Failures**:
   - Review build logs
   - Check package configuration
   - Verify all required files are present

### **Debug Mode**
Enable debug logging by adding to workflow:
```yaml
env:
  ACTIONS_STEP_DEBUG: true
  ACTIONS_RUNNER_DEBUG: true
```

## 📈 Best Practices

### **Release Management**
1. **Use Semantic Versioning**: v1.0.0, v1.0.1, v1.1.0
2. **Create Release Notes**: Document changes clearly
3. **Test Before Release**: Use dry run mode first on Windows
4. **Monitor Deployment**: Check PyPI after publishing

### **Code Quality**
1. **Run Tests Locally**: Before pushing (on Windows)
2. **Check Formatting**: Use Black and isort
3. **Lint Code**: Run flake8 and mypy
4. **Security Scan**: Regular dependency checks
5. **Windows Compatibility**: Test file handling and encoding

### **Workflow Maintenance**
1. **Update Dependencies**: Keep actions up to date
2. **Monitor Performance**: Optimize slow workflows
3. **Review Logs**: Regular workflow health checks
4. **Backup Secrets**: Store credentials securely

## 🔗 Related Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Publishing Guide](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
- [Python Package Building](https://packaging.python.org/tutorials/packaging-projects/)
- [GitHub Secrets Management](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

**🎉 With these Windows-optimized workflows, PowerLogger will automatically build, test, and publish to PyPI on Windows whenever you create a release!**

**🪟 Windows-First Approach**: All workflows are optimized for Windows compatibility, ensuring your package works perfectly on Windows platforms.
