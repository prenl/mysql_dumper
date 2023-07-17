# MySQL Dumper


MySQL Dumper a script for dumping any mysql databases to .sql files

## Installation

> Clone repository to any folder\
> Use the pip3 to install required dependencies ```pip3 install -r requirements.txt```

## Usage

>- Configure your .env file using ```.env.sample``` file\
>- Run file add_to_cron.py using ```python3 add_to_cron.py```\
>- It will add the dump.py to your Cron tasks planner and will execute it every N time. (TIMEOUT constant in .env)\

## Dotenv tips

>- DB_HOST is an IP address of your database, if your database is local just use 127.0.0.1
>- DB_PORT is unnecessary
>- DB_NAME is the name of database that you want to dump
>- DB_USER is your username in MySQL Server (default ```root```)
>- DB_PASSWORD is your user's password for MySQL Server
>- MAX_DAYS is the maximum days for keeeping dump files (autodeletion)
>- TIMEOUT is the time in seconds that defines interval for dump script running
>- DATE_FORMAT is the time format that is used for file name 
>- DIRECTORY is the folder where the dumps will be saved (you can use only folder name and it will be created in the same folder with this repository, or choose your own like ```~/Desktop/...```


## DATE_FORMAT TIPS
>- %d - days
>- %m - months
>- %Y - years
>- %H - hours
>- %M - minutes
>- %S - seconds
