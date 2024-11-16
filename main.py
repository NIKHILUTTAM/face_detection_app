from config.config import Config, setup_logging
from src.face_detector import FaceDetector
from src.video_capture import VideoCapture
from src.image_processor import ImageProcessor
import logging

def main():
    # Setup logging
    setup_logging()
    
    try:
        face_detector = FaceDetector()
        video_capture = VideoCapture()
        
        mode = input("Select mode (0: Webcam, 1: Image): ")
        
        if mode == "0":
            video_capture.start_webcam(face_detector)
        elif mode == "1":
            image_path = input("Enter image path: ")
            image = cv2.imread(image_path)
            if image is not None:
                # Resize image if needed
                image = ImageProcessor.resize_image(
                    image,
                    width=Config.DEFAULT_OUTPUT_WIDTH
                )
                result = face_detector.detect_faces(image)
                cv2.imshow("Result", result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                # Save the result
                output_path = os.path.join(
                    Config.OUTPUT_DIR,
                    f"processed_{os.path.basename(image_path)}"
                )
                ImageProcessor.save_image(result, output_path)
            else:
                logging.error("Could not load image")
                
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        
if __name__ == "__main__":
    main()