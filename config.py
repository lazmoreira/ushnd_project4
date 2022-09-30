import os
#import urllib.parse 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ushndstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'A2FbsBDwAHwahjcSnI9VzTGInX2dBZtVhPxhzM1gnIJteBYtg/GdWhOESUM5nffaOovHrz3isHzd+AStlShnhw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ushnd-sql-database.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ushnd-sql-database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'lazoadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Thunderbolt@13'

    #Local setup
    #params = urllib.parse.quote_plus("DRIVER={SQL Server};"+f"SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USER_NAME};PWD={SQL_PASSWORD}")
    #SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = ".Gg8Q~_5.SSBZf83IrsDtTvEDPVJ~3thP8xg-ajY"
    #VALUE: .Gg8Q~_5.SSBZf83IrsDtTvEDPVJ~3thP8xg-ajY
    #SECRETID: de3790e8-dd66-49e8-b336-92510e88dee1
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/cab89e55-6750-4a18-a435-adeda2d4b339"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "0e5870ff-1dde-4853-bf3f-a7146267146e"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session