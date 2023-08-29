# ReadFlow

ReadFlow is an app designed to help organize and mantain libraries across the world.


## CURRENTLY IN DEVELOPMENT

## DEV INFO

Please run the following in your terminal (pointing at ROOT DIRECTORY, make sure your virtual enviroment is activated):

```bash
pip install -r requirements.txt
```

Next, create a .env file in your project's ROOT DIRECTORY. Insert the following data into it:

DB_NAME= database name here
DB_USER= database username here
DB_PASS= database user's password here
DB_PORT= port here (normally 5432)
DB_HOST= host here. Ip address if connecting to external host, otherwise 'localhost'

This will allow environ to read from your file and pass the information to psycopg, that way your database will be connected and you will be ready to work with it.