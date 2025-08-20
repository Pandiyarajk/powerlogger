# 🚀 Quick Start Guide

Welcome to PowerLogger! This guide will get you up and running with PowerLogger in minutes.

## 📋 **Prerequisites**

- **Python**: 3.11 or higher
- **Platform**: Windows (optimized), macOS, Linux
- **Package Manager**: pip

## 🚀 **Installation**

### **Basic Installation**
```bash
pip install powerlogger
```

### **Development Installation**
```bash
# Clone the repository
git clone https://github.com/Pandiyarajk/powerlogger.git
cd powerlogger

# Install in development mode
pip install -e ".[dev]"
```

### **Verify Installation**
```python
import powerlogger
print(f"PowerLogger version: {powerlogger.__version__}")
```

---

## 🎯 **Your First Logger**

### **1. Basic Console Logger**
```python
from powerlogger import get_logger

# Create a simple logger
logger = get_logger("my_app")

# Start logging
logger.info("🚀 Application started!")
logger.warning("⚠️ This is a warning message")
logger.error("❌ An error occurred")
logger.debug("🔍 Debug information")
```

**Output:**
```
2025-01-17 10:30:15,123 - INFO - my_app - 🚀 Application started!
2025-01-17 10:30:15,124 - WARNING - my_app - ⚠️ This is a warning message
2025-01-17 10:30:15,125 - ERROR - my_app - ❌ An error occurred
```

### **2. Logger with File Output**
```python
from powerlogger import get_logger_with_file_handler

# Create logger with file output
logger = get_logger_with_file_handler("file_app", log_file="logs/app.log")

# Log messages (will appear in both console and file)
logger.info("📝 This message goes to both console and file")
logger.warning("⚠️ Warning logged to file")
```

### **3. Thread-Safe Queue Logger**
```python
from powerlogger import get_logger_with_queue

# Create thread-safe logger
logger = get_logger_with_queue("queue_app")

# Safe for multi-threaded applications
logger.info("🧵 Thread-safe logging!")
```

### **4. Complete Solution Logger**
```python
from powerlogger import get_logger_with_queue_and_file

# Best of all worlds: console, file, rotation, thread-safe
logger = get_logger_with_queue_and_file("production_app", log_file="logs/prod.log")

# High-performance logging
logger.info("🚀 Production logging with all features!")
```

---

## ⚙️ **Configuration**

### **Create Configuration File**
Create `log_config.ini` in your project root:

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

### **Use Configuration**
```python
from powerlogger import get_logger

# Logger will automatically use log_config.ini
logger = get_logger("configured_app")

# Or specify custom config file
logger = get_logger("custom_app", config_file="my_config.ini")
```

---

## 🌟 **Common Patterns**

### **Application Startup/Shutdown**
```python
from powerlogger import get_logger, cleanup_loggers

logger = get_logger("my_app")

def main():
    logger.info("🚀 Starting application...")
    
    try:
        # Your application logic here
        logger.info("✅ Application running successfully")
        
        # Simulate work
        import time
        time.sleep(2)
        
    except Exception as e:
        logger.error(f"❌ Application error: {e}")
        logger.exception("📋 Full traceback:")
    
    finally:
        logger.info("🏁 Application shutting down...")
        cleanup_loggers()

if __name__ == "__main__":
    main()
```

### **Function/Method Logging**
```python
from powerlogger import get_logger
import time

logger = get_logger("function_logger")

def process_data(data):
    logger.info(f"🔄 Processing {len(data)} items...")
    
    start_time = time.time()
    
    try:
        # Process data
        result = [item * 2 for item in data]
        
        elapsed = time.time() - start_time
        logger.info(f"✅ Processed {len(result)} items in {elapsed:.2f}s")
        
        return result
        
    except Exception as e:
        logger.error(f"❌ Processing failed: {e}")
        raise

# Usage
data = [1, 2, 3, 4, 5]
result = process_data(data)
```

### **Error Handling with Logging**
```python
from powerlogger import get_logger

logger = get_logger("error_handler")

def risky_operation():
    try:
        # Simulate risky operation
        import random
        if random.random() < 0.5:
            raise ValueError("Random error occurred!")
        
        logger.info("✅ Operation completed successfully")
        
    except ValueError as e:
        logger.warning(f"⚠️ Expected error: {e}")
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        logger.exception("📋 Full error details:")
        
    finally:
        logger.debug("🔍 Operation cleanup completed")

# Run multiple times to see different outcomes
for i in range(3):
    logger.info(f"🔄 Attempt {i+1}")
    risky_operation()
```

---

## 🧵 **Multi-Threading Example**

### **Thread-Safe Logging**
```python
from powerlogger import get_logger_with_queue
import threading
import time

# Create thread-safe logger
logger = get_logger_with_queue("thread_app")

def worker(worker_id, count):
    logger.info(f"👷 Worker {worker_id} started")
    
    for i in range(count):
        logger.info(f"👷 Worker {worker_id}: Processing item {i+1}/{count}")
        time.sleep(0.1)  # Simulate work
    
    logger.info(f"✅ Worker {worker_id} completed")

def main():
    logger.info("🚀 Starting multi-threaded application")
    
    # Create worker threads
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i+1, 5))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    logger.info("🏁 All workers completed")
    
    # Clean up
    from powerlogger import cleanup_loggers
    cleanup_loggers()

if __name__ == "__main__":
    main()
```

---

## 🌍 **UTF-8 and International Support**

### **Multi-Language Logging**
```python
from powerlogger import get_logger_with_file_handler

logger = get_logger_with_file_handler("unicode_test", log_file="logs/unicode.log")

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

## 📊 **Performance Tips**

### **Optimal Configuration**
```ini
[queue_handler]
queue_size = 1000        # Larger for high-throughput
flush_interval = 0.05    # Faster for low-latency

[file_handler]
max_bytes = 5242880      # 5MB for production
```

### **High-Performance Logging**
```python
from powerlogger import get_logger_with_queue_and_file
import time

logger = get_logger_with_queue_and_file("perf_app", log_file="logs/perf.log")

# Batch logging for performance
start_time = time.time()
for i in range(10000):
    logger.info(f"Performance test message {i}")
    
elapsed = time.time() - start_time
print(f"⚡ 10,000 messages in {elapsed:.2f} seconds")
```

---

## 🔧 **Troubleshooting**

### **Common Issues**

#### **1. Import Error**
```python
# ❌ Wrong
import powerlogger

# ✅ Correct
from powerlogger import get_logger
```

#### **2. Configuration Not Found**
```bash
# Ensure log_config.ini is in your project root
ls -la log_config.ini
```

#### **3. Permission Errors (Windows)**
```python
# PowerLogger handles Windows file access automatically
# If issues persist, check file permissions
```

#### **4. Queue Full Errors**
```ini
# Increase queue size in log_config.ini
[queue_handler]
queue_size = 1000  # Default is 100
```

---

## 📚 **Next Steps**

Now that you have the basics, explore:

1. **[Configuration](Configuration)** - Advanced configuration options
2. **[Logging Types](Logging-Types)** - Different logger types and when to use them
3. **[UTF-8 Support](UTF-8-Support)** - International character support
4. **[Log Rotation](Log-Rotation)** - File management and rotation
5. **[Thread Safety](Thread-Safety)** - Multi-threading considerations
6. **[Examples Gallery](Examples-Gallery)** - More usage examples

---

## 🆘 **Need Help?**

- **📧 Email**: pandiyarajk@live.com
- **🐛 Issues**: [GitHub Issues](https://github.com/Pandiyarajk/powerlogger/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Pandiyarajk/powerlogger/discussions)
- **📖 Documentation**: [GitHub README](https://github.com/Pandiyarajk/powerlogger#readme)

---

**🎉 Congratulations! You're now logging with PowerLogger!**

Start with simple console logging and gradually add file output, rotation, and queue features as your needs grow.
