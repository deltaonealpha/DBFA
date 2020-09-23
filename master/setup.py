from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None

packages = ["idna", "tabular-print", "tabulate", "reportlab", "PySimpleGUI", "pandas", "cv2", "tqdm", "colorama", "win10toast", "telegram", "telegram_send", "telegram.ext", "PyQRCode", "PIL", "spotilib", "SwSpotify", "pynput", "matplotlib", "oschmod", "os", "time", "sys", "shutil", "pathlib", "logging", "socket", "urllib", "json", "math", "random", "getpass", "sqlite3", "requests", "png", "email", "platform", "webbrowser"]
executables = [Executable("bleading_edge.py", base=base)]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "deltaDBFA",
    options = options,
    version = "8.42",
    description = 'Experimental exe runnable for deltaDBFA.',
    executables = executables
)
