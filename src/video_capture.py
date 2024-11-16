# src/video_capture.py
import cv2
import logging
from typing import Optional

class VideoCapture:
    def __init__(self):
        self.cap: Optional[cv2.VideoCapture] = None
        self.frame_width = 640
        self.frame_height = 480
        
    def start_webcam(self, face_detector):
        """
        Start webcam capture and face detection.
        
        Args:
            face_detector: FaceDetector instance for processing frames
        """
        try:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
            
            if not self.cap.isOpened():
                raise ValueError("Could not open webcam")
            
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                    
                # Process frame with face detection
                processed_frame = face_detector.detect_faces(frame)
                
                # Display the number of faces detected
                faces_count = face_detector.get_face_count(frame)
                cv2.putText(
                    processed_frame,
                    f'Faces detected: {faces_count}',
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )
                
                cv2.imshow('Face Detection', processed_frame)
                
                # Break loop on 'q' press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except Exception as e:
            logging.error(f"Error in webcam capture: {str(e)}")
            raise
        finally:
            self.release()
    
    def release(self):
        """Release webcam resources"""
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()