import ctypes

try:
    phigros = ctypes.CDLL("Library/phigros.dll")
except:
    try:
        phigros = ctypes.CDLL("Library/libphigros-64.so")
    except:
        print("Error: Failed to load phigros.dll or libphigros-64.so")
        print("Please see ./Library/README.md and ./Library/PhigrosLibrary.md or for more information. You should compile the library yourself. See also https://github.com/7aGiven/PhigrosLibrary.")
        raise
        exit()
else:
    phigros.get_handle.argtypes = [ctypes.c_char_p]
    phigros.get_handle.restype = ctypes.c_void_p

    phigros.free_handle.argtypes = [ctypes.c_void_p]
    phigros.free_handle.restype = ctypes.c_void_p



class PhigrosGet:
    def __init__(self, sessionToken: str):
        self.sessionToken = bytes(sessionToken, "utf-8")
        self.handle = phigros.get_handle(self.sessionToken)
        if not self.handle:
            raise RuntimeError("Failed to get handle from phigros library")

    def __del__(self):
        if hasattr(self, 'handle') and self.handle:
            try:
                phigros.free_handle(self.handle)
            except:
                pass
            
    
        
# PhigrosGet("ztl8rh36krtgro724jo83f3o5")

