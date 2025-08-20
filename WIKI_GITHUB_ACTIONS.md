# 🚀 GitHub Actions Workflows

PowerLogger uses GitHub Actions for automated testing, building, and publishing. All workflows are optimized for Windows platforms and provide comprehensive CI/CD capabilities.

## 📋 **Available Workflows**

### **1. 🚀 Publish to PyPI** (`publish.yml`)
**Purpose**: Automatically publish PowerLogger to PyPI when releases are created.

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

**Jobs**:
```yaml
jobs:
  test:                    # Quick validation
  build-and-publish:       # Package building and PyPI upload
  test-installation:       # Verify PyPI installation
  notify:                  # Status notifications
```

---

### **2. 🧪 Test & Quality** (`test.yml`)
**Purpose**: Comprehensive testing and code quality checks on every push and pull request.

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

**Jobs**:
```yaml
jobs:
  test:                    # Quick validation
  test-matrix:             # Multi-Python testing
  lint:                    # Code quality checks
  security:                # Security analysis
  summary:                 # Results summary
```

---

### **3. 🪟 Windows-Only Build & Test** (`build-exe.yml`)
**Purpose**: Windows-specific testing, building, and performance analysis.

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

**Jobs**:
```yaml
jobs:
  test:                    # Quick validation
  windows-build:           # Multi-Python building
  windows-security:        # Security analysis
  windows-performance:     # Performance testing
  windows-summary:         # Windows results summary
```

---

### **4. 🐛 Debug Dependencies** (`debug-deps.yml`)
**Purpose**: Troubleshoot dependency and file location issues in CI/CD.

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

**Jobs**:
```yaml
jobs:
  test:                    # Quick validation
  debug:                   # Dependency debugging
  summary:                 # Debug results summary
```

---

## 🔧 **Simple Test Job Structure**

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

---

## 🚀 **How to Use**

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

---

## 🔧 **Setup Requirements**

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

---

## 📊 **Workflow Outputs**

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

---

## 🔍 **Monitoring Workflows**

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

---

## 🛠️ **Customization**

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

---

## 🚨 **Troubleshooting**

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

---

## 📈 **Best Practices**

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

---

## 🔗 **Related Resources**

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Publishing Guide](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
- [Python Package Building](https://packaging.python.org/tutorials/packaging-projects/)
- [GitHub Secrets Management](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

## 🎯 **Workflow Matrix**

| Workflow | Purpose | Python Versions | Platform | Key Features |
|----------|---------|-----------------|----------|--------------|
| **publish.yml** | PyPI Publishing | 3.11, 3.12, 3.13 | Windows | Auto-publish, PyPI testing |
| **test.yml** | Quality & Testing | 3.11, 3.12, 3.13 | Windows | Comprehensive testing, linting |
| **build-exe.yml** | Windows Build | 3.11, 3.12, 3.13 | Windows | Performance, security, coverage |
| **debug-deps.yml** | Troubleshooting | 3.11, 3.12, 3.13 | Windows | Dependency debugging, validation |

---

## 🚀 **Getting Started with Workflows**

1. **First Time Setup**:
   - Add PyPI API token to secrets
   - Enable GitHub Actions
   - Push to main branch to trigger first run

2. **Regular Development**:
   - Push changes to trigger testing
   - Create pull requests for review
   - Monitor workflow status

3. **Releasing**:
   - Create and push Git tags
   - Create GitHub releases
   - Monitor PyPI deployment

---

**🎉 With these Windows-optimized workflows, PowerLogger will automatically build, test, and publish to PyPI on Windows whenever you create a release!**

**🪟 Windows-First Approach**: All workflows are optimized for Windows compatibility, ensuring your package works perfectly on Windows platforms.

---

## 📝 **Workflow Files Location**

All workflow files are located in `.github/workflows/`:

- `.github/workflows/publish.yml` - PyPI publishing
- `.github/workflows/test.yml` - Testing and quality
- `.github/workflows/build-exe.yml` - Windows build and test
- `.github/workflows/debug-deps.yml` - Dependency debugging

---

## 🔄 **Workflow Triggers Summary**

| Event | publish.yml | test.yml | build-exe.yml | debug-deps.yml |
|-------|-------------|----------|----------------|----------------|
| **Push to main** | ❌ | ✅ | ✅ | ✅ |
| **Push to develop** | ❌ | ✅ | ✅ | ✅ |
| **Pull Request** | ❌ | ✅ | ✅ | ❌ |
| **Release** | ✅ | ❌ | ❌ | ❌ |
| **Manual Dispatch** | ✅ | ✅ | ✅ | ✅ |

---

**💡 Tip**: Start with the test workflow to ensure your code quality, then use the publish workflow when you're ready to release!
