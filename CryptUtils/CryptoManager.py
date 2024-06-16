# import os
# from cryptography.fernet import Fernet
# import base64
# from Database.DBConfig import DBConfig



# class CrytoManager:
#     input = ""

#     @staticmethod
#     def GenerateKey(filePath="Crytography\secret.key"):
#         try:
#             newKey = Fernet.generate_key()
#             with open(filePath, 'ab') as key_file:
#                 key_file.write(newKey + b'\n')
#             print(f"Key generated and saved to {filePath}")
#             print(f"Your key: {newKey}")
#         except Exception as e:
#             print(f"An error occurred while generating the key: {e}")

#     def load_key(filePath="Crytography\secret.key"):
#         try:
#             # Controleer of het bestand bestaat voordat je het probeert te openen
#             if not os.path.exists(filePath):
#                 raise FileNotFoundError(f"Key file not found: {filePath}")
            
#             with open(filePath, 'rb') as key_file:
#                 key = key_file.read()
#             return key
#         except Exception as e:
#             print(f"An error occurred while loading the key: {e}")
#             return None

#     @staticmethod
#     def LoadKey(filePath="Crytography\secret.key"):
#         try:
#             if not os.path.exists(filePath):
#                 print(f"Bestand '{filePath}' niet gevonden.")
#                 return None
#             with open(filePath, 'rb') as key_file:
#                 lines = filePath.readlines()
#                 for line in lines:
#                     print(line.strip())
#         except Exception as e:
#             print(f"Fout bij het laden van de sleutel: {e}")
#             return None


#     @staticmethod
#     def EncryptMessage(key, message):
#         cipher_suite = Fernet(key)
#         encryptedMessage = cipher_suite.encrypt(message.encode())
#         return encryptedMessage

#     @staticmethod
#     def DecryptMessage(encryptedMessage, key):
#         cipher_suite = Fernet(key)
#         decryptedMessage = cipher_suite.decrypt(encryptedMessage).decode()
#         return decryptedMessage
        
import json
import base64

SETTINGS_JSON = """
{
    "encryption": { 
        "shift": 3
    }
}
"""


__SETTINGS = json.loads(SETTINGS_JSON)
__SHIFT = __SETTINGS["encryption"]["shift"]

def encrypt(text: str) -> str:
    result = ""
    for char in text:
        shifted_char = chr(ord(char) + __SHIFT)
        result += shifted_char
  
    return base64.b64encode(result.encode()).decode()

def decrypt(text: str) -> str:
    decoded_text = base64.b64decode(text.encode()).decode()
    result = ""
    for char in decoded_text:
        shifted_char = chr(ord(char) - __SHIFT)
        result += shifted_char
  
    return result
