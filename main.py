import os
import time
import typer

CURRENT_USER = os.getlogin()
PATH_TO_GAME = f"C:\\Users\\{CURRENT_USER}\\AppData\\Local\\osu!\\Songs" # Assumes that the osu folder is in the default installation location

def nuke(path): # Function that deletes all the beatmap backgrounds in the specified song folder
    beatmaps = []

    os.chdir(path) # Changes directory to the specified path (or default path if no CLI argument has been passed)

    song_folder_files = os.listdir(path)
    for file in song_folder_files:
        # Pushes all the song folders to the "beatmaps" list
        if os.path.isdir(file):
            beatmaps.append(file)

    for beatmap in beatmaps:
        os.chdir(path + f"\\{beatmap}")
        file_list = os.listdir()
        for file in file_list:
            # Checks for the file extensions and deletes the files accordingly
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".mp4"):
                print(f"Deleting background for {beatmap}...")
                os.remove(file)
                print("Background deleted.")

    print("Deleted all map backgrounds!")

def main(path: str = PATH_TO_GAME): # Main function
    print(f"Target folder: {path}\n")
    confirm = input("Enter 'CONFIRM' to delete all of your beatmap backgrounds: ")

    if confirm == "CONFIRM":
        nuke(path)

    else:
        print("Exiting...")
        time.sleep(2)

if __name__ == "__main__":
    typer.run(main)




