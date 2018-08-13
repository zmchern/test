# -*- mode: python -*-

block_cipher = None


a = Analysis(['guessNum.py'],
             pathex=['D:\\360\xb0\xb2\xc8\xab\xe4\xaf\xc0\xc0\xc6\xf7\xcf\xc2\xd4\xd8\\python\\\xd4\xb4\xb4\xfa\xc2\xeb'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='guessNum',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
