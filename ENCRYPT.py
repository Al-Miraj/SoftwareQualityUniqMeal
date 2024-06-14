import json
import argparse
import os
#import argon2
import base64


# Retrieve full path of the directory this Python file is in.
dirname = os.path.dirname(__file__)
# Full path of settings.json.
__settings_path = os.path.join(dirname, 'settings.json')

if __name__ == "__main__":
  import sys
  if sys.argv[0] ==  ".\encryption.py":
    __settings_path = "../settings.json"


with open(__settings_path) as file:
  __SETTINGS = json.load(file)
  
__SHIFT = __SETTINGS["encryption"]["shift"]
__ADD = lambda x,y: x + y 
__SUBTRACT = lambda x,y: x - y

def __ceasar_cipher(func: callable) -> callable:
  def encryptor(text: str) -> str:
    result = ""
    for char in text:
      result += chr(
        func(ord(char), __SHIFT) % 0x110000
        
      )
  
    return result
  
  return encryptor


def encrypt(text: str) -> str:
  result = __ceasar_cipher(__ADD)(text)
  return base64.b64encode(result.encode()).decode()

def decrypt(text: str) -> str:
  text = base64.b64decode(text.encode()).decode()
  return __ceasar_cipher(__SUBTRACT)(text)
