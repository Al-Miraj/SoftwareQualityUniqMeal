import logging

def init_log():
    # Set log file,  log format, and the log level.
    logging.basicConfig(filename='logfile.log',
                        format='%(asctime)s : %(levelname)s : %(filename)s : %(message)s',
                        level=logging.INFO,
                        force=True)
    #
    # # Gets or creates a logger
    # logger = logging.getLogger(__name__)  
    # # set log level
    # logger.setLevel(logging.WARNING)
    # # define file handler and set formatter
    # file_handler = logging.FileHandler('logfile.log')
    # formatter    = logging.Formatter()
    # file_handler.setFormatter(formatter)
    # # add file handler to logger
    # logger.addHandler(file_handler)

# def log_warning(msg):
#     # Encrypt log message.
#     enc_msg = encrypt(msg)
#     # Log message.
#     logging.warning(enc_msg)


# def log_info(msg):
#     # Encrypt log message.
#     enc_msg = encrypt(msg)
#     # Log message.
#     logging.info(enc_msg)


def read_log(msg):

    enc_msg = decrypt(msg)
    # Log message.
    logging.warning(enc_msg)

def getLog():
  with open("logfile.log", "r", encoding="utf-8") as f:
    #read log file, split on new line and save only non empty lines 
    encrypted_content = [line for line in f.read().split("\n") if line]
    # Loop over the lines in the log file.
    for log_line in encrypted_content:
        # Example log line:
        # 2023-06-11 18:31:37,210 : WARNING : root : Zxjw%xzujwfirnsb%itjx%sty%j}nxy3
        # Get encrypted log string.
        last = log_line.split(" : ")[-1] 
        log_msg = decrypt(last)
        first = log_line.split(" : ")[:3]
        log_line = " : ".join(first + [log_msg])
        print(log_line)
    

    # Logs
    #logger.debug('A debug message')
    #logger.info('An info message')
    #encrypt.encrypt(str(logger.warning('Something is not right.')))
    #logger.error('A Major error has happened.')
    #logger.critical('Fatal error. Cannot continue')
