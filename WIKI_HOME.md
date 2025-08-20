# 🚀 PowerLogger Wiki

Welcome to the **PowerLogger Wiki** - your comprehensive guide to understanding, using, and contributing to PowerLogger, the high-performance, thread-safe logging library built with Python's logging module and enhanced with the Rich library.

## 📚 Table of Contents

### 🏠 **Getting Started**
- [Home](Home) ← You are here
- [Quick Start Guide](Quick-Start-Guide)
- [Installation](Installation)
- [Configuration](Configuration)

### 🎯 **Core Features**
- [Logging Types](Logging-Types)
- [UTF-8 Support](UTF-8-Support)
- [Log Rotation](Log-Rotation)
- [Thread Safety](Thread-Safety)
- [Windows Optimization](Windows-Optimization)

### 🛠️ **Development & Testing**
- [Development Setup](Development-Setup)
- [Testing Guide](Testing-Guide)
- [Contributing Guidelines](Contributing-Guidelines)
- [Code Style Guide](Code-Style-Guide)

### 🚀 **CI/CD & Deployment**
- [GitHub Actions Workflows](GitHub-Actions-Workflows)
- [PyPI Publishing](PyPI-Publishing)
- [Release Management](Release-Management)
- [Troubleshooting](Troubleshooting)

### 📖 **Reference**
- [API Reference](API-Reference)
- [Configuration Options](Configuration-Options)
- [Examples Gallery](Examples-Gallery)
- [Performance Benchmarks](Performance-Benchmarks)

---

## 🌟 **What is PowerLogger?**

PowerLogger is a modern, high-performance logging library designed for Python applications that need:

- **🚀 High Performance**: Asynchronous, non-blocking logging with configurable queues
- **🪟 Windows Optimized**: Special handling for Windows file access and compatibility
- **🎨 Beautiful Output**: Rich console formatting with colors, emojis, and structured display
- **🌍 Full UTF-8 Support**: International characters, emojis, and special symbols
- **🔄 Smart Rotation**: Intelligent log file management with truncation-based rotation
- **🧵 Thread Safe**: Enterprise-grade thread safety for multi-threaded applications

### **Key Benefits**

| Feature | Benefit |
|---------|---------|
| **Rich Console** | Beautiful, colored output with emojis and formatting |
| **UTF-8 Support** | Log in any language with proper character encoding |
| **Thread Safety** | Safe logging in multi-threaded environments |
| **Windows Optimized** | Special handling for Windows file operations |
| **Performance** | Non-blocking logging with configurable performance |
| **Flexibility** | Multiple logger types for different use cases |

---

## 🚀 **Quick Overview**

### **Installation**
```bash
pip install powerlogger
```

### **Basic Usage**
```python
from powerlogger import get_logger

logger = get_logger("my_app")
logger.info("🚀 Application started!")
logger.warning("⚠️ This is a warning")
logger.error("❌ An error occurred")
```

### **Advanced Usage**
```python
from powerlogger import get_logger_with_queue_and_file

# Thread-safe logger with file rotation
logger = get_logger_with_queue_and_file("production_app")
logger.info("🔄 Processing batch job...")
```

---

## 🎯 **Supported Python Versions**

PowerLogger supports **Python 3.11+** for optimal performance and modern features:

- **Python 3.11** ✅ (Minimum supported)
- **Python 3.12** ✅ (Recommended)
- **Python 3.13** ✅ (Latest features)

### **Why Python 3.11+?**

- **Better Performance**: 10-60% faster than older versions
- **Enhanced Error Messages**: Improved debugging experience
- **Modern Type Hints**: Better type checking and IDE support
- **Async Improvements**: Enhanced async/await capabilities
- **Security Features**: Latest security enhancements

---

## 🏗️ **Architecture Overview**

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Application   │───▶│  PowerLogger     │───▶│  Output Handlers│
│                 │    │                  │    │                 │
│                 │    │  ┌─────────────┐ │    │ • Rich Console  │
│                 │    │  │   Queue     │ │    │ • File Handler  │
│                 │    │  │   Worker    │ │    │ • Rotation      │
│                 │    │  └─────────────┘ │    │ • UTF-8 Support │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### **Core Components**

1. **Logger Factory**: Creates different types of loggers
2. **Queue Handler**: Manages asynchronous log processing
3. **File Handler**: Handles file output with rotation
4. **Rich Console**: Beautiful terminal output
5. **Configuration**: Flexible INI-based configuration

---

## 🔧 **Configuration System**

PowerLogger uses a flexible configuration system based on INI files:

```ini
[logging]
level = INFO
format = %(asctime)s - %(levelname)s - %(name)s - %(message)s
date_format = %Y-%m-%d %H:%M:%S

[file_handler]
enabled = true
log_file = logs/app.log
max_bytes = 1048576
encoding = utf-8

[queue_handler]
enabled = true
queue_size = 100
flush_interval = 0.1
```

### **Configuration Sources**

1. **Default**: Built-in sensible defaults
2. **File**: `log_config.ini` in your project
3. **Custom**: Specify custom config file path
4. **Environment**: Override with environment variables

---

## 🧪 **Testing & Quality**

PowerLogger includes comprehensive testing:

- **Unit Tests**: Core functionality testing
- **Integration Tests**: End-to-end workflow testing
- **Performance Tests**: Benchmarking and profiling
- **Windows Tests**: Platform-specific compatibility
- **Security Tests**: Vulnerability scanning

### **Running Tests**
```bash
# Install development dependencies
pip install powerlogger[dev]

# Run all tests
python -m pytest tests/ -v

# Run specific test categories
python -m pytest tests/ -m "slow"
python -m pytest tests/ -m "integration"
```

---

## 🚀 **CI/CD Pipeline**

PowerLogger uses GitHub Actions for automated:

- **Testing**: Windows-optimized test suites
- **Building**: Package building and validation
- **Publishing**: Automatic PyPI deployment
- **Quality**: Code quality and security checks
- **Performance**: Performance benchmarking

### **Workflow Features**

- **Windows-First**: All workflows optimized for Windows
- **Matrix Testing**: Multiple Python versions (3.11, 3.12, 3.13)
- **Security Scanning**: Automated vulnerability detection
- **Performance Testing**: Continuous performance monitoring
- **Coverage Reporting**: Code coverage metrics

---

## 📊 **Performance Characteristics**

### **Benchmark Results**

| Operation | Performance |
|-----------|-------------|
| **Console Logging** | ~10,000 msgs/sec |
| **File Logging** | ~5,000 msgs/sec |
| **Queue Logging** | ~50,000 msgs/sec |
| **Rotation** | < 1ms overhead |
| **Memory Usage** | ~2MB base + queue size |

### **Performance Tips**

1. **Queue Size**: Use 100-1000 for optimal performance
2. **Flush Interval**: 0.1s provides good balance
3. **File Rotation**: Truncation minimizes I/O overhead
4. **Thread Count**: Single worker thread is optimal
5. **Memory**: Monitor queue size for long-running apps

---

## 🌟 **Use Cases**

### **Web Applications**
- Request/response logging
- Performance monitoring
- Error tracking
- User activity logging

### **Desktop Applications**
- User interaction logging
- File operation tracking
- Error reporting
- Performance profiling

### **Data Processing**
- Batch job monitoring
- Progress tracking
- Error handling
- Performance metrics

### **System Services**
- Service lifecycle logging
- Health monitoring
- Error reporting
- Performance tracking

---

## 🤝 **Community & Support**

### **Getting Help**

- **📧 Email**: pandiyarajk@live.com
- **🐛 Issues**: [GitHub Issues](https://github.com/Pandiyarajk/powerlogger/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Pandiyarajk/powerlogger/discussions)
- **📖 Documentation**: [GitHub README](https://github.com/Pandiyarajk/powerlogger#readme)

### **Contributing**

We welcome contributions! See our [Contributing Guidelines](Contributing-Guidelines) for:

- Code contributions
- Documentation improvements
- Bug reports
- Feature requests
- Testing help

### **Code of Conduct**

- Be respectful and inclusive
- Focus on technical discussions
- Help others learn and grow
- Follow project guidelines

---

## 📈 **Roadmap & Future**

### **Short Term (Next 3 months)**
- [ ] Enhanced configuration validation
- [ ] Additional output formats (JSON, XML)
- [ ] Performance optimizations
- [ ] Extended test coverage

### **Medium Term (3-6 months)**
- [ ] Structured logging support
- [ ] Log aggregation features
- [ ] Advanced filtering options
- [ ] Plugin system

### **Long Term (6+ months)**
- [ ] Distributed logging support
- [ ] Machine learning integration
- [ ] Advanced analytics
- [ ] Enterprise features

---

## 📄 **License & Legal**

PowerLogger is licensed under the **MIT License** - see the [LICENSE](https://github.com/Pandiyarajk/powerlogger/blob/main/LICENSE) file for details.

### **License Benefits**

- **Commercial Use**: ✅ Allowed
- **Modification**: ✅ Allowed
- **Distribution**: ✅ Allowed
- **Private Use**: ✅ Allowed
- **Liability**: ❌ Limited
- **Warranty**: ❌ None

---

## 🌟 **Star History**

If you find PowerLogger useful, please consider giving it a star on GitHub! ⭐

Your support helps us:
- Improve documentation
- Add new features
- Fix bugs faster
- Support more platforms
- Build a stronger community

---

## 🔗 **Quick Links**

- **📦 PyPI Package**: [powerlogger](https://pypi.org/project/powerlogger/)
- **🐍 Python Support**: 3.11, 3.12, 3.13
- **🪟 Platform**: Windows-optimized, cross-platform
- **📚 Documentation**: [GitHub README](https://github.com/Pandiyarajk/powerlogger#readme)
- **📋 Changelog**: [CHANGELOG.md](https://github.com/Pandiyarajk/powerlogger/blob/main/CHANGELOG.md)
- **🚀 Actions**: [GitHub Actions](https://github.com/Pandiyarajk/powerlogger/actions)

---

**Made with ❤️ by [Pandiyaraj Karuppasamy](https://github.com/Pandiyarajk)**

_PowerLogger - Empowering your applications with beautiful, high-performance logging._

---

## 📝 **Wiki Navigation**

Use the navigation menu on the right to explore different sections of this wiki. Each page contains detailed information about specific aspects of PowerLogger.

**💡 Tip**: Start with the [Quick Start Guide](Quick-Start-Guide) if you're new to PowerLogger!
