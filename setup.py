from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None

executables = [Executable("App.py", base=base)]


setup(
    name="Alencur Software Jurídico",
    version="2.0",
    description='Software para a área Jurídica',
    executables=executables
)

#comando python setup.py build para buildar
