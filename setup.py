from setuptools import setup, Extension
setup(
    name="python_ctypes_example",
    version="0.1",
    ext_modules=[Extension('myclib', ['c/myclib.c'])],
)
