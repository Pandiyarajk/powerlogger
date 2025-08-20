"""
Rich UTF-8 Logger Module

Enhanced logging functionality using the 'rich' library with thread-safe queue processing,
file rotation, UTF-8 support, and configuration management.
"""

import configparser
import logging
import logging.handlers
import os
import queue
import threading
import time
from typing import Any, Dict, Optional

from rich.console import Console
from rich.logging import RichHandler


class WindowsSafeRotatingFileHandler(logging.handlers.RotatingFileHandler):
    """Windows-safe rotating file handler with custom naming convention."""

    def emit(self, record):
        """Emit a record and check for rotation after writing."""
        super().emit(record)

        if self.shouldRollover(record):
            try:
                self.doRollover()
                print(f"Log rotation performed for {self.baseFilename}")
            except Exception as e:
                print(f"Error during log rotation: {e}")

    def doRollover(self):
        """Perform log rotation by truncating the current file."""
        if self.stream:
            self.stream.close()
            self.stream = None

        # Simply truncate the current file instead of creating backups
        if os.path.exists(self.baseFilename):
            try:
                # Truncate the file to 0 bytes
                with open(self.baseFilename, "w", encoding="utf-8") as f:
                    pass  # This creates/truncates the file
                print(f"Log file truncated: {self.baseFilename}")
            except OSError as e:
                print(f"Error truncating log file: {e}")

        if not self.delay:
            self.stream = self._open()


class ThreadSafeQueueHandler(logging.Handler):
    """Thread-safe queue handler for asynchronous logging."""

    def __init__(self, queue_size: int = 1000, flush_interval: float = 1.0):
        """Initialize queue handler with specified size and flush interval."""
        super().__init__()
        self.queue: queue.Queue = queue.Queue(maxsize=queue_size)
        self.flush_interval = flush_interval
        self.running = False
        self.worker_thread: Optional[threading.Thread] = None
        self.lock = threading.Lock()
        self.handlers: list[logging.Handler] = []
        self._start_worker()

    def add_handler(self, handler: logging.Handler):
        """Add a handler to the queue handler."""
        self.handlers.append(handler)

    def remove_handler(self, handler: logging.Handler):
        """Remove a handler from the queue handler."""
        if handler in self.handlers:
            self.handlers.remove(handler)

    def check_rotation(self):
        """Check if any file handlers need rotation and perform it."""
        for handler in self.handlers:
            if hasattr(handler, "shouldRollover") and hasattr(handler, "doRollover"):
                try:
                    dummy_record = logging.LogRecord(
                        name="rotation_check",
                        level=logging.INFO,
                        pathname="",
                        lineno=0,
                        msg="",
                        args=(),
                        exc_info=None,
                    )

                    if handler.shouldRollover(dummy_record):
                        handler.doRollover()
                        print(
                            f"Log rotation performed for {getattr(handler, 'baseFilename', 'unknown')}"
                        )
                except Exception as e:
                    print(f"Error during rotation check: {e}")

    def _start_worker(self):
        """Start the worker thread for processing queued log records."""
        if not self.running:
            self.running = True
            self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
            self.worker_thread.start()

    def _worker_loop(self):
        """Worker thread loop for processing queued log records."""
        last_rotation_check = time.time()
        rotation_check_interval = 0.2

        while self.running:
            try:
                record = self.queue.get(timeout=self.flush_interval)
                if record is not None:
                    self._process_record(record)
                self.queue.task_done()

                current_time = time.time()
                if current_time - last_rotation_check >= rotation_check_interval:
                    self.check_rotation()
                    last_rotation_check = current_time

            except queue.Empty:
                current_time = time.time()
                if current_time - last_rotation_check >= rotation_check_interval:
                    self.check_rotation()
                    last_rotation_check = current_time
                continue
            except Exception as e:
                print(f"Error processing log record: {e}")

    def _process_record(self, record: logging.LogRecord):
        """Process a single log record."""
        try:
            for handler in self.handlers:
                if record.levelno >= handler.level:
                    handler.emit(record)

                    if hasattr(handler, "shouldRollover") and hasattr(
                        handler, "doRollover"
                    ):
                        try:
                            dummy_record = logging.LogRecord(
                                name="rotation_check",
                                level=logging.INFO,
                                pathname="",
                                lineno=0,
                                msg="",
                                args=(),
                                exc_info=None,
                            )

                            if handler.shouldRollover(dummy_record):
                                handler.doRollover()
                                print(
                                    f"Log rotation performed for {getattr(handler, 'baseFilename', 'unknown')}"
                                )
                        except Exception as e:
                            print(f"Error during log rotation: {e}")

        except Exception as e:
            print(f"Error emitting log record: {e}")

    def emit(self, record: logging.LogRecord):
        """Emit a log record by adding it to the queue."""
        try:
            record.msg = str(record.msg)
            record.args = None

            try:
                self.queue.put_nowait(record)
            except queue.Full:
                print(f"Log queue is full, dropping log record: {record.getMessage()}")
        except Exception as e:
            print(f"Error queuing log record: {e}")

    def close(self):
        """Close the handler and stop the worker thread."""
        with self.lock:
            if self.running:
                self.running = False
                if self.worker_thread and self.worker_thread.is_alive():
                    self.worker_thread.join(timeout=5.0)
                super().close()


def load_config(config_file: str = "log_config.ini") -> configparser.ConfigParser:
    """Load configuration from log_config.ini file with fallback defaults."""
    config = configparser.ConfigParser()

    config["app"] = {"name": "powerlogger_app"}

    config["logging"] = {
        "output_mode": "both",
        "level": "INFO",
        "format": "%%(levelname)s %%(name)s - %%(message)s",
        "console_format": "%%(levelname)s %%(message)s",
        "logs_dir": "logs",
        "archive_days_keep": "30",
        "masking_enabled": "true",
        "max_bytes": "10485760",
        "queue_enabled": "true",
        "queue_size": "100",
        "flush_interval": "0.1",
    }

    if os.path.exists(config_file):
        try:
            config.read(config_file)
            print(f"Configuration loaded from {config_file}")
        except Exception as e:
            print(f"Warning: Could not parse {config_file}: {e}")
            print("   Using default configuration")
    else:
        print(f"Configuration file {config_file} not found, using defaults")

    return config


def get_log_level_from_config(config: configparser.ConfigParser) -> int:
    """Convert log level string from config to logging constant."""
    level_str = config.get("logging", "level", fallback="INFO").upper()

    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    return level_map.get(level_str, logging.INFO)


def get_logger(
    name: Optional[str] = None,
    level: Optional[int] = None,
    config_file: str = "log_config.ini",
) -> logging.Logger:
    """Create a logger instance with Rich logging output and configuration support."""
    config = load_config(config_file)

    if name is None:
        name = config.get("app", "name", fallback="app_logger")

    if level is None:
        level = get_log_level_from_config(config)

    console = Console()

    log_format = config.get("logging", "format", fallback="%(message)s")
    if log_format != "%(message)s":
        log_format = log_format.replace("%%", "%")

    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=level,
            format=log_format,
            datefmt="[%X]",
            handlers=[RichHandler(console=console)],
        )

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(RichHandler(console=console))

    return logger


def get_logger_with_queue(
    name: Optional[str] = None,
    level: Optional[int] = None,
    config_file: str = "log_config.ini",
) -> logging.Logger:
    """Create a thread-safe logger with queue-based logging."""
    config = load_config(config_file)

    if name is None:
        name = config.get("app", "name", fallback="app_logger")

    if level is None:
        level = get_log_level_from_config(config)

    queue_enabled = (
        config.get("logging", "queue_enabled", fallback="true").lower() == "true"
    )

    if not queue_enabled:
        return get_logger(name, level, config_file)

    queue_size = int(config.get("logging", "queue_size", fallback="1000"))
    flush_interval = float(config.get("logging", "flush_interval", fallback="1.0"))

    console = Console()

    log_format = config.get("logging", "format", fallback="%(message)s")
    if log_format != "%(message)s":
        log_format = log_format.replace("%%", "%")

    queue_handler = ThreadSafeQueueHandler(
        queue_size=queue_size, flush_interval=flush_interval
    )

    rich_handler = RichHandler(console=console)
    rich_handler.setFormatter(logging.Formatter(log_format))
    queue_handler.add_handler(rich_handler)

    logger = logging.getLogger(f"{name}_queued")
    logger.setLevel(level)
    logger.propagate = False

    logger.addHandler(queue_handler)

    return logger


def get_logger_with_queue_and_file(
    name: Optional[str] = None,
    level: Optional[int] = None,
    log_file: Optional[str] = None,
    config_file: str = "log_config.ini",
) -> logging.Logger:
    """Create a thread-safe logger with both queue processing and file output with rotation."""
    config = load_config(config_file)

    if name is None:
        name = config.get("app", "name", fallback="app_logger")

    if level is None:
        level = get_log_level_from_config(config)

    queue_enabled = (
        config.get("logging", "queue_enabled", fallback="true").lower() == "true"
    )

    if not queue_enabled:
        return get_logger_with_file_handler(name, level, log_file, config_file)

    queue_size = int(config.get("logging", "queue_size", fallback="1000"))
    flush_interval = float(config.get("logging", "flush_interval", fallback="1.0"))

    console = Console()

    log_format = config.get("logging", "format", fallback="%(message)s")
    if log_format != "%(message)s":
        log_format = log_format.replace("%%", "%")

    queue_handler = ThreadSafeQueueHandler(
        queue_size=queue_size, flush_interval=flush_interval
    )

    rich_handler = RichHandler(console=console)
    rich_handler.setFormatter(logging.Formatter(log_format))
    queue_handler.add_handler(rich_handler)

    if log_file is None:
        logs_dir = config.get("logging", "logs_dir", fallback="logs")
        if not os.path.exists(logs_dir):
            try:
                os.makedirs(logs_dir, exist_ok=True)
            except Exception as e:
                print(f"Warning: Could not create logs directory {logs_dir}: {e}")

    if log_file is None:
        log_file = os.path.join(logs_dir, f"{name or 'app'}.log")

    try:
        max_bytes = int(config.get("logging", "max_bytes", fallback="10485760"))

        file_handler = WindowsSafeRotatingFileHandler(
            log_file, maxBytes=max_bytes, encoding="utf-8", delay=False
        )
        file_handler.setLevel(level)

        file_format = config.get(
            "logging",
            "format",
            fallback="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        if file_format != "%(asctime)s - %(name)s - %(levelname)s - %(message)s":
            file_format = file_format.replace("%%", "%")
            file_format = "%(asctime)s - " + file_format
        formatter = logging.Formatter(file_format)
        file_handler.setFormatter(formatter)

        queue_handler.add_handler(file_handler)

        print(f"Queue logging with file rotation enabled: {log_file}")

    except Exception as e:
        print(f"Warning: Could not add file handler to queue: {e}")

    logger = logging.getLogger(f"{name}_queued_file")
    logger.setLevel(level)
    logger.propagate = False

    logger.addHandler(queue_handler)

    # Add file_handler attribute to logger for cleanup purposes
    if "file_handler" in locals():
        setattr(logger, "file_handler", file_handler)

    return logger


def get_logger_with_file_handler(
    name: Optional[str] = None,
    level: Optional[int] = None,
    log_file: Optional[str] = None,
    config_file: str = "log_config.ini",
) -> logging.Logger:
    """Create a logger with both console and file output."""
    config = load_config(config_file)

    file_logger = logging.getLogger(f"{name or 'app'}_file")
    file_logger.setLevel(level or get_log_level_from_config(config))
    file_logger.propagate = False

    if log_file is None:
        logs_dir = config.get("logging", "logs_dir", fallback="logs")
        if not os.path.exists(logs_dir):
            try:
                os.makedirs(logs_dir, exist_ok=True)
            except Exception as e:
                print(f"Warning: Could not create logs directory {logs_dir}: {e}")
                return get_logger(name, level, config_file)

        log_file = os.path.join(logs_dir, f"{name or 'app'}.log")

    try:
        max_bytes = int(config.get("logging", "max_bytes", fallback="10485760"))

        file_handler = WindowsSafeRotatingFileHandler(
            log_file, maxBytes=max_bytes, encoding="utf-8", delay=False
        )
        file_handler.setLevel(level or get_log_level_from_config(config))

        file_format = config.get(
            "logging",
            "format",
            fallback="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        if file_format != "%(asctime)s - %(name)s - %(levelname)s - %(message)s":
            file_format = file_format.replace("%%", "%")
            file_format = "%(asctime)s - " + file_format
        formatter = logging.Formatter(file_format)
        file_handler.setFormatter(formatter)

        file_logger.addHandler(file_handler)

        combined_logger = logging.getLogger(f"{name or 'app'}_combined")
        combined_logger.setLevel(level or get_log_level_from_config(config))
        combined_logger.propagate = False

        console_logger = get_logger(name, level, config_file)

        combined_logger.addHandler(file_handler)

        for handler in console_logger.handlers:
            if isinstance(handler, RichHandler):
                combined_logger.addHandler(handler)
                break

        print(f"File logging enabled: {log_file}")

        # Add file_handler attribute to logger for cleanup purposes
        setattr(combined_logger, "file_handler", file_handler)

        return combined_logger

    except Exception as e:
        print(f"Warning: Could not add file handler: {e}")
        return get_logger(name, level, config_file)


def cleanup_loggers():
    """Clean up all loggers and close file handlers."""
    try:
        # Get all loggers more safely by using a different approach
        loggers = []
        # Try to get loggers by name if we know them
        known_logger_names = [
            "powerlogger",
            "powerlogger_queued",
            "powerlogger_queued_file",
            "powerlogger_file",
            "powerlogger_combined",
            "app_logger",
        ]

        for name in known_logger_names:
            try:
                logger = logging.getLogger(name)
                if logger is not None and logger.handlers:
                    loggers.append(logger)
            except (ValueError, TypeError) as e:
                # Log specific exceptions that might occur when getting loggers
                print(f"Warning: Could not get logger '{name}': {e}")
                continue

        for logger in loggers:
            for handler in logger.handlers[:]:
                try:
                    if hasattr(handler, "close"):
                        handler.close()
                    logger.removeHandler(handler)
                except Exception as e:
                    print(f"Warning: Could not close handler {handler}: {e}")

            # Check for file_handler attribute using getattr
            if hasattr(logger, "file_handler"):
                try:
                    file_handler = getattr(logger, "file_handler")
                    if hasattr(file_handler, "close"):
                        file_handler.close()
                except Exception as e:
                    print(f"Warning: Could not close file handler: {e}")
    except Exception as e:
        print(f"Warning: Could not access logger manager: {e}")

    for handler in logging.root.handlers[:]:
        try:
            handler.close()
            logging.root.removeHandler(handler)
        except Exception as e:
            print(f"Warning: Could not close root handler: {e}")

    print("All loggers cleaned up successfully")
