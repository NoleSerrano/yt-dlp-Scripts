import os
import subprocess
import shutil
import sys

def get_frame_rate(file_path):
    """Get the frame rate of a video file using ffprobe."""
    try:
        cmd = [
            'ffprobe', '-v', 'error', '-select_streams', 'v:0',
            '-show_entries', 'stream=avg_frame_rate', '-of', 'default=noprint_wrappers=1:nokey=1',
            file_path
        ]
        fps = subprocess.check_output(cmd).decode('utf-8').strip()
        return eval(fps).as_integer_ratio()  # Convert the fps to a fraction
    except subprocess.CalledProcessError as e:
        print(f"Error processing file {file_path}: {e}")
        return None

def move_file_to_folder(file_path, folder):
    """Move a file to a specified folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    shutil.move(file_path, folder)

def organize_videos_by_frame_rate(folder_path):
    """Organize video files in a folder by their frame rate."""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            frame_rate = get_frame_rate(file_path)
            if frame_rate:
                # Convert the frame rate to a string format like '24_1' for 24fps
                fps_folder = f"{frame_rate[0]}_{frame_rate[1]}"
                fps_folder_path = os.path.join(folder_path, fps_folder)
                move_file_to_folder(file_path, fps_folder_path)
                print(f"Moved {file_name} to {fps_folder_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Usage: python script.py <path_to_folder>")
            sys.exit(1)

    folder_path = sys.argv[1]
    organize_videos_by_frame_rate(folder_path)