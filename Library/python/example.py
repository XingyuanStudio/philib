import ctypes

# phigros = ctypes.CDLL("../libphigros-64.so")
phigros = ctypes.CDLL("./phigros.dll")
print(phigros)
phigros.get_handle.argtypes = ctypes.c_char_p,
phigros.get_handle.restype = ctypes.c_void_p
phigros.free_handle.argtypes = ctypes.c_void_p,
phigros.get_nickname.argtypes = ctypes.c_void_p,
phigros.get_nickname.restype = ctypes.c_char_p
phigros.get_summary.argtypes = ctypes.c_void_p,
phigros.get_summary.restype = ctypes.c_char_p
phigros.get_save.argtypes = ctypes.c_void_p,
phigros.get_save.restype = ctypes.c_char_p
phigros.load_difficulty.argtypes = ctypes.c_void_p,
phigros.get_b19.argtypes = ctypes.c_void_p,
phigros.get_b19.restype = ctypes.c_char_p
# phigros.re8.argtypes = ctypes.c_void_p,

sessionToken = b"ztl8rh36krtgro724jo83f3o5"
handle = phigros.get_handle(sessionToken)   # 获取handle,申请内存,参数为sessionToken
# print(handle)
# print(phigros.get_nickname(handle))         # 获取玩家昵称
print(str(phigros.get_summary(handle), "utf-8"))          # 获取Summary
print(str(phigros.get_save(handle), "utf-8"))        # 获取存档
phigros.load_difficulty(b"./difficulty.tsv")# 读取difficulty.tsv,参数为文件路径
print()
print("b19:")
# print(str(phigros.get_b19(handle), "utf-8"))           # 从存档读取B19,依赖load_difficulty
phigros.free_handle(handle)                 # 释放handle的内存,不会被垃圾回收,使用完handle请确保释放
