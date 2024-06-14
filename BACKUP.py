import os
import sqlite3
from zipfile import ZipFile
import argon2
from datetime import datetime


__PATH = "./backups"


def createFile(filename: str) -> tuple[bool, str]:
  createDirectory()
  timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
  try:
    with ZipFile("{path}/{fn}.zip".format(fn=filename, path=__PATH), "a") as zipObj:
      zipObj.write(filename="./database.db", arcname=timestamp + ".db")
    
    with ZipFile("{path}/{fn}.zip".format(fn=filename, path=__PATH), "a") as zipObj:
      zipObj.write(filename="./logfile.log", arcname=timestamp + ".log")

    return (True, "")
      
  except Exception as e:
    print(f"Unable to write to backup: {e}")
    return (False, "")
  
  
  #Takes list, sorts the newest 5 backups
def restoreFile():
    
    with ZipFile("{path}/backups.zip".format(path=__PATH), "r") as zipObj:
      file_names = zipObj.namelist()
      # Retrieve the timestamps of all backups.
      backups = [file_name.split(".")[0] for file_name in file_names]
      file_names.sort(reverse=True)
      # Deduplicate timestamps.
      backups = list(set(backups))
      backups.sort(reverse=True)

      print("These are the last 5 backups")
      for count, _ in enumerate(backups[:5]):
        print(count + 1, _)

      #timestamp = backups[:5][user_input - 1]
      user_input = input("Choose number 1 to 5. Select an option: ")
      
      
      if user_input == '1':
        print(f"Restored backup to {backups[0]}")
        restoreNumber(backups[0])
      elif user_input == '2':
        print(f"Restored backup to {backups[1]}")
        restoreNumber(backups[1])
      elif user_input == '3':
        print(f"Restored backup to {backups[2]}")
        restoreNumber(backups[2])
      elif user_input == '4':
        print(f"Restored backup to {backups[3]}")
        restoreNumber(backups[3])
      elif user_input == '5':
        print(f"Restored backup to {backups[4]}")
        restoreNumber(backups[4])
      else:
        print("Invalid. Choose between 1 and 5")

      
      
def restoreNumber(stringtime):
  log = stringtime + ".log"
  db = stringtime + ".db"

  print(log)
  print(db)
  
  with ZipFile("{path}/backups.zip".format(path=__PATH), "r") as zipObj:
    log_file = zipObj.read(log)
    db_file = zipObj.read(db)    
  
  with open("D:\CODE\src\database.db","wb") as file:
    file.write(db_file)

  with open("D:\CODE\src\logfile.log","wb") as file:
    file.write(log_file)

  


def createDirectory() -> None:
  if not os.path.exists(__PATH):
    os.mkdir(__PATH)

