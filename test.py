# Test ctypes
# A. Pletzer NeSI/NIWA
from ctypes import CDLL, c_int, c_double, c_void_p, byref, POINTER, Structure
import numpy
import sys

if len(sys.argv) < 2:
	print('Must provide path to the shared object')
	sys.exit(1)

libName = sys.argv[1]

# open the shared library
lib = CDLL(libName)

# ints and strings need no declaration
ier = lib.sayHello('PIG')

# how to pass a numpy array to C and get back the result by reference
arr = numpy.array([1, 2, 3], numpy.float64)
n = len(arr)
arrPtr = arr.ctypes.data_as(POINTER(c_double))
res = c_double()
ier = lib.getSum(len(arr), arrPtr, byref(res))

# create the Position struct object on the Python side and populate it
class Position(Structure):
	_fields = [("x", c_double),
		       ("y", c_double)]
pos1 = Position(x=1., y=2.)
pos2 = Position(x=1., y=3.)
print pos1
print pos1.x, pos1.y
lib.getSum.restype = c_double
lib.argtypes = [POINTER(Position), POINTER(Position)]
res = lib.getDistance(byref(pos1), byref(pos2))
print('The distance between pos1 and pos2 is {}'.format(res))
print pos1.x, pos1.y

# let the C library create the object and use void pointers to 
# pass the object around
handle = c_void_p()
lib.createPosition.restype = None
lib.createPosition.argtypes = [POINTER(c_void_p)]
lib.createPosition(byref(handle))

lib.setPosition.restype = None
lib.setPosition.argtypes = [POINTER(c_void_p), c_double, c_double]
lib.setPosition(byref(handle), 1.2, 2.3)

lib.printPosition.restype = None
lib.printPosition.argtypes = [POINTER(c_void_p)]
lib.printPosition(byref(handle))

lib.destroyPosition.restype = None
lib.destroyPosition.argtypes = [POINTER(c_void_p)]
lib.destroyPosition(byref(handle))

