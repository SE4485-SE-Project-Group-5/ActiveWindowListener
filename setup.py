import sys
from cx_Freeze import setup, Executable

# Build options
options = {
    # Similar to Pyinstaller's "--add-data" flag
    "include_files": [
        ("static", "static"),
        ("templates", "templates")
    ]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="ActiveWindowListener",
      version="0.1.0",
      description="Description placeholder",
      options={"build_exe": options},
      executables=[Executable("flair.py", base=base)])
