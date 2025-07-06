import cv2

def resize_frame(frame, width=640, height=480):
    return cv2.resize(frame, (width, height))

def log_message(message):
    print(message)

def save_output_video(video_path, fourcc, fps, frame_size):
    return cv2.VideoWriter(video_path, fourcc, fps, frame_size)