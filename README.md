# python_ctypes_examples

A simple example showing how to call C from Python. 

## How to build 

In the top directory type:

```bash
python setup.py build
```

## How to run the example

Type:

```bash
python test.py <path_to_shared_library>
```

The library is typically called ```myclib.so```. For instance:

```bash
python test.py build/lib.linux-x86_64-2.7/myclib.so
```

