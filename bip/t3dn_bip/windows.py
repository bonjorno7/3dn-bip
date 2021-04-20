import ctypes
from ctypes import c_ulong, c_wchar_p, c_int, c_void_p
from ctypes.wintypes import HANDLE, DWORD, HWND, HINSTANCE, HKEY
from subprocess import list2cmdline

ShellExecuteEx = ctypes.windll.shell32.ShellExecuteExW
WaitForSingleObject = ctypes.windll.kernel32.WaitForSingleObject
GetExitCodeProcess = ctypes.windll.kernel32.GetExitCodeProcess
CloseHandle = ctypes.windll.kernel32.CloseHandle

SEE_MASK_NOCLOSEPROCESS = 0x00000040
SEE_MASK_NO_CONSOLE = 0x00008000
SW_SHOW = 5


class ShellExecuteInfo(ctypes.Structure):
    _fields_ = [
        ('cbSize', DWORD),
        ('fMask', c_ulong),
        ('hwnd', HWND),
        ('lpVerb', c_wchar_p),
        ('lpFile', c_wchar_p),
        ('lpParameters', c_wchar_p),
        ('lpDirectory', c_wchar_p),
        ('nShow', c_int),
        ('hInstApp', HINSTANCE),
        ('lpIDList', c_void_p),
        ('lpClass', c_wchar_p),
        ('hKeyClass', HKEY),
        ('dwHotKey', DWORD),
        ('hIcon', HANDLE),
        ('hProcess', HANDLE),
    ]

    def __init__(self, **kwargs):
        ctypes.Structure.__init__(self)
        self.cbSize = ctypes.sizeof(self)

        for key, value in kwargs.items():
            setattr(self, key, value)


def call(args: list, timeout: int = None):
    '''Call executable with admin privileges.'''
    executable = args[0]
    parameters = args[1:]

    if timeout is not None:
        milliseconds = timeout * 1000
    else:
        milliseconds = -1

    execute_info = ShellExecuteInfo(
        fMask=SEE_MASK_NOCLOSEPROCESS | SEE_MASK_NO_CONSOLE,
        hwnd=None,
        lpVerb='runas',
        lpFile=executable,
        lpParameters=list2cmdline(parameters),
        lpDirectory=None,
        nShow=SW_SHOW,
    )

    if not ShellExecuteEx(ctypes.byref(execute_info)):
        raise ctypes.WinError()

    process_handle = execute_info.hProcess
    WaitForSingleObject(process_handle, milliseconds)

    exit_code = DWORD()
    GetExitCodeProcess(process_handle, ctypes.byref(exit_code))

    CloseHandle(process_handle)
    return exit_code.value
