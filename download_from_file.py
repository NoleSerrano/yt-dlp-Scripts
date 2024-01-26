import subprocess
import os
import socket
import sys
import requests

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except requests.RequestException as e:
        print(f"Unable to retrieve public IP address: {e}")
        return None

def download_videos(input_file, ip_address):
    print(f"Your IP address is: {ip_address}")

    confirm = input("Are you sure you want to continue? (y/n): ").lower()
    if confirm != 'y':
        print("Download canceled.")
        return

    input_directory = os.path.dirname(input_file)
    subprocess.run(['yt-dlp', '--batch-file', input_file, '-o', os.path.join(input_directory, '%(title)s.%(ext)s')])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    public_ip = get_public_ip()
    if public_ip:
        download_videos(input_file, public_ip)