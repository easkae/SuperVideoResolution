import cv2
import os

# Specify the output video parameters
output_video_name = 'output_video.mp4'
frame_rate = 25

# Initialize variables to store the dimensions of the first frame
frame_width = None
frame_height = None

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None

# Directory where your PNG frames are stored
frame_dir = './results/swinir_classical_sr_x2'  # Change this to your directory

# Get the list of PNG frame files
frame_files = sorted(os.listdir(frame_dir), key=lambda x: int(x.split('.')[0]))  # Sort numerically

for frame_file in frame_files:
    if frame_file.endswith('.png'):
        frame_path = os.path.join(frame_dir, frame_file)
        frame = cv2.imread(frame_path)

        # Get the dimensions of the first frame and initialize the VideoWriter
        if frame_width is None or frame_height is None:
            frame_height, frame_width, _ = frame.shape
            out = cv2.VideoWriter(output_video_name, fourcc, frame_rate, (frame_width, frame_height))

        # Resize the frame to match the dimensions of the first frame
        frame = cv2.resize(frame, (frame_width, frame_height))

        # Write the frame to the video
        out.write(frame)

# Release the VideoWriter object and clean up
if out is not None:
    out.release()

cv2.destroyAllWindows()