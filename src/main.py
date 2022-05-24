"""
Run the game
"""

from os import system, name, getcwd, chdir
from os.path import sep

curdir = getcwd().split(sep)[-1]

def get_os():
    """
    Get the OS of the user
    """
    if name == 'nt':
        return 'windows'
    else:
        return 'linux'


if curdir == 'src':
    if get_os == "windows":
        system("python menu.py")
    else:
        system("python3 menu.py")
        
elif curdir == 'pyMinecraft':
    chdir("src")
    if get_os == "windows":
        system("python menu.py")
    else:
        system("python3 menu.py")
else:
    print("invalid directory")
    exit(1)