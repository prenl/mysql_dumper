import os
import time
from config import DB_HOST, DB_PASSWORD, DB_NAME, DB_USER, DATE_FORMAT, DIRECTORY, MAX_DAYS
# import all constanst from dotenv file

current_time = time.strftime(DATE_FORMAT)
# gets current time in date_format (default DAY_MONTH_YEAR-HRS_MIN_SEC)

backup_file_name = f"{DB_NAME}-{current_time}.sql"
backup_file_path = DIRECTORY + backup_file_name
# defines file path for generated file

mysql_cmd = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_file_path}"
os.system(mysql_cmd)
# executes mysql_cmd in terminal, it takes selected db_name and dumps it to backup_file_path
    
find_cmd = f'find {DIRECTORY} -type f -name "*.sql" -mtime +{MAX_DAYS} -delete'
os.system(find_cmd)
# executes find_cmd in terminal, checks whether there are outdated files
