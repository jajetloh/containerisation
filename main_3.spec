# -*- mode: python ; coding: utf-8 -*-
# https://discuss.streamlit.io/t/using-pyinstaller-or-similar-to-create-an-executable/902/18?page=3

block_cipher = None

a = Analysis(['main_3.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 (
                     "env/Lib/site-packages/altair/vegalite/v4/schema/vega-lite-schema.json",
                     "./altair/vegalite/v4/schema/"
                 ),
                 (
                     "env/Lib/site-packages/streamlit/static",
                     "./streamlit/static"
                 )
            ],
            hiddenimports=[],
            hookspath=[],
            hooksconfig={},
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main_3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main_3',
)
