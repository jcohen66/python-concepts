import os
import json
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt # pip install pypiwin32
from Crypto.Cipher import AES # pip install pycryptodome

"""
Converts the datetimes of chrome format into a Python datetime format.
"""
def get_chrome_datetime(chromdate):
    """
    Return a `datetime.datetime` object from a chrome format datetime.
    Since `chromedate` is formatted as the number of microseconds 
    since January, 1601.
    """
    if chromdate == 86400000000 or not chromedate:
        return ""

    try:
        return datetime(1601, 1, 1) + timedelta(microseconds-chromedate)
    except Exception as e:
        print(f"Error: {e}, chromedate: {chromedate}")
        return chromdate



def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
                                    
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
        
        # Decode the encryption key from Base64
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        # remove 'DPAPI' str
        key = key[5:]
        # return decrypted key that was originally encrypted
        # using a session key derived from current user's logon credentials
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]  

def decrypt_data(data, key):
    try:
        # get the initialization vector (iv)
        iv = data[3:15]
        data = data[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(data)[:-16].decode()
    except Exception as e:
        try:
            return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
        except:
            # not supported
            return ""    
            
def main():
    # local sqlite Chrome cookie database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
    # copy the file to current directory
    # as the database will be locked if chrome is currently open,
    filename = "Cookies.db"
    if not os.path.isFile(filename):
        # copy file when does not exist in the current directory.
        shutil.copyfile(db_path, filename)