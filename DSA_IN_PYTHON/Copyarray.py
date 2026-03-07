from array import *

val = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])

copyArray = array(val.typecode, (x for x in val))

copyArray.pop(2)  # for deleting elments in array

for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")
