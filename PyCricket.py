#!/usr/bin/python           # This is client.py file

import socket     # Import socket module
import winreg

REG_PATH = r"Software\Microsoft\Windows\CurrentVersion"

REG_PATH = r"Control Panel\Mouse"

def set_reg(reg, name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(reg, name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

def main():
    # AF_INET == ipv4
    # SOCK_STREAM == TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object


    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                # Reserve a port for your service.



    s.connect((host, port))
    print(s.recv(1024))
    s.close()
def burrow():
    if
    print(get_reg('MouseSensitivity'))
    get_reg(r"Software\Microsoft\Windows\CurrentVersion\Run", "WindowsServe")

burrow()
main()