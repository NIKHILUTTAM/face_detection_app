# tests/conftest.py
import pytest
import os
import sys

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(autouse=True)
def setup_test_env():
    """Setup any state specific to the execution of tests."""
    # Use os.path.join for cross-platform compatibility
    output_dir = os.path.join('data', 'output')
    test_images_dir = os.path.join('data', 'test_images')
    models_dir = 'models'

    # Create directories if they don't exist
    for directory in [output_dir, test_images_dir, models_dir]:
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            print(f"Warning: Could not create directory {directory}: {e}")
            
    # Download the Haar cascade file if it doesn't exist
    haar_cascade_path = os.path.join('models', 'haarcascade_frontalface_default.xml')
    if not os.path.exists(haar_cascade_path):
        try:
            url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
            import urllib.request
            urllib.request.urlretrieve(url, haar_cascade_path)
        except Exception as e:
            print(f"Warning: Could not download cascade file: {e}")