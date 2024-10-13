import os
import shutil

# '''
# Print functions moeten nog weggehaald worden na het testen van deze functies
# '''

# FILE_TO_BACKUP = 'Database/UniqueMealDB.db'

# class Backup:

#     def create_backup():
#         backup_dir = 'Backups'
#         if not os.path.exists(backup_dir):
#             os.makedirs(backup_dir)
        
#         existing_backups = [f for f in os.listdir(backup_dir) if f.startswith('Backup_') and os.path.isfile(os.path.join(backup_dir, f))]
#         backup_number = len(existing_backups) + 1
        
#         new_backup_file = os.path.join(backup_dir, f"Backup_{backup_number}.db")
        
#         shutil.copy(FILE_TO_BACKUP, new_backup_file)
#         print(f"Backup made: {new_backup_file}")

#     def restore_backup():
#         backup_dir = 'Backups'
        
#         if not os.path.exists(backup_dir):
#             print("No backups found")
#             return
        
        
#         existing_backups = os.listdir(backup_dir)
        
#         new_backup_file = os.path.join(backup_dir, existing_backups[-1])
        
#         shutil.copy(new_backup_file, FILE_TO_BACKUP)
#         print(f"restore succesful: {new_backup_file}")


import os
import shutil
import zipfile
from datetime import datetime

FILE_TO_BACKUP = 'Database/UniqueMealDB.db'
LOG_FILE = 'superadmin_log.log'  # Path naar het logbestand !!!!!!!!!!!!!!!!!!

class Backup:

    @staticmethod
    def create_backup():
        backup_dir = 'Backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        backup_filename = f"Backup_{timestamp}.zip"
        new_backup_file = os.path.join(backup_dir, backup_filename)

        try:
            with zipfile.ZipFile(new_backup_file, 'w') as zipf:
                zipf.write(FILE_TO_BACKUP, os.path.basename(FILE_TO_BACKUP))
                
                # Voeg het logbestand toe aan de zip als het bestaat TODOOOOOOO
                if os.path.exists(LOG_FILE):
                    zipf.write(LOG_FILE, os.path.basename(LOG_FILE))
                else:
                    print(f"Logfile not found: {LOG_FILE}")

            print(f"Backup made: {new_backup_file}")
        except Exception as e:
            print(f"Error creating backup: {e}")

    @staticmethod
    def restore_backup():
        backup_dir = 'Backups'

        if not os.path.exists(backup_dir):
            print("Backup directory not found.")
            return

        existing_backups = [f for f in os.listdir(backup_dir) if f.endswith('.zip')]
        if not existing_backups:
            print("No backups found in the directory.")
            return

        try:
            latest_backup = max(existing_backups, key=lambda f: os.path.getctime(os.path.join(backup_dir, f)))
            backup_path = os.path.join(backup_dir, latest_backup)

            with zipfile.ZipFile(backup_path, 'r') as zipf:
                zipf.extract(os.path.basename(FILE_TO_BACKUP), os.path.dirname(FILE_TO_BACKUP))
                zipf.extract(os.path.basename(LOG_FILE), os.path.dirname(LOG_FILE))

            print(f"Restore successful from: {backup_path}")
        except Exception as e:
            print(f"Error restoring backup: {e}")
        