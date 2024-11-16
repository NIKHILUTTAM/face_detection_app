# src/image_processor.py
import cv2
import numpy as np
from typing import Tuple, Optional
import logging

class ImageProcessor:
    @staticmethod
    def resize_image(image: np.ndarray, width: Optional[int] = None, height: Optional[int] = None) -> np.ndarray:
        """
        Resize image maintaining aspect ratio.
        
        Args:
            image: Input image
            width: Desired width
            height: Desired height
            
        Returns:
            Resized image
        """
        dims = None
        (h, w) = image.shape[:2]
        
        if width is None and height is None:
            return image
            
        if width is None:
            r = height / float(h)
            dims = (int(w * r), height)
        else:
            r = width / float(w)
            dims = (width, int(h * r))
            
        return cv2.resize(image, dims, interpolation=cv2.INTER_AREA)
    
    @staticmethod
    def adjust_brightness_contrast(image: np.ndarray, brightness: float = 1.0, contrast: float = 1.0) -> np.ndarray:
        """
        Adjust image brightness and contrast.
        
        Args:
            image: Input image
            brightness: Brightness factor (1.0 is original)
            contrast: Contrast factor (1.0 is original)
            
        Returns:
            Adjusted image
        """
        try:
            adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
            return adjusted
        except Exception as e:
            logging.error(f"Error adjusting brightness/contrast: {str(e)}")
            return image
    
    @staticmethod
    def save_image(image: np.ndarray, filepath: str) -> bool:
        """
        Save image to file.
        
        Args:
            image: Image to save
            filepath: Output file path
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            return cv2.imwrite(filepath, image)
        except Exception as e:
            logging.error(f"Error saving image: {str(e)}")
            return False