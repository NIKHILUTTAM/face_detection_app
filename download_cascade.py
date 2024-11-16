# download_cascade.py
import os
import urllib.request

def download_haar_cascade():
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Path for the cascade file
    cascade_path = os.path.join('models', 'haarcascade_frontalface_default.xml')
    
    # Download if not exists
    if not os.path.exists(cascade_path):
        print("Downloading Haar Cascade file...")
        url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
        urllib.request.urlretrieve(url, cascade_path)
        print("Download completed!")
    else:
        print("Haar Cascade file already exists!")

if __name__ == "__main__":
    download_haar_cascade()