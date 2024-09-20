# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('addPlatoAc_ui.py', '.'), ('control_bd.py', '.'), ('dialogoAgregarPlatos.py', '.'), ('dialogoOrden_ui.py', '.'), ('estado.json', '.'), ('exporControl.py', '.'), ('formBorrarInv_ui.py', '.'), ('formEditarInv_ui.py', '.'), ('formularioAI_ui.py', '.'), ('formularioControl.py', '.'), ('Inventario.db', '.'), ('paginaPrincipal.py', '.'), ('paginaPrincipal_ui.py', '.'), ('recursos_rc.py', '.'), ('recursos_rc', 'recursos_rc/'), ('build', 'build/')],
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
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['invoice.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
