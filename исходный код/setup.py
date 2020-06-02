from cx_Freeze import setup, Executable

setup (name='server', version = '1.0', description = 'server', executables = [Executable('server.py')])