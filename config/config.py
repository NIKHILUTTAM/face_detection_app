# config/config.py
import os
from dataclasses import dataclass

@dataclass
class Config:
    # Paths
    MODEL_PATH = os.path.join('models', 'haarcascade_frontalface_default.xml')
    OUTPUT_DIR = os.path.join('data', 'output')
    TEST_IMAGES_DIR = os.path.join('data', 'test_images')
    
    # Face Detection Parameters
    SCALE_FACTOR = 1.1
    MIN_NEIGHBORS = 5
    MIN_FACE_SIZE = (30, 30)
    
    # Video Capture Settings
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480
    
    # Image Processing
    DEFAULT_OUTPUT_WIDTH = 800
    JPEG_QUALITY = 95
    
    # Logging Configuration
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE = 'face_detection.log'
    LOG_LEVEL = 'INFO'

# Initialize logging
import logging

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format=Config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()
        ]
    )