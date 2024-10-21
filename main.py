import os
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def delete_all_beatmaps(path_to_game):
    if not os.path.exists(path_to_game):
        messagebox.showerror("Error", "Invalid path. Please check and try again.")
        return
    normalized_path = os.path.normpath(path_to_game)
    components = normalized_path.split(os.sep)

    if not (len(components) >= 2 and components[-2].lower() == 'osu!' and components[-1].lower() == 'songs'):
        messagebox.showerror("Error",
                             "The selected folder is not a valid osu! Songs folder. Please select the correct folder.")
        return

    song_folder_files = os.listdir(path_to_game)
    beatmaps = []



    for file in song_folder_files:
        # Pushes all the song folders to the "beatmaps" list
        if os.path.isdir(os.path.join(path_to_game, file)):
            beatmaps.append(file)

    for beatmap in beatmaps:
        beatmap_path = os.path.join(path_to_game, beatmap)
        file_list = os.listdir(beatmap_path)
        for file in file_list:
            # Checks for the file extensions and deletes the files accordingly
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".mp4"):
                os.remove(os.path.join(beatmap_path, file))

    messagebox.showinfo("Success", "Deleted all map backgrounds!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)

def start_deletion():
    confirm = messagebox.askquestion("Confirm", "Are you sure you want to delete all of your beatmap backgrounds?")
    if confirm == 'yes':
        delete_all_beatmaps(path_entry.get())

root = tk.Tk()
root.title("Osu Background Nuker")
root.geometry("300x300")

background_image = tk.PhotoImage(file=resource_path("background.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
root.resizable(False, False)


path_label = tk.Label(root, text="Path to osu! Songs folder:", bg="white", fg="black")
path_label.pack(pady=10)

path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Beatmap Backgrounds", command=start_deletion, bg="white", fg="black")
delete_button.pack(pady=20)

root.mainloop()