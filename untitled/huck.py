# class ArrayIterator:
#     _arr = []
#     _point = 0
#     _len = 0
#
#     def __init__(self, array=[], point=0):
#         self._arr = array
#         self._len = len(self._arr)
#         self._point = point
#
#     def __str__(self):
#         return str(self._arr[self._point])
#
#     def set_default(self):
#         self._point = 0
#
#     def next(self):
#         if self._point == self._len:
#             self._point = 0
#         else:
#             self._point += 1
#         return self.__str__()
#
#     def prev(self):
#         if self._point == 0:
#             self._point = self._len-1
#         else:
#             self._point -= 1
#         return self.__str__()
#
# arr = [1, 2, 3, 4, 5]
# it = ArrayIterator(arr)
# print(it.next())
# print(it.prev())
# print(it.prev())

message = "hello world"
b = bytes(message, 'ascii')

for i in b:
    print(i)

