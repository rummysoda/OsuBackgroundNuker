# Osu Background Nuker

Title is self explanatory.

Python script that fetches all of the beatmaps in your Osu! song folder, then deletes all of the background images in order to save space.

The background images are directly deleted, not moved to the recycle bin.

## How to run

### Windows

Either download the latest release on the [Releases](https://github.com/AmineLeCepe/OsuBackgroundNuker/releases) tab, or:

- Download the latest [Python](https://www.python.org/downloads/) release
- Clone this repository
- Open either Powershell or CMD and write the following command:
```
python3 main.py
```

### Linux

For now, opening the executable of the latest release with Wine *should* do the same job as on Windows (I have not tested it)

## Current limitations

- Does not support custom paths
- Super ugly interface

