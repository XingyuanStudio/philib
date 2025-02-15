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


class PhigrosGet:
    def __init__(self, sessionToken: str):
        self.sessionToken = bytes(sessionToken, "utf-8")
        self.handle = phigros.get_handle(sessionToken)

    def __del__(self):
        phigros.free_handle(self.handle)