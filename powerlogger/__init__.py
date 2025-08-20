"""
PowerLogger - Enhanced logging functionality with Rich console output and file rotation.

A Python logging library that provides:
- Rich console output with colors and formatting
- File logging with automatic rotation
- Thread-safe queue-based logging
- Windows-optimized file handling
- Configuration management via INI files
"""

__version__ = "0.1.0"
__author__ = "Pandiyaraj Karuppasamy"
__email__ = "pandiyarajk@live.com"

from .powerlogger import (
    ThreadSafeQueueHandler,
    WindowsSafeRotatingFileHandler,
    cleanup_loggers,
    get_logger,
    get_logger_with_file_handler,
    get_logger_with_queue,
    get_logger_with_queue_and_file,
)

__all__ = [
    "ThreadSafeQueueHandler",
    "WindowsSafeRotatingFileHandler",
    "cleanup_loggers",
    "get_logger",
    "get_logger_with_file_handler",
    "get_logger_with_queue",
    "get_logger_with_queue_and_file",
]
