# -*- mode: python ; coding: utf-8 -*-

from PyInstaller import compat, log as logging
from os import listdir, getcwd
from os.path import join

block_cipher = None

dll_dir = join(getcwd(), "dlls")
binaries = [(join(dll_dir, dll), ".") for dll in listdir("dlls")]

a = Analysis(
    ['my_script.py'],
    pathex=['/path/to/your/script'],
    binaries=[],
    datas=[('data_file.txt', 'data')],
    hiddenimports=['additional_package'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=false
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='my_script',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='my_script'
)
