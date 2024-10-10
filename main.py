import os
import time
import typer
import rich

CURRENT_USER = os.getlogin()
PATH_TO_GAME = f"C:\\Users\\{CURRENT_USER}\\AppData\\Local\\osu!\\Songs" # Assumes that the osu folder is in the default installation location

def nuke(path): # Function that deletes all the beatmap backgrounds in the specified song folder
    beatmaps = []
    deletion_counter = 0 # Keeps track of the number of deleted maps

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
                deletion_counter += 1
                print("Background deleted.")

    rich.print("\n\n[bold green]Deleted all map backgrounds![/bold green]\n")
    rich.print(f"[green]Total deleted backgrounds: {deletion_counter}[/green]")

def main(path: str = PATH_TO_GAME): # Main function
    rich.print(f"[blue]Target folder: {path}\n[/blue]")

    if not os.path.isdir(path): # Throws an error if the path is invalid
        rich.print(f"[bold red]{path} is not a valid folder. Exiting...[/bold red]")
        raise typer.Exit()

    rich.print("Enter [bold green]'CONFIRM'[/bold green] to delete all of your beatmap backgrounds: ")
    confirm = input()

    if confirm == "CONFIRM":
            nuke(path)

    else:
        rich.print("[bold red]Exiting...[/bold red]")
        raise typer.Exit()

if __name__ == "__main__":
    typer.run(main)




