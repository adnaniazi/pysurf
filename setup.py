"""This file is used to convert GUI application into an executable or an msi installer"""

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py',
               base=base,
               targetName='PySurf.exe',
               icon='icon.ico'
               )
]

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "PySurf",                                 # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]PySurf.exe",                  # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),

    ("StartupShortcut",        # Shortcut
     "StartupFolder",          # Directory_
     "PySurf",                                 # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]PySurf.exe",                  # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
]

msi_data = {"Shortcut": shortcut_table}  # This will be part of the 'data' option of bdist_msi

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}


setup(
    name = "PySurf",
    version = '0.1',
    description = "A Python-based web browser",
    options = {'bdist_msi':bdist_msi_options},
    executables = executables
)