# Osu Background Nuker

Title is self explanatory.

Python script that fetches all of the beatmaps in your Osu! song folder, then deletes all of the background images in order to save space.

The background images are directly deleted, not moved to the recycle bin.

## How to run

### Windows

Either download the latest release on the [Releases](https://github.com/AmineLeCepe/OsuBackgroundNuker/releases) tab, or:

- Download the latest [Python](https://www.python.org/downloads/) release
- Clone this repository (using git or by downloading the source code)
- Open either Powershell or CMD and write the following command inside of the source code directory:
```
python3 main.py
```
  - If you wish to specify a custom song folder, use the **--path** flag either:
    ```
    python3 main.py --path <Path to your osu! song folder>
    ```
    or this way:
    ```
    OsuBackgroundNuker.exe --path <Path to your osu! song folder>
    ```
    depending on your installation method.
    Passing an invalid directory will result in a crash and will not delete anything.

### Linux

- Download **Python** and **Git** (Check your distro's documentation on how to do it)
- Enter the following commands:
```
git clone https://github.com/AmineLeCepe/OsuBackgroundNuker/
cd OsuBackgroundNuker
python main.py
```
  - If you wish to specify a custom song folder, use the **--path** flag:
    ```
    python main.py --path <Path to your osu! song folder>
    ```
    
## Current limitations

- Does not support custom paths
- Super ugly interface

