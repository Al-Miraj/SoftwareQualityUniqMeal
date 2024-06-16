import logging
from cryptography.fernet import Fernet

# Generate a key for encryption (only once, then save it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# For the purpose of this example, we'll print the key. In real scenarios, store it securely.
print(f"Encryption key: {key.decode()}")

LOG_FILE_PATH = 'logfile.log'

def init_log():
    logging.basicConfig(filename=LOG_FILE_PATH,
                        format='%(asctime)s : %(levelname)s : %(filename)s : %(message)s',
                        level=logging.INFO,
                        force=True)

def log_warning(msg):
    enc_msg = encrypt(msg)
    logging.warning(enc_msg)

def log_info(msg):
    enc_msg = encrypt(msg)
    logging.info(enc_msg)

def read_log(msg):
    enc_msg = decrypt(msg)
    logging.warning(enc_msg)

def getLog():
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
        # Read log file, split on new line, and save only non-empty lines 
        encrypted_content = [line for line in f.read().split("\n") if line]
        for log_line in encrypted_content:
            # Example log line:
            # 2023-06-11 18:31:37,210 : WARNING : root : Zxjw%xzujwfirnsb%itjx%sty%j}nxy3
            # Get encrypted log string.
            last = log_line.split(" : ")[-1] 
            log_msg = decrypt(last)
            first = log_line.split(" : ")[:3]
            log_line = " : ".join(first + [log_msg])
            print(log_line)

def encrypt(msg):
    enc_msg = cipher_suite.encrypt(msg.encode())
    return enc_msg.decode()

def decrypt(enc_msg):
    dec_msg = cipher_suite.decrypt(enc_msg.encode())
    return dec_msg.decode()




