import cv2
from PIL import Image

def extract_frames(video_path, skip_seconds=2):
    """
    Extracts frames from a video file every 'skip_seconds'.
    """
    video = cv2.VideoCapture(video_path)
    frames = []
    timestamps = []
    
    # Get the frame rate (frames per second)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    # Calculate how many frames to skip (e.g. 60fps * 2s = 120 frames)
    frame_skip = fps * skip_seconds
    
    count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break # Stop when video ends
        
        # Only keep the frame if it matches our skip interval
        if count % frame_skip == 0:
            # Convert BGR (OpenCV) to RGB (AI Model standard)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            
            frames.append(pil_image)
            timestamps.append(count / fps) # Save exact time
            
        count += 1
        
    video.release()
    return frames, timestamps