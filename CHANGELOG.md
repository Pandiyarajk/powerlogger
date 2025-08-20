# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-08-20

### Added
- **Core Logging**: Rich console output with beautiful formatting and colors
- **File Logging**: Automatic log file creation with configurable paths
- **Log Rotation**: Size-based log file rotation with truncation strategy (no backup files)
- **Thread Safety**: Queue-based asynchronous logging for multi-threaded applications
- **Windows Optimization**: Windows-safe file handling with proper encoding support
- **Configuration Management**: INI-based configuration with sensible defaults
- **UTF-8 Support**: Full Unicode support for international character logging

### Features
- **Rich Console Output**: Beautiful, colored console logging using the Rich library
- **File Rotation**: Automatic log file size management with configurable limits
- **Queue Processing**: Thread-safe logging with configurable queue sizes and flush intervals
- **Multiple Logger Types**: Console-only, file-only, and combined logging options
- **Configuration Files**: Easy customization via `log_config.ini` files
- **Error Handling**: Robust error handling with fallback configurations
- **Cleanup Functions**: Proper resource cleanup for file handlers and threads

### Technical Specifications
- **Python Version**: Requires Python 3.11 or higher
- **Dependencies**: Rich library for console formatting
- **File Size Limit**: Configurable log file size limits (default: 10MB)
- **Queue Size**: Configurable queue sizes for thread-safe logging
- **Flush Interval**: Configurable flush intervals for queue processing
- **Encoding**: UTF-8 encoding for all file operations
- **Platform**: Windows-optimized with cross-platform compatibility

### Configuration Options
- **Log Level**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Output Mode**: Console, file, or both
- **File Rotation**: Configurable maximum file sizes
- **Queue Settings**: Enable/disable queue-based logging with size and interval controls
- **Formatting**: Customizable log message formats
- **Directory Management**: Automatic logs directory creation

### Use Cases
- **Application Logging**: Comprehensive logging for desktop and web applications
- **Development**: Enhanced debugging and development logging
- **Production**: Reliable file-based logging for production environments
- **Multi-threaded Apps**: Thread-safe logging for concurrent applications
- **Windows Applications**: Optimized logging for Windows environments
