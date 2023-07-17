import os
import time
from config import DB_HOST, DB_PASSWORD, DB_NAME, DB_USER, TIMEOUT, DATE_FORMAT, DIRECTORY, MAX_DAYS


while True:
    current_time = time.strftime(DATE_FORMAT)
    backup_file_name = f"{DB_NAME}-{current_time}.sql"
    backup_file_path = DIRECTORY + backup_file_name
    
    mysql_cmd = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_file_path}"
    os.system(mysql_cmd)
    
    find_cmd = f'find {DIRECTORY} -type f -name "*.sql" -mtime +{MAX_DAYS} -delete'
    os.system(find_cmd)
    
    time.sleep(TIMEOUT)

    


