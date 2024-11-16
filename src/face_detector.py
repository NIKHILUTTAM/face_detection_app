# src/face_detector.py
import cv2
import numpy as np
import os

class FaceDetector:
    def __init__(self):
        # Load the face cascade classifier
        cascade_path = os.path.join('models', 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        # Detection parameters
        self.scale_factor = 1.1
        self.min_neighbors = 5
        self.min_size = (30, 30)
        
    def detect_faces(self, image):
        """
        Detect faces in the input image.
        
        Args:
            image: numpy.ndarray, input image
            
        Returns:
            numpy.ndarray: Image with detected faces marked
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_size
        )
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        return image

    def get_face_count(self, image):
        """
        Get the number of faces detected in the image.
        
        Args:
            image: numpy.ndarray, input image
            
        Returns:
            int: Number of faces detected
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_size
        )
        return len(faces)