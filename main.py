# import cv2
# import tkinter as tk
# from tkinter import ttk, messagebox
# import PIL.Image, PIL.ImageTk
# from datetime import datetime
# import os

# class FaceDetectionApp:
#     def __init__(self, window):
#         self.window = window
#         self.window.title("Face Detection System")
#         self.window.geometry("800x600")

#         # Initialize video capture
#         self.cap = cv2.VideoCapture(0)
#         if not self.cap.isOpened():
#             messagebox.showerror("Error", "Cannot open webcam")
#             self.window.quit()

#         # Load the face cascade classifier
#         self.face_cascade = cv2.CascadeClassifier(
#             cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
#         )

#         # Create GUI elements
#         self.create_gui()

#         # Initialize variables
#         self.is_detecting = False
#         self.show_landmarks = False
#         self.photo = None
#         self.detected_faces = 0

#     def create_gui(self):
#         # Create main frame
#         self.main_frame = ttk.Frame(self.window, padding="10")
#         self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

#         # Video frame
#         self.video_frame = ttk.Frame(self.main_frame)
#         self.video_frame.grid(row=0, column=0, columnspan=2, pady=10)

#         self.video_label = ttk.Label(self.video_frame)
#         self.video_label.pack()

#         # Control buttons frame
#         self.control_frame = ttk.Frame(self.main_frame)
#         self.control_frame.grid(row=1, column=0, columnspan=2, pady=10)

#         # Start/Stop button
#         self.toggle_button = ttk.Button(
#             self.control_frame, 
#             text="Start Detection", 
#             command=self.toggle_detection
#         )
#         self.toggle_button.grid(row=0, column=0, padx=5)

#         # Screenshot button
#         self.screenshot_button = ttk.Button(
#             self.control_frame, 
#             text="Take Screenshot", 
#             command=self.take_screenshot
#         )
#         self.screenshot_button.grid(row=0, column=1, padx=5)

#         # Settings frame
#         self.settings_frame = ttk.LabelFrame(self.main_frame, text="Settings", padding="10")
#         self.settings_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

#         # Scale factor setting
#         ttk.Label(self.settings_frame, text="Scale Factor:").grid(row=0, column=0, padx=5)
#         self.scale_factor = tk.DoubleVar(value=1.1)
#         self.scale_factor_entry = ttk.Entry(
#             self.settings_frame, 
#             textvariable=self.scale_factor, 
#             width=10
#         )
#         self.scale_factor_entry.grid(row=0, column=1, padx=5)

#         # Min neighbors setting
#         ttk.Label(self.settings_frame, text="Min Neighbors:").grid(row=0, column=2, padx=5)
#         self.min_neighbors = tk.IntVar(value=5)
#         self.min_neighbors_entry = ttk.Entry(
#             self.settings_frame, 
#             textvariable=self.min_neighbors, 
#             width=10
#         )
#         self.min_neighbors_entry.grid(row=0, column=3, padx=5)

#         # Status frame
#         self.status_frame = ttk.LabelFrame(self.main_frame, text="Status", padding="10")
#         self.status_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

#         self.status_label = ttk.Label(self.status_frame, text="Detection Stopped")
#         self.status_label.pack()

#         self.faces_label = ttk.Label(self.status_frame, text="Faces Detected: 0")
#         self.faces_label.pack()

#     def toggle_detection(self):
#         self.is_detecting = not self.is_detecting
#         if self.is_detecting:
#             self.toggle_button.configure(text="Stop Detection")
#             self.status_label.configure(text="Detection Running")
#             self.update_frame()
#         else:
#             self.toggle_button.configure(text="Start Detection")
#             self.status_label.configure(text="Detection Stopped")

#     def detect_faces(self, frame):
#         # Convert frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect faces
#         faces = self.face_cascade.detectMultiScale(
#             gray,
#             scaleFactor=self.scale_factor.get(),
#             minNeighbors=self.min_neighbors.get(),
#             minSize=(30, 30)
#         )

#         # Update faces count
#         self.detected_faces = len(faces)
#         self.faces_label.configure(text=f"Faces Detected: {self.detected_faces}")

#         # Draw rectangle around faces
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#         return frame

#     def update_frame(self):
#         if self.is_detecting:
#             # Read frame from camera
#             ret, frame = self.cap.read()
#             if ret:
#                 # Flip frame horizontally for mirror effect
#                 frame = cv2.flip(frame, 1)

#                 if self.is_detecting:
#                     frame = self.detect_faces(frame)

#                 # Convert frame to PhotoImage
#                 frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame_rgb))
#                 self.video_label.configure(image=self.photo)

#             # Schedule next update
#             self.window.after(10, self.update_frame)

#     def take_screenshot(self):
#         if self.photo:
#             # Create screenshots directory if it doesn't exist
#             if not os.path.exists("screenshots"):
#                 os.makedirs("screenshots")

#             # Save screenshot with timestamp
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             filename = f"screenshots/face_detection_{timestamp}.png"
            
#             # Get the current frame
#             ret, frame = self.cap.read()
#             if ret:
#                 frame = cv2.flip(frame, 1)
#                 if self.is_detecting:
#                     frame = self.detect_faces(frame)
#                 cv2.imwrite(filename, frame)
#                 messagebox.showinfo("Success", f"Screenshot saved as {filename}")
#             else:
#                 messagebox.showerror("Error", "Failed to capture screenshot")

#     def cleanup(self):
#         if self.cap.isOpened():
#             self.cap.release()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FaceDetectionApp(root)
#     root.protocol("WM_DELETE_WINDOW", lambda: (app.cleanup(), root.destroy()))
#     root.mainloop()


import cv2
import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import PIL.Image, PIL.ImageTk
from datetime import datetime
import os
import time
from threading import Thread
from queue import Queue

class FaceDetectionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Face Detection System")
        self.window.geometry("1200x800")

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Cannot open webcam")
            self.window.quit()

        # Initialize detectors
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_eye.xml'
        )
        self.smile_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_smile.xml'
        )

        # Initialize variables
        self.is_detecting = False
        self.show_eyes = False
        self.show_smile = False
        self.record_video = False
        self.photo = None
        self.detected_faces = 0
        self.rectangle_color = (0, 255, 0)
        self.video_writer = None
        self.recording_started = None
        self.fps_counter = FPSCounter()
        
        # Processing queue
        self.frame_queue = Queue(maxsize=2)
        self.result_queue = Queue(maxsize=2)
        
        # Create GUI elements
        self.create_gui()
        
        # Start processing thread
        self.processing_thread = Thread(target=self.process_frame_thread, daemon=True)
        self.processing_thread.start()

    def create_gui(self):
        # Create main frame
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create left and right frames
        left_frame = ttk.Frame(self.main_frame)
        left_frame.grid(row=0, column=0, padx=10)
        
        right_frame = ttk.Frame(self.main_frame)
        right_frame.grid(row=0, column=1, padx=10)

        # Video frame (left side)
        self.video_frame = ttk.Frame(left_frame)
        self.video_frame.pack(pady=10)

        self.video_label = ttk.Label(self.video_frame)
        self.video_label.pack()

        # Create control panel
        self.create_control_panel(right_frame)

    def create_control_panel(self, parent):
        # Detection Controls
        controls_frame = ttk.LabelFrame(parent, text="Controls", padding="10")
        controls_frame.pack(fill=tk.X, pady=5)

        # Start/Stop button
        self.toggle_button = ttk.Button(
            controls_frame, 
            text="Start Detection",
            command=self.toggle_detection
        )
        self.toggle_button.pack(fill=tk.X, pady=2)

        # Feature toggles
        self.create_feature_toggles(controls_frame)

        # Settings
        self.create_settings_panel(parent)

        # Recording controls
        self.create_recording_controls(parent)

        # Statistics
        self.create_statistics_panel(parent)

    def create_feature_toggles(self, parent):
        # Eye detection toggle
        self.eyes_var = tk.BooleanVar()
        ttk.Checkbutton(
            parent,
            text="Detect Eyes",
            variable=self.eyes_var,
            command=lambda: setattr(self, 'show_eyes', self.eyes_var.get())
        ).pack(fill=tk.X)

        # Smile detection toggle
        self.smile_var = tk.BooleanVar()
        ttk.Checkbutton(
            parent,
            text="Detect Smile",
            variable=self.smile_var,
            command=lambda: setattr(self, 'show_smile', self.smile_var.get())
        ).pack(fill=tk.X)

    def create_settings_panel(self, parent):
        settings_frame = ttk.LabelFrame(parent, text="Detection Settings", padding="10")
        settings_frame.pack(fill=tk.X, pady=5)

        # Scale factor setting
        ttk.Label(settings_frame, text="Scale Factor:").pack()
        self.scale_factor = tk.DoubleVar(value=1.1)
        ttk.Scale(
            settings_frame,
            from_=1.1,
            to=2.0,
            variable=self.scale_factor,
            orient=tk.HORIZONTAL
        ).pack(fill=tk.X)

        # Min neighbors setting
        ttk.Label(settings_frame, text="Min Neighbors:").pack()
        self.min_neighbors = tk.IntVar(value=5)
        ttk.Scale(
            settings_frame,
            from_=1,
            to=10,
            variable=self.min_neighbors,
            orient=tk.HORIZONTAL
        ).pack(fill=tk.X)

        # Color picker
        ttk.Button(
            settings_frame,
            text="Choose Rectangle Color",
            command=self.choose_color
        ).pack(fill=tk.X, pady=5)

    def create_recording_controls(self, parent):
        recording_frame = ttk.LabelFrame(parent, text="Recording", padding="10")
        recording_frame.pack(fill=tk.X, pady=5)

        # Screenshot button
        ttk.Button(
            recording_frame,
            text="Take Screenshot",
            command=self.take_screenshot
        ).pack(fill=tk.X, pady=2)

        # Record video button
        self.record_button = ttk.Button(
            recording_frame,
            text="Start Recording",
            command=self.toggle_recording
        )
        self.record_button.pack(fill=tk.X, pady=2)

        # Recording duration label
        self.recording_label = ttk.Label(recording_frame, text="")
        self.recording_label.pack()

    def create_statistics_panel(self, parent):
        stats_frame = ttk.LabelFrame(parent, text="Statistics", padding="10")
        stats_frame.pack(fill=tk.X, pady=5)

        self.faces_label = ttk.Label(stats_frame, text="Faces Detected: 0")
        self.faces_label.pack()

        self.fps_label = ttk.Label(stats_frame, text="FPS: 0")
        self.fps_label.pack()

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Rectangle Color")
        if color[0]:
            self.rectangle_color = tuple(int(x) for x in color[0])

    def process_frame_thread(self):
        while True:
            if not self.frame_queue.empty():
                frame = self.frame_queue.get()
                processed_frame = self.process_frame(frame)
                if self.result_queue.full():
                    self.result_queue.get()
                self.result_queue.put(processed_frame)

    def process_frame(self, frame):
        if not self.is_detecting:
            return frame

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=self.scale_factor.get(),
            minNeighbors=self.min_neighbors.get(),
            minSize=(30, 30)
        )

        self.detected_faces = len(faces)

        # Process each face
        for (x, y, w, h) in faces:
            # Draw face rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), self.rectangle_color, 2)

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Detect eyes
            if self.show_eyes:
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

            # Detect smile
            if self.show_smile:
                smiles = self.smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

        return frame

    def update_frame(self):
        if self.is_detecting:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                
                # Put frame in processing queue
                if not self.frame_queue.full():
                    self.frame_queue.put(frame)

                # Get processed frame if available
                if not self.result_queue.empty():
                    processed_frame = self.result_queue.get()
                    
                    # Save frame if recording
                    if self.record_video and self.video_writer:
                        self.video_writer.write(processed_frame)

                    # Update GUI
                    frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                    self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame_rgb))
                    self.video_label.configure(image=self.photo)
                    
                    # Update statistics
                    self.faces_label.configure(text=f"Faces Detected: {self.detected_faces}")
                    fps = self.fps_counter.update()
                    self.fps_label.configure(text=f"FPS: {fps:.1f}")

            # Schedule next update
            self.window.after(10, self.update_frame)

    def toggle_detection(self):
        self.is_detecting = not self.is_detecting
        if self.is_detecting:
            self.toggle_button.configure(text="Stop Detection")
            self.update_frame()
        else:
            self.toggle_button.configure(text="Start Detection")

    def toggle_recording(self):
        self.record_video = not self.record_video
        if self.record_video:
            # Initialize video writer
            if not os.path.exists("recordings"):
                os.makedirs("recordings")
                
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recordings/face_detection_{timestamp}.avi"
            
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video_writer = cv2.VideoWriter(
                filename,
                fourcc,
                20.0,
                (640, 480)
            )
            self.recording_started = time.time()
            self.record_button.configure(text="Stop Recording")
            self.update_recording_duration()
        else:
            if self.video_writer:
                self.video_writer.release()
                self.video_writer = None
            self.record_button.configure(text="Start Recording")
            self.recording_label.configure(text="")

    def update_recording_duration(self):
        if self.record_video and self.recording_started:
            duration = int(time.time() - self.recording_started)
            minutes = duration // 60
            seconds = duration % 60
            self.recording_label.configure(text=f"Recording: {minutes:02d}:{seconds:02d}")
            self.window.after(1000, self.update_recording_duration)

    def take_screenshot(self):
        if self.photo:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/face_detection_{timestamp}.png"
            
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                processed_frame = self.process_frame(frame)
                cv2.imwrite(filename, processed_frame)
                messagebox.showinfo("Success", f"Screenshot saved as {filename}")
            else:
                messagebox.showerror("Error", "Failed to capture screenshot")

    def cleanup(self):
        if self.video_writer:
            self.video_writer.release()
        if self.cap.isOpened():
            self.cap.release()

class FPSCounter:
    def __init__(self):
        self.fps = 0
        self.frame_count = 0
        self.start_time = time.time()
    
    def update(self):
        self.frame_count += 1
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 1:
            self.fps = self.frame_count / elapsed_time
            self.frame_count = 0
            self.start_time = time.time()
        return self.fps

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
    
    # Configure window resize behavior
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    # Add keyboard shortcuts
    root.bind('<space>', lambda e: app.toggle_detection())
    root.bind('<s>', lambda e: app.take_screenshot())
    root.bind('<r>', lambda e: app.toggle_recording())
    root.bind('<Escape>', lambda e: root.quit())
    
    # Set up proper window closing
    root.protocol("WM_DELETE_WINDOW", lambda: (app.cleanup(), root.destroy()))
    
    root.mainloop()