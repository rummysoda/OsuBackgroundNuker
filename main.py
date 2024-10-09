import os
import time

CURRENT_USER = os.getlogin()
PATH_TO_GAME = f"C:\\Users\\{CURRENT_USER}\\AppData\\Local\\osu!\\Songs" # Assumes that the osu folder is in the default installation location
SONG_FOLDER_FILES = os.listdir(PATH_TO_GAME)

beatmaps = []

def delete_all_beatmaps():
    for file in SONG_FOLDER_FILES:
        # Pushes all the song folders to the "beatmaps" list
        if os.path.isdir(file):
            beatmaps.append(file)

    for beatmap in beatmaps:
        os.chdir(PATH_TO_GAME + f"\\{beatmap}")
        file_list = os.listdir()
        for file in file_list:
            # Checks for the file extensions and deletes the files accordingly
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".mp4"):
                print(f"Deleting background for {beatmap}...")
                os.remove(file)
                print("Background deleted.")

    print("Deleted all map backgrounds!")

confirm = input("Enter 'CONFIRM' to delete all of your beatmap backgrounds: ")

if confirm == "CONFIRM":
    delete_all_beatmaps()
else:
    print("Exiting...")
    time.sleep(2)


os.chdir(PATH_TO_GAME)

