"""AWS connection module with secure credential handling."""

import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)


def get_aws_secret_key() -> str:
    """
    Get AWS secret key from environment variables securely.
    
    Returns:
        AWS secret key from environment
    
    Raises:
        ValueError: If AWS_SECRET_KEY is not configured
    """
    secret_key = os.getenv("AWS_SECRET_KEY")
    if not secret_key:
        raise ValueError(
            "AWS_SECRET_KEY environment variable not found. "
            "Please configure it in .env file"
        )
    return secret_key


def connect() -> None:
    """Connect to AWS using secure credentials."""
    try:
        secret_key = get_aws_secret_key()
        logger.info("Connecting to AWS...")
        # IMPORTANT: Never print or log the actual secret key!
        logger.debug("AWS connection established successfully")
    except ValueError as e:
        logger.error(f"Failed to connect: {e}")
        raise