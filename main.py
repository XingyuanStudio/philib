import ctypes
import platform


system = platform.system()
if system == "Windows":
    lib_name = "Library/phigros.dll"
elif system == "Linux":
    lib_name = "Library/libphigros-64.so"
else:
    raise OSError("Unsupported operating system")


try:
    phigros = ctypes.CDLL(lib_name)
except FileNotFoundError:
    raise FileNotFoundError(
        "Error: Failed to load phigros.dll or libphigros-64.so"
        "Please see ./Library/README.md and ./Library/PhigrosLibrary.md or for more information. You should compile the library yourself. See also https://github.com/7aGiven/PhigrosLibrary."
    )
else:
    phigros.get_handle.argtypes = [ctypes.c_char_p]
    phigros.get_handle.restype = ctypes.c_void_p

    phigros.get_save.argtypes = [ctypes.c_void_p]
    phigros.get_save.restype = ctypes.c_char_p

    phigros.free_handle.argtypes = [ctypes.c_void_p]
    phigros.free_handle.restype = ctypes.c_void_p


class PhigrosGet:
    def __init__(self, sessionToken: str):
        self.sessionToken = bytes(sessionToken, "utf-8")
        self.handle = phigros.get_handle(self.sessionToken)
        if not self.handle:
            raise RuntimeError("Failed to get handle from phigros library")

    def get_save(self):
        return phigros.get_save(self.handle)

    def __del__(self):
        if hasattr(self, "handle") and self.handle:
            try:
                phigros.free_handle(self.handle)
            except:
                pass


# Example usage
if __name__ == "__main__":
    user = PhigrosGet("Your sessionToken")
    print(user.get_save())
