import logging
from cryptography.fernet import Fernet
import os

# Load the SuperAdmin key
key_file_path = os.path.join(os.path.dirname(__file__), "superadmin_key.key")

try:
    with open(key_file_path, "rb") as key_file:
        superadmin_key = key_file.read()

    cipher = Fernet(superadmin_key)

except FileNotFoundError:
    print(f"Error: The SuperAdmin key file 'superadmin_key.key' was not found.")
    raise
except Exception as e:
    print(f"An error occurred while loading the SuperAdmin key: {str(e)}")
    raise

# Custom SuperAdmin Log Handler
class SuperAdminLogHandler(logging.Handler):
    def emit(self, record):
        try:
            log_entry = self.format(record)
            print(f"Logging Entry: {log_entry}")  # Debugging print to confirm log entry content
            encrypted_log = cipher.encrypt(log_entry.encode())

            # Debugging: Check if the log file is being accessed
            print("Writing to superadmin_log.log")
            with open("superadmin_log.log", "ab") as log_file:
                log_file.write(encrypted_log + b"\n")
            print("Log written successfully.")

        except Exception as e:
            print(f"Error encrypting SuperAdmin log entry: {e}")

# Set up the SuperAdmin logger
superadmin_logger = logging.getLogger("SuperAdminLogger")
superadmin_logger.setLevel(logging.INFO)

# Add handler for SuperAdmin logs
superadmin_log_handler = SuperAdminLogHandler()
formatter = logging.Formatter('%(asctime)s || %(message)s || Suspicious: %(suspicious)s')
superadmin_log_handler.setFormatter(formatter)
superadmin_logger.addHandler(superadmin_log_handler)

# Expose the logger for other modules
def get_logger():
    return superadmin_logger

# Function to read SuperAdmin logs
def view_superadmin_logs():
    try:
        with open("superadmin_log.log", "rb") as log_file:
            for encrypted_log in log_file:
                decrypted_log = cipher.decrypt(encrypted_log.strip())
                print(decrypted_log.decode())
                # Log the viewing of the logs
            superadmin_logger.info("Logs are viewed", extra={"suspicious": "No"})
    except FileNotFoundError:
        print("SuperAdmin log file not found.")
    except Exception as e:
        print(f"Error reading SuperAdmin logs: {str(e)}")


# import logging
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import serialization
# from cryptography.fernet import Fernet
# from datetime import datetime
# import os

# # Load public key for encryption (for regular log file)
# with open("public_key.pem", "rb") as key_file:
#     public_key = serialization.load_pem_public_key(key_file.read())

# # Load encryption key for SuperAdmin log
# with open("Login/superadmin_key.key", "rb") as key_file:
#     encryption_key = key_file.read()


# # Initialize the cipher for SuperAdmin log encryption
# cipher = Fernet(superadmin_key)

# # In-memory list to store log entries
# log_list = []
# log_counter = 1  # Initialize a log entry counter

# # Custom logging handler to encrypt logs and store them in a list
# class EncryptedLogHandler(logging.Handler):
#     def emit(self, record):
#         global log_counter
#         try:
#             # Format log record with additional fields
#             log_entry = f"{log_counter} | {datetime.now().strftime('%d-%m-%Y')} | {datetime.now().strftime('%H:%M:%S')} | {record.__dict__.get('username', 'unknown')} | {record.getMessage()} | Suspicious: {record.__dict__.get('suspicious', 'No')}"
            
#             # Add to in-memory log list
#             log_list.append({
#                 'No.': log_counter,
#                 'Date': datetime.now().strftime('%d-%m-%Y'),
#                 'Time': datetime.now().strftime('%H:%M:%S'),
#                 'Username': record.__dict__.get('username', 'unknown'),
#                 'Activity': record.getMessage(),
#                 'Suspicious': record.__dict__.get('suspicious', False)
#             })
            
#             # Increment log counter after adding to log_list
#             log_counter += 1

#             # Encrypt the log entry
#             encrypted_log = public_key.encrypt(
#                 log_entry.encode(),
#                 padding.OAEP(
#                     mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                     algorithm=hashes.SHA256(),
#                     label=None
#                 )
#             )

#             # Write encrypted log to file
#             with open("encrypted_log.log", "ab") as log_file:
#                 log_file.write(encrypted_log + b"\n")

#         except Exception as e:
#             print(f"Error encrypting log entry: {e}")

# # Set up logger for regular logging
# logger = logging.getLogger("EncryptedLogger")
# logger.setLevel(logging.INFO)

# # Set custom encrypted log handler
# encrypted_log_handler = EncryptedLogHandler()
# formatter = logging.Formatter('%(asctime)s - %(username)s - %(message)s')
# encrypted_log_handler.setFormatter(formatter)

# logger.addHandler(encrypted_log_handler)


# # Custom logging handler for SuperAdmin log file
# class SuperAdminLogHandler(logging.Handler):
#     def emit(self, record):
#         try:
#             # Format log record
#             log_entry = self.format(record)
            
#             # Encrypt the log entry using Fernet
#             encrypted_log = cipher.encrypt(log_entry.encode())

#             # Write encrypted log to the SuperAdmin log file
#             with open("superadmin_log.log", "ab") as log_file:
#                 log_file.write(encrypted_log + b"\n")
                
#         except Exception as e:
#             print(f"Error encrypting SuperAdmin log entry: {e}")

# # Set up SuperAdmin logger
# superadmin_logger = logging.getLogger("SuperAdminLogger")
# superadmin_logger.setLevel(logging.INFO)

# # Set up SuperAdmin log handler
# superadmin_log_handler = SuperAdminLogHandler()
# superadmin_log_handler.setFormatter(formatter)

# superadmin_logger.addHandler(superadmin_log_handler)

# # Function to decrypt and view SuperAdmin logs
# def view_superadmin_logs():
#     try:
#         with open("superadmin_log.log", "rb") as log_file:
#             for encrypted_log in log_file:
#                 decrypted_log = cipher.decrypt(encrypted_log.strip())
#                 print(decrypted_log.decode())
#     except Exception as e:
#         print(f"Error reading SuperAdmin logs: {str(e)}")


# # Test SuperAdmin logging and viewing
# def test_superadmin_logging():
#     username = "superadmin"
#     superadmin_logger.info(f"Test log entry for {username}.", extra={"username": username})

# Uncomment to test logging
# test_superadmin_logging()
# view_superadmin_logs()

# Example call to decrypt logs
# decrypt_log_file()


# # For admin to view decrypted logs
# decrypt_log_file()



# import logging

# def init_log():
#     # Set log file,  log format, and the log level.
#     logging.basicConfig(filename='logfile.log',
#                         format='%(asctime)s : %(levelname)s : %(filename)s : %(message)s',
#                         level=logging.INFO,
#                         force=True)
#     #
#     # # Gets or creates a logger
#     # logger = logging.getLogger(__name__)  
#     # # set log level
#     # logger.setLevel(logging.WARNING)
#     # # define file handler and set formatter
#     # file_handler = logging.FileHandler('logfile.log')
#     # formatter    = logging.Formatter()
#     # file_handler.setFormatter(formatter)
#     # # add file handler to logger
#     # logger.addHandler(file_handler)

# # def log_warning(msg):
# #     # Encrypt log message.
# #     enc_msg = encrypt(msg)
# #     # Log message.
# #     logging.warning(enc_msg)


# # def log_info(msg):
# #     # Encrypt log message.
# #     enc_msg = encrypt(msg)
# #     # Log message.
# #     logging.info(enc_msg)


# def read_log(msg):

#     enc_msg = decrypt(msg)
#     # Log message.
#     logging.warning(enc_msg)

# def getLog():
#   with open("logfile.log", "r", encoding="utf-8") as f:
#     #read log file, split on new line and save only non empty lines 
#     encrypted_content = [line for line in f.read().split("\n") if line]
#     # Loop over the lines in the log file.
#     for log_line in encrypted_content:
#         # Example log line:
#         # 2023-06-11 18:31:37,210 : WARNING : root : Zxjw%xzujwfirnsb%itjx%sty%j}nxy3
#         # Get encrypted log string.
#         last = log_line.split(" : ")[-1] 
#         log_msg = decrypt(last)
#         first = log_line.split(" : ")[:3]
#         log_line = " : ".join(first + [log_msg])
#         print(log_line)
    

#     # Logs
#     #logger.debug('A debug message')
#     #logger.info('An info message')
#     #encrypt.encrypt(str(logger.warning('Something is not right.')))
#     #logger.error('A Major error has happened.')
#     #logger.critical('Fatal error. Cannot continue')
