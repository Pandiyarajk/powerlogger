# 📖 API Reference

Complete API reference for PowerLogger, including all functions, classes, and configuration options.

## 🚀 **Core Functions**

### **`get_logger(name, level=None, config_file=None)`**

Creates a basic Rich console logger with optional configuration.

**Parameters:**
- `name` (str): Logger name (required)
- `level` (int, optional): Logging level (default: from config or INFO)
- `config_file` (str, optional): Path to configuration file (default: `log_config.ini`)

**Returns:** Logger instance with Rich console handler

**Example:**
```python
from powerlogger import get_logger

# Basic logger
logger = get_logger("my_app")

# With custom level
logger = get_logger("debug_app", level=logging.DEBUG)

# With custom config
logger = get_logger("custom_app", config_file="my_config.ini")
```

---

### **`get_logger_with_file_handler(name, level=None, log_file=None, config_file=None)`**

Creates a logger with both Rich console and file output, including log rotation.

**Parameters:**
- `name` (str): Logger name (required)
- `level` (int, optional): Logging level (default: from config or INFO)
- `log_file` (str, optional): Log file path (default: from config or `logs/app.log`)
- `config_file` (str, optional): Path to configuration file (default: `log_config.ini`)

**Returns:** Logger instance with Rich console and file handlers

**Example:**
```python
from powerlogger import get_logger_with_file_handler

# Logger with file output
logger = get_logger_with_file_handler("file_app")

# With custom log file
logger = get_logger_with_file_handler("custom_file", log_file="logs/myapp.log")

# With custom level and config
logger = get_logger_with_file_handler(
    "debug_file", 
    level=logging.DEBUG, 
    config_file="debug_config.ini"
)
```

---

### **`get_logger_with_queue(name, level=None, config_file=None)`**

Creates a thread-safe logger using queue-based asynchronous processing.

**Parameters:**
- `name` (str): Logger name (required)
- `level` (int, optional): Logging level (default: from config or INFO)
- `config_file` (str, optional): Path to configuration file (default: `log_config.ini`)

**Returns:** Logger instance with ThreadSafeQueueHandler

**Example:**
```python
from powerlogger import get_logger_with_queue

# Thread-safe logger
logger = get_logger_with_queue("queue_app")

# With custom level
logger = get_logger_with_queue("debug_queue", level=logging.DEBUG)
```

---

### **`get_logger_with_queue_and_file(name, level=None, log_file=None, config_file=None)`**

Creates a complete solution logger with console, file, rotation, and thread safety.

**Parameters:**
- `name` (str): Logger name (required)
- `level` (int, optional): Logging level (default: from config or INFO)
- `log_file` (str, optional): Log file path (default: from config or `logs/app.log`)
- `config_file` (str, optional): Path to configuration file (default: `log_config.ini`)

**Returns:** Logger instance with all handlers (Rich console, file, queue)

**Example:**
```python
from powerlogger import get_logger_with_queue_and_file

# Complete solution logger
logger = get_logger_with_queue_and_file("production_app")

# With custom configuration
logger = get_logger_with_queue_and_file(
    "custom_prod",
    log_file="logs/production.log",
    config_file="prod_config.ini"
)
```

---

### **`cleanup_loggers()`**

Cleans up all loggers and handlers, ensuring proper resource cleanup.

**Parameters:** None

**Returns:** None

**Example:**
```python
from powerlogger import cleanup_loggers

# Clean up at application shutdown
cleanup_loggers()
```

---

## 🔧 **Utility Functions**

### **`load_config(config_file=None)`**

Loads configuration from INI file with fallback to defaults.

**Parameters:**
- `config_file` (str, optional): Path to configuration file (default: `log_config.ini`)

**Returns:** ConfigParser instance with loaded configuration

**Example:**
```python
from powerlogger import load_config

# Load default config
config = load_config()

# Load custom config
config = load_config("my_config.ini")

# Access configuration values
log_level = config.get('logging', 'level')
max_bytes = config.getint('file_handler', 'max_bytes')
```

---

### **`get_log_level_from_config(config, section='logging', key='level')`**

Extracts logging level from configuration with fallback to INFO.

**Parameters:**
- `config` (ConfigParser): Configuration instance
- `section` (str, optional): Configuration section (default: 'logging')
- `key` (str, optional): Configuration key (default: 'level')

**Returns:** Logging level constant (int)

**Example:**
```python
from powerlogger import load_config, get_log_level_from_config

config = load_config()
level = get_log_level_from_config(config)
print(f"Log level: {level}")  # e.g., 20 for INFO
```

---

## 🏗️ **Classes**

### **`WindowsSafeRotatingFileHandler`**

Windows-optimized file handler with intelligent log rotation and truncation.

**Inheritance:** `logging.handlers.RotatingFileHandler`

**Constructor:**
```python
WindowsSafeRotatingFileHandler(
    filename,
    mode='a',
    maxBytes=0,
    backupCount=0,
    encoding='utf-8',
    delay=False
)
```

**Parameters:**
- `filename` (str): Log file path
- `mode` (str): File open mode (default: 'a')
- `maxBytes` (int): Maximum file size before rotation (default: 0)
- `backupCount` (int): Number of backup files (default: 0, not used in truncation mode)
- `encoding` (str): File encoding (default: 'utf-8')
- `delay` (bool): Delay file creation (default: False for immediate creation)

**Key Methods:**

#### **`doRollover()`**
Performs log rotation by truncating the current file to 0 bytes.

**Parameters:** None

**Returns:** None

**Behavior:**
- Closes current file stream
- Truncates file to 0 bytes
- Reopens file for new logging
- Handles Windows file access conflicts

#### **`shouldRollover(record)`**
Determines if log rotation should occur based on file size.

**Parameters:**
- `record` (LogRecord): Log record to check

**Returns:** bool - True if rotation needed, False otherwise

**Example:**
```python
from powerlogger import WindowsSafeRotatingFileHandler

# Create handler with 1MB rotation
handler = WindowsSafeRotatingFileHandler(
    filename="logs/app.log",
    maxBytes=1048576,  # 1MB
    encoding='utf-8'
)

# Add to logger
logger.addHandler(handler)
```

---

### **`ThreadSafeQueueHandler`**

Asynchronous, thread-safe log handler using queue-based processing.

**Inheritance:** `logging.Handler`

**Constructor:**
```python
ThreadSafeQueueHandler(
    queue_size=100,
    flush_interval=0.1,
    handlers=None
)
```

**Parameters:**
- `queue_size` (int): Maximum queue size (default: 100)
- `flush_interval` (float): Flush interval in seconds (default: 0.1)
- `handlers` (list): List of handlers to process (default: None)

**Key Methods:**

#### **`emit(record)`**
Adds log record to the queue for asynchronous processing.

**Parameters:**
- `record` (LogRecord): Log record to queue

**Returns:** None

#### **`add_handler(handler)`**
Adds a handler to be processed by the queue worker.

**Parameters:**
- `handler` (Handler): Logging handler to add

**Returns:** None

#### **`remove_handler(handler)`**
Removes a handler from processing.

**Parameters:**
- `handler` (Handler): Logging handler to remove

**Returns:** None

#### **`start()`**
Starts the queue worker thread.

**Parameters:** None

**Returns:** None

#### **`stop()`**
Stops the queue worker thread gracefully.

**Parameters:** None

**Returns:** None

**Example:**
```python
from powerlogger import ThreadSafeQueueHandler, WindowsSafeRotatingFileHandler

# Create file handler
file_handler = WindowsSafeRotatingFileHandler("logs/app.log")

# Create queue handler
queue_handler = ThreadSafeQueueHandler(queue_size=1000, flush_interval=0.05)

# Add file handler to queue handler
queue_handler.add_handler(file_handler)

# Start processing
queue_handler.start()

# Add to logger
logger.addHandler(queue_handler)
```

---

## ⚙️ **Configuration Options**

### **Configuration File Structure**

PowerLogger uses INI-based configuration files with the following sections:

#### **`[logging]` Section**
```ini
[logging]
level = INFO                    # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
format = %(asctime)s - %(levelname)s - %(name)s - %(message)s
date_format = %Y-%m-%d %H:%M:%S
```

**Options:**
- `level`: Logging level (default: INFO)
- `format`: Log message format string
- `date_format`: Date/time format string

#### **`[file_handler]` Section**
```ini
[file_handler]
enabled = true                  # Enable file logging
log_file = logs/app.log         # Log file path
max_bytes = 1048576            # Maximum file size (1MB)
encoding = utf-8                # File encoding
```

**Options:**
- `enabled`: Enable/disable file handler (default: true)
- `log_file`: Log file path (default: logs/app.log)
- `max_bytes`: Maximum file size before rotation (default: 1048576)
- `encoding`: File encoding (default: utf-8)

#### **`[queue_handler]` Section**
```ini
[queue_handler]
enabled = true                  # Enable queue handler
queue_size = 100               # Maximum queue size
flush_interval = 0.1           # Flush interval in seconds
```

**Options:**
- `enabled`: Enable/disable queue handler (default: true)
- `queue_size`: Maximum queue size (default: 100)
- `flush_interval`: Flush interval in seconds (default: 0.1)

---

## 📊 **Logging Levels**

PowerLogger supports standard Python logging levels:

| Level | Numeric Value | Description | Use Case |
|-------|---------------|-------------|----------|
| **DEBUG** | 10 | Detailed information for debugging | Development, troubleshooting |
| **INFO** | 20 | General information about program execution | Normal operation, status updates |
| **WARNING** | 30 | Warning messages for potentially problematic situations | Deprecation warnings, resource usage |
| **ERROR** | 40 | Error messages for serious problems | Exceptions, failures |
| **CRITICAL** | 50 | Critical errors that may prevent the program from running | System failures, fatal errors |

**Example:**
```python
import logging
from powerlogger import get_logger

logger = get_logger("level_demo")

logger.debug("🔍 Debug information")
logger.info("ℹ️ General information")
logger.warning("⚠️ Warning message")
logger.error("❌ Error message")
logger.critical("🚨 Critical error!")
```

---

## 🔄 **Log Rotation Behavior**

### **Truncation Mode**

PowerLogger uses a truncation-based rotation strategy:

1. **File Size Monitoring**: Continuously monitors log file size
2. **Rotation Trigger**: When `max_bytes` is reached
3. **Truncation Process**: 
   - Closes current file stream
   - Truncates file to 0 bytes
   - Reopens file for new logging
4. **Windows Optimization**: Handles file access conflicts automatically

**Example:**
```python
from powerlogger import get_logger_with_file_handler

# Logger with 1MB rotation
logger = get_logger_with_file_handler(
    "rotation_demo",
    log_file="logs/rotation.log"
)

# Configuration in log_config.ini:
# [file_handler]
# max_bytes = 1048576  # 1MB
```

---

## 🧵 **Thread Safety Features**

### **Queue-Based Processing**

- **Asynchronous**: Log records are queued, not processed immediately
- **Non-blocking**: Log emission never blocks your application
- **Thread-safe**: Safe for multi-threaded environments
- **Configurable**: Adjustable queue size and flush intervals

### **Worker Thread Management**

- **Single Worker**: One dedicated thread processes all log records
- **Automatic Start**: Worker starts when handler is added to logger
- **Graceful Shutdown**: Worker stops when `cleanup_loggers()` is called
- **Error Recovery**: Robust error handling and fallback mechanisms

**Example:**
```python
from powerlogger import get_logger_with_queue
import threading
import time

logger = get_logger_with_queue("thread_demo")

def worker(worker_id):
    for i in range(100):
        logger.info(f"Worker {worker_id}: Message {i}")
        time.sleep(0.01)

# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for completion
for t in threads:
    t.join()

# Clean up
from powerlogger import cleanup_loggers
cleanup_loggers()
```

---

## 🌍 **UTF-8 Support**

### **Character Encoding**

- **File Encoding**: All log files use UTF-8 encoding
- **Console Output**: Rich library handles UTF-8 display
- **International Support**: Full Unicode character support
- **Emoji Support**: Emojis and special symbols

**Example:**
```python
from powerlogger import get_logger_with_file_handler

logger = get_logger_with_file_handler("unicode_demo", log_file="logs/unicode.log")

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

---

## 🚨 **Error Handling**

### **Built-in Error Recovery**

- **File Access Errors**: Automatic handling of Windows file conflicts
- **Queue Overflow**: Graceful handling when queue is full
- **Handler Failures**: Fallback mechanisms for failed handlers
- **Resource Cleanup**: Proper cleanup on errors and shutdown

### **Error Logging**

```python
from powerlogger import get_logger

logger = get_logger("error_demo")

try:
    # Risky operation
    result = 10 / 0
except Exception as e:
    logger.error(f"❌ Operation failed: {e}")
    logger.exception("📋 Full traceback:")
```

---

## 📈 **Performance Considerations**

### **Queue Configuration**

| Queue Size | Flush Interval | Performance | Memory Usage |
|------------|----------------|-------------|--------------|
| **100** | 0.1s | Good | Low |
| **500** | 0.05s | Better | Medium |
| **1000** | 0.02s | Best | High |

### **File Rotation Impact**

- **Truncation Overhead**: < 1ms per rotation
- **I/O Optimization**: Minimal disk I/O during rotation
- **Memory Efficiency**: No backup file management
- **Windows Compatibility**: Optimized for Windows file systems

---

## 🔗 **Integration Examples**

### **With Flask Web Application**
```python
from flask import Flask
from powerlogger import get_logger_with_queue_and_file

app = Flask(__name__)
logger = get_logger_with_queue_and_file("flask_app", log_file="logs/flask.log")

@app.route('/')
def home():
    logger.info("🏠 Home page accessed")
    return "Hello, World!"

@app.errorhandler(404)
def not_found(error):
    logger.warning("⚠️ 404 error: Page not found")
    return "Page not found", 404

if __name__ == '__main__':
    logger.info("🚀 Flask application starting...")
    app.run(debug=True)
```

### **With FastAPI**
```python
from fastapi import FastAPI
from powerlogger import get_logger_with_queue_and_file

app = FastAPI()
logger = get_logger_with_queue_and_file("fastapi_app", log_file="logs/fastapi.log")

@app.get("/")
async def root():
    logger.info("🏠 Root endpoint accessed")
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.info(f"📦 Item {item_id} requested")
    return {"item_id": item_id}
```

---

## 📝 **Best Practices**

### **Logger Naming**
```python
# ✅ Good: Descriptive, hierarchical names
logger = get_logger("myapp.database")
logger = get_logger("myapp.api.users")
logger = get_logger("myapp.worker.batch_processor")

# ❌ Avoid: Generic names
logger = get_logger("logger")
logger = get_logger("log")
```

### **Configuration Management**
```python
# ✅ Good: Use configuration files
logger = get_logger("myapp")  # Uses log_config.ini

# ✅ Good: Environment-specific configs
logger = get_logger("myapp", config_file="prod_config.ini")

# ❌ Avoid: Hard-coded values
logger = get_logger("myapp", level=logging.INFO)
```

### **Resource Cleanup**
```python
# ✅ Good: Clean up at shutdown
try:
    # Your application logic
    pass
finally:
    from powerlogger import cleanup_loggers
    cleanup_loggers()
```

---

## 🔍 **Debugging and Troubleshooting**

### **Enable Debug Logging**
```python
import logging
from powerlogger import get_logger

# Set to DEBUG level
logger = get_logger("debug_app", level=logging.DEBUG)

# Enable all debug messages
logger.debug("🔍 Debug information enabled")
```

### **Check Handler Status**
```python
from powerlogger import get_logger_with_queue_and_file

logger = get_logger_with_queue_and_file("status_app")

# Check handlers
for handler in logger.handlers:
    print(f"Handler: {type(handler).__name__}")
    if hasattr(handler, 'handlers'):
        for sub_handler in handler.handlers:
            print(f"  Sub-handler: {type(sub_handler).__name__}")
```

---

## 📚 **Related Documentation**

- **[Quick Start Guide](Quick-Start-Guide)** - Get started with PowerLogger
- **[Configuration](Configuration)** - Configuration options and examples
- **[Examples Gallery](Examples-Gallery)** - More usage examples
- **[Troubleshooting](Troubleshooting)** - Common issues and solutions

---

**💡 Tip**: Start with the basic `get_logger()` function and gradually add features as your needs grow. PowerLogger is designed to be simple to start with but powerful enough for production use!
