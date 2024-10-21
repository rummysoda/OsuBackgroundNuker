a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[('background.png', '.'),
                    ('app.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,  # Set cipher to None
             noarchive=False)  # Fixed typo from 'Fals' to 'False'

pyz = PYZ(a.pure, a.zipped_data,
           cipher=None)  # Set cipher to None

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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
    icon='app.ico',  # Corrected the icon path
)

app = BUNDLE(
    exe,
    name='main.app',
    icon='app.ico',
    bundle_identifier=None,
)