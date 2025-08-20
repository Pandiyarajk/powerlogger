# PowerLogger

A high-performance, thread-safe logging library built with Python's logging module and enhanced with the Rich library for beautiful console output with full UTF-8 support.

[![PyPI version](https://badge.fury.io/py/powerlogger.svg)](https://badge.fury.io/py/powerlogger)
[![Python versions](https://img.shields.io/pypi/pyversions/powerlogger.svg)](https://pypi.org/project/powerlogger/)
[![License](https://img.shields.io/pypi/l/powerlogger.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **🎨 Rich Console Output**: Beautiful, colored logging with the Rich library
- **🔄 Thread-Safe Queue Logging**: Asynchronous, non-blocking log processing
- **📁 File Rotation**: Automatic log file rotation with size-based truncation
- **🌍 UTF-8 Support**: Full Unicode and emoji support in log files
- **⚙️ Configuration Management**: Flexible configuration via `log_config.ini`
- **🪟 Windows Optimized**: Special handling for Windows file access issues
- **🔧 Multiple Logger Types**: Console-only, file-only, queue-based, and combined loggers
- **⚡ High Performance**: Optimized for real-time logging applications
- **🛡️ Production Ready**: Comprehensive error handling and recovery mechanisms

## 🚀 Installation

```bash
pip install powerlogger
```

## 🎯 Quick Start

```python
from powerlogger import get_logger

# Create a basic logger
logger = get_logger("my_app")

# Log messages with beautiful formatting
logger.info("🚀 Application started successfully!")
logger.warning("⚠️  This is a warning message")
logger.error("❌ An error occurred during execution")
logger.debug("🔍 Debug information for developers")
```

## 🚀 Automated Publishing (Windows)

PowerLogger uses GitHub Actions for automated building, testing, and publishing to PyPI on Windows:

- **🚀 Auto-publish**: Creates GitHub releases automatically
- **🪟 Windows-optimized testing**: Comprehensive Windows compatibility testing
- **📦 Multi-version support**: Python 3.11-3.13 compatibility on Windows
- **🔒 Security scanning**: Automated vulnerability checks on Windows
- **📊 Coverage reporting**: Windows-specific code coverage metrics
- **⚡ Performance testing**: Windows performance and scalability testing

See [GitHub Actions Guide](GITHUB_ACTIONS.md) for detailed Windows workflow information.

## 📚 Logger Types

### Basic Logger (Console Only)
```python
from powerlogger import get_logger

logger = get_logger("app_name")
# Beautiful console output with colors and formatting
```

### File Logger with Rotation
```python
from powerlogger import get_logger_with_file_handler

logger = get_logger_with_file_handler("app_name")
# Logs to both console and file with automatic rotation
```

### Queue Logger (Thread-Safe)
```python
from powerlogger import get_logger_with_queue

logger = get_logger_with_queue("app_name")
# Asynchronous logging for high-performance applications
```

### Complete Solution (Queue + File)
```python
from powerlogger import get_logger_with_queue_and_file

logger = get_logger_with_queue_and_file("app_name")
# Best of both worlds: thread-safe + file output + rotation
```

## ⚙️ Configuration

Create `log_config.ini` in your project root:

```ini
[app]
name = my_app

[logging]
output_mode = both
level = INFO
format = %%(levelname)s %%(name)s - %%(message)s
console_format = %%(levelname)s %%(message)s
logs_dir = logs
max_bytes = 1048576
queue_enabled = true
queue_size = 100
flush_interval = 0.1
```

### Configuration Options

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `level` | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL) | INFO | `DEBUG` |
| `format` | Log message format for files | `%(levelname)s %(name)s - %(message)s` | `%(asctime)s - %(levelname)s - %(message)s` |
| `console_format` | Log message format for console | `%(levelname)s %(message)s` | `%(levelname)s: %(message)s` |
| `logs_dir` | Directory for log files | `logs` | `app_logs` |
| `max_bytes` | Maximum log file size before rotation | 1MB (1048576) | 5242880 (5MB) |
| `queue_enabled` | Enable thread-safe queue logging | true | false |
| `queue_size` | Maximum queue size for log records | 100 | 1000 |
| `flush_interval` | Queue flush interval in seconds | 0.1 | 0.5 |

## 🔄 Log Rotation

PowerLogger automatically manages log file sizes through intelligent truncation:

- **Size-based Rotation**: Logs rotate when they reach `max_bytes`
- **Truncation Strategy**: Current log file is truncated to start fresh
- **Single File Management**: Maintains one log file instead of multiple backups
- **Windows Optimized**: Special handling for Windows file access conflicts

## 🧵 Thread Safety

The queue-based loggers provide enterprise-grade thread safety:

- **🔄 Asynchronous Processing**: Log records are buffered in a thread-safe queue
- **👷 Dedicated Worker**: Single worker thread processes all log records
- **⚡ Non-blocking**: Log emission never blocks your application
- **📊 Configurable**: Adjustable queue size and flush intervals
- **🛡️ Error Handling**: Robust error recovery and fallback mechanisms

## 💡 Usage Examples

### Basic Application Logging
```python
from powerlogger import get_logger

logger = get_logger("my_application")

def main():
    logger.info("🚀 Starting application")
    
    try:
        # Your application logic here
        logger.info("✅ Application running successfully")
        logger.debug("🔍 Processing user input...")
    except Exception as e:
        logger.error(f"❌ Application error: {e}")
        logger.exception("📋 Full traceback:")
    
    logger.info("🏁 Application finished")

if __name__ == "__main__":
    main()
```

### Web Application with File Logging
```python
from powerlogger import get_logger_with_file_handler
import time

logger = get_logger_with_file_handler("web_app")

def handle_request(request_id):
    logger.info(f"📥 Processing request {request_id}")
    time.sleep(0.1)  # Simulate work
    logger.info(f"✅ Request {request_id} completed")

# Simulate multiple requests
for i in range(100):
    handle_request(i)
```

### High-Performance Multi-threaded Logging
```python
from powerlogger import get_logger_with_queue_and_file
import threading
import time

logger = get_logger_with_queue_and_file("high_perf_app")

def worker(worker_id):
    for i in range(1000):
        logger.info(f"👷 Worker {worker_id}: Processing task {i}")
        time.sleep(0.001)  # Very fast logging

# Start multiple worker threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

# Wait for completion
for t in threads:
    t.join()

# Clean up resources
from powerlogger import cleanup_loggers
cleanup_loggers()
```

### UTF-8 and Emoji Support
```python
from powerlogger import get_logger_with_file_handler

logger = get_logger_with_file_handler("unicode_test")

# International characters
logger.info("Hola mundo! Bonjour le monde! Hallo Welt!")
logger.warning("Special chars: á é í ó ú ñ ç")

# Emojis and symbols
logger.info("✅ Success! 🚀 Launching... 🌟 Amazing!")
logger.error("❌ Error occurred 💥 Boom! 🔥 Fire!")

# Complex Unicode
logger.info("世界 🌍 2024 © ® ™")
logger.debug("Math: ± × ÷ √ ∞ ≠ ≤ ≥")
```

## ⚡ Performance Considerations

- **📊 Queue Size**: Smaller queues (100-1000) provide better real-time logging
- **⏱️ Flush Interval**: Lower intervals (0.1-0.5s) reduce latency but increase CPU usage
- **💾 File Rotation**: Truncation-based rotation minimizes I/O overhead
- **🧵 Thread Count**: Single worker thread optimizes resource usage
- **🚀 Memory Usage**: Efficient memory management for long-running applications

## 🛠️ Troubleshooting

### Console Colors Not Working
- **Windows**: Use Windows Terminal or enable ANSI support
- **macOS/Linux**: Ensure `TERM` environment variable is set
- **Check**: Verify your terminal supports ANSI color codes

### Log Files Not Rotating
- **File Size**: Ensure file size exceeds `max_bytes` setting
- **Permissions**: Check write permissions to the logs directory
- **Configuration**: Verify `log_config.ini` is in the correct location

### Queue Performance Issues
- **Queue Full**: Increase `queue_size` or reduce logging frequency
- **High Latency**: Decrease `flush_interval` for faster processing
- **Memory Usage**: Monitor queue size and adjust accordingly

### Windows File Access Errors
- **Built-in Protection**: PowerLogger includes special Windows handling
- **File Locks**: Ensure no other processes are accessing log files
- **Permissions**: Run with appropriate user permissions

## 📖 API Reference

### Core Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `get_logger(name, level, config_file)` | Basic Rich console logger | Logger instance |
| `get_logger_with_file_handler(name, level, log_file, config_file)` | Logger with file output and rotation | Logger instance |
| `get_logger_with_queue(name, level, config_file)` | Thread-safe queue logger | Logger instance |
| `get_logger_with_queue_and_file(name, level, log_file, config_file)` | Complete solution | Logger instance |
| `cleanup_loggers()` | Clean up all loggers and handlers | None |

### Utility Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `load_config(config_file)` | Load configuration from INI file | ConfigParser instance |
| `get_log_level_from_config(config)` | Get log level from config | Logging level constant |

### Classes

| Class | Description | Purpose |
|-------|-------------|---------|
| `WindowsSafeRotatingFileHandler` | Windows-optimized file rotation | Handle file rotation safely |
| `ThreadSafeQueueHandler` | Asynchronous log processing | Process logs in background |

## 🧪 Testing

Run the test suite to verify everything works:

```bash
# Install development dependencies
pip install powerlogger[dev]

# Run tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_logging.py -v
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Add** tests if applicable
5. **Commit** your changes (`git commit -m 'Add amazing feature'`)
6. **Push** to the branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/Pandiyarajk/powerlogger.git
cd powerlogger

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Pandiyarajk/powerlogger/blob/main/LICENSE) file for details.

## 📋 Changelog

See [CHANGELOG.md](https://github.com/Pandiyarajk/powerlogger/blob/main/CHANGELOG.md) for a detailed history of changes and features.

## 🌟 What's New in 1.0.0

- **🎉 Production Release**: First stable release with comprehensive features
- **🔄 Truncation-based Rotation**: Simplified log rotation strategy
- **⚡ Performance Optimizations**: Enhanced queue processing and file handling
- **🛡️ Windows Compatibility**: Improved file access handling for Windows
- **📚 Enhanced Documentation**: Comprehensive guides and examples
- **🧪 Test Coverage**: Extensive test suite for reliability
- **🔧 Configuration Management**: Flexible and robust configuration system

## 📞 Support

- **📧 Email**: pandiyarajk@live.com
- **🐛 Issues**: [GitHub Issues](https://github.com/Pandiyarajk/powerlogger/issues)
- **📖 Documentation**: [GitHub README](https://github.com/Pandiyarajk/powerlogger#readme)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Pandiyarajk/powerlogger/discussions)

## ⭐ Star History

If you find PowerLogger useful, please consider giving it a star on GitHub! ⭐

---

**Made with ❤️ by [Pandiyaraj Karuppasamy](https://github.com/Pandiyarajk)**

*PowerLogger - Empowering your applications with beautiful, high-performance logging.*
