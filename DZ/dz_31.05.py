# # Функторы
# #
# # class Counter:
# #     def __init__(self):
# #         self.__count = 0
# #
# #     def __call__(self, *args, **kwargs):
# #         self.__count += 1
# #         print(self.__count)
# #
# #
# # c1 = Counter()
# # c1()
# # c1()
# # c1()
#
# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1("  ?  : Hello World!  ; "))
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StringStrip("?:!.; ")
# print(s1("  ?  : Hello World!  ; "))
