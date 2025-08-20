#!/usr/bin/env python3
"""
Test logging with special characters, emojis, and international text
"""

from powerlogger import get_logger_with_file_handler

# Create logger with file output
logger = get_logger_with_file_handler("test_logging")


def test_logging():
    """Test logging with special characters and emojis."""
    print("🚀 Rich Logger - Logging Test")
    print("=" * 50)

    # Test with emojis
    logger.info("✅ Success message with emoji")
    logger.warning("⚠️  Warning message with emoji")
    logger.error("❌ Error message with emoji")
    logger.debug("🔍 Debug message with emoji")

    # Test with special characters
    logger.info("Special characters: á é í ó ú ñ ç")
    logger.warning("Currency symbols: € £ ¥ $ ₹ ₽")
    logger.error("Mathematical symbols: ± × ÷ √ ∞ ≠ ≤ ≥")

    # Test with international text
    logger.info("English: Hello World")
    logger.warning("Spanish: ¡Hola Mundo!")
    logger.error("French: Bonjour le Monde!")
    logger.debug("German: Hallo Welt!")

    # Test with complex Unicode
    logger.info("Complex Unicode: 🚀🌟💻🎯📊🔧⚡🎨✨")
    logger.warning("Mixed content: Hello 世界 🌍 2024 © ® ™")

    print("\n" + "=" * 50)
    print("✅ Logging test completed! Check logs/test_logging.log for results.")
    print("📁 File should contain all special characters and emojis correctly.")


if __name__ == "__main__":
    test_logging()
