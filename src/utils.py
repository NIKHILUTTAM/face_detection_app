# src/utils.py
import logging
import traceback
from functools import wraps
from typing import Callable, Any

class FaceDetectionError(Exception):
    """Custom exception for face detection errors"""
    pass

def handle_errors(func: Callable) -> Callable:
    """
    Decorator for handling errors in face detection operations.
    
    Args:
        func: Function to wrap
        
    Returns:
        Wrapped function with error handling
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            logging.debug(traceback.format_exc())
            raise FaceDetectionError(f"Operation failed: {str(e)}")
    return wrapper

def validate_image(func: Callable) -> Callable:
    """
    Decorator to validate image input.
    
    Args:
        func: Function to wrap
        
    Returns:
        Wrapped function with input validation
    """
    @wraps(func)
    def wrapper(self, image, *args, **kwargs):
        if image is None:
            raise ValueError("Invalid image input: Image is None")
        if len(image.shape) < 2:
            raise ValueError("Invalid image input: Incorrect dimensions")
        return func(self, image, *args, **kwargs)
    return wrapper