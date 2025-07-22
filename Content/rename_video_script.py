import os
import re


def rename_videos(video_folder, text_file):
    with open(text_file, 'r') as file:
        lines = file.readlines()

        instructions = []
        for line in lines:
            match = re.match(r'(.+?)\s+x(\d+)', line.strip(), re.IGNORECASE)
            if match:
                label = match.group(1).strip().upper()
                count = int(match.group(2))
                instructions.append((label, count))

        # List and sort all files in the folder (assuming only videos are there)
        video_files = sorted(
            [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]
        )

        video_index = 0
        for label, count in instructions:
            for i in range(1, count + 1):
                if video_index >= len(video_files):
                    print(f"❗ Not enough video files for instruction: {label} x{count}")
                    return
                old_name = video_files[video_index]
                ext = os.path.splitext(old_name)[1]
                new_name = f"{label}_{i}{ext}"
                old_path = os.path.join(video_folder, old_name)
                new_path = os.path.join(video_folder, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} ➜ {new_name}")
                video_index += 1

        if video_index < len(video_files):
            print(f"⚠️ {len(video_files) - video_index} unused video files remaining.")

video_folder_path = "/Volumes/T7 Shield/Speed Solutions/Day 3"
text_file_path = "/Users/leomorgan/Documents/Day3Exercises.txt"
video_folder_new = "/Volumes/T7 Shield/Speed Solutions/NAMED"

rename_videos(video_folder_path, text_file_path)

