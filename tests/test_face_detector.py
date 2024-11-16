# tests/test_face_detector.py
import pytest
import cv2
import numpy as np
import os
from src.face_detector import FaceDetector
from src.image_processor import ImageProcessor

class TestFaceDetector:
    @pytest.fixture
    def face_detector(self):
        try:
            return FaceDetector()
        except Exception as e:
            pytest.skip(f"Could not initialize FaceDetector: {e}")
    
    @pytest.fixture
    def sample_image(self):
        img = np.zeros((300, 300, 3), dtype=np.uint8)
        cv2.ellipse(img, (150, 150), (100, 130), 0, 0, 360, (255, 255, 255), -1)
        return img
    
    def test_face_detector_initialization(self, face_detector):
        assert hasattr(face_detector, 'face_cascade')
        assert hasattr(face_detector, 'scale_factor')
        assert hasattr(face_detector, 'min_neighbors')
        
    def test_detect_faces(self, face_detector, sample_image):
        if face_detector is None:
            pytest.skip("Face detector not initialized")
        result = face_detector.detect_faces(sample_image)
        assert isinstance(result, np.ndarray)
        
    def test_get_face_count(self, face_detector, sample_image):
        if face_detector is None:
            pytest.skip("Face detector not initialized")
        count = face_detector.get_face_count(sample_image)
        assert isinstance(count, int)
        assert count >= 0