import subprocess
import os
import sys
import shutil

# Used for downloading but also updates the time so it's hidden behind older files
# Example: python download.py https://www.youtube.com/watch?v=pIZ0QRWK0zg ba[ext=m4a]

def download_and_touch(url, format_code, output_folder=os.path.join(os.path.expanduser('~'), 'Downloads')):
    # Run yt-dlp to download the file
    result = subprocess.run(['yt-dlp', '-f', format_code, url], capture_output=True, text=True)

    if result.returncode != 0:
        print("Error downloading file:", result.stderr)
        return

    # Extracting filename from output
    lines = result.stdout.split('\n')
    filename_line = [line for line in lines if 'Destination:' in line]

    if not filename_line:
        print("Could not find filename in yt-dlp output.")
        return

    filename = filename_line[0].split('Destination: ')[-1].strip()

    # Update the timestamp of the file
    os.utime(filename, None)

    shutil.move(filename, output_folder)

if __name__ == '__main__':
    if len(sys.argv) < 3:

        # use defaults
        url = "https://www.youtube.com/watch?v=pIZ0QRWK0zg"
        format_code = "ba[ext=m4a]"
        download_and_touch(url, format_code)
    else:
        download_and_touch(sys.argv[1], sys.argv[2])
