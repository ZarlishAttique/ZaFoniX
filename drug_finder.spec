# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['drug_finder.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/GCA/Downloads/DrugBank Project/DrugsList.xlsx', '.'), ('C:/Users/GCA/Downloads/sc1.jpeg', '.'), ('C:/Users/GCA/Downloads/sc2.jpeg', '.'), ('C:/Users/GCA/Downloads/sc3.jpeg', '.'), ('C:/Users/GCA/Downloads/sc4.jpeg', '.'), ('C:/Users/GCA/Downloads/SC5.jpeg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='drug_finder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\GCA\\Downloads\\DrugBank Project\\DrugFinder\\app_icon.ico'],
)
