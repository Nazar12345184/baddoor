# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.utils.hooks import collect_all

datas = [('Config.prc', '.'), ('0.jpg', '.'), ('002.jpg', '.'), ('004.jpg', '.'), ('005.jpg', '.'), ('006.jpg', '.'), ('007.jpg', '.'), ('008.jpg', '.'), ('00922.jpg', '.'), ('01.jpg', '.'), ('010 (1).jpg', '.'), ('010.jpg', '.'), ('03 (1).jpg', '.'), ('03.jpg', '.'), ('bm (1).mp3', '.'), ('bm.mp3', '.'), ('cldr (1).jpg', '.'), ('cldr.jpg', '.'), ('deah (1).jpg', '.'), ('deah.jpg', '.'), ('dooropen.mp3', '.'), ('Elevator.mp3', '.'), ('fgd.mp3', '.'), ('fig.jpg', '.'), ('figv.mp3', '.'), ('fndr.mp3', '.'), ('ima.png', '.'), ('images.jpg', '.'), ('lift.jpg', '.'), ('liftend (1).mp3', '.'), ('liftend.mp3', '.'), ('liftstop.jpg', '.'), ('loby.mp3', '.'), ('ort.jpg', '.'), ('photo.jpg', '.'), ('pip.mp3', '.'), ('pol.jpg', '.'), ('potolok.jpg', '.'), ('ppooiiuuyytt.png', '.'), ('redkey.mp3', '.'), ('rush.mp3', '.'), ('rushstart.mp3', '.'), ('sc.mp3', '.'), ('seek.mp3', '.'), ('Seek.obj', '.'), ('seekend.mp3', '.'), ('sfrm.png', '.'), ('stina.jpg', '.'), ('tbk.png', '.'), ('tem.jpg', '.'), ('temp.jpg', '.'), ('tinker.obj', '.'), ('Voicy_Figure Roar .mp3', '.'), ('YOU WIN.mp3', '.'), ('yw.jpg', '.')]
binaries = []
hiddenimports = ['panda3d.core', 'panda3d.direct']
binaries += collect_dynamic_libs('panda3d')
tmp_ret = collect_all('ursina')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('panda3d')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['sam proekt.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
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
    name='BaddoorGame',
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
)
