import os
import shutil

'''
Print functions moeten nog weggehaald worden na het testen van deze functies
'''

FILE_TO_BACKUP = 'Database/UniqueMealDB.db'

class Backup:

    def create_backup():
        backup_dir = 'Backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        existing_backups = [f for f in os.listdir(backup_dir) if f.startswith('Backup_') and os.path.isfile(os.path.join(backup_dir, f))]
        backup_number = len(existing_backups) + 1
        
        new_backup_file = os.path.join(backup_dir, f"Backup_{backup_number}.db")
        
        shutil.copy(FILE_TO_BACKUP, new_backup_file)
        print(f"Backup made: {new_backup_file}")

    def restore_backup():
        backup_dir = 'Backups'
        
        if not os.path.exists(backup_dir):
            print("No backups found")
            return
        
        
        existing_backups = os.listdir(backup_dir)
        
        new_backup_file = os.path.join(backup_dir, existing_backups[-1])
        
        shutil.copy(new_backup_file, FILE_TO_BACKUP)
        print(f"restore succesful: {new_backup_file}")