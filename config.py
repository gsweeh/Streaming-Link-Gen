import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2022219715:AAG6r4RuYaLnG-Fmib6MKl4cHDU9AnQrOvU")
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 2923258))
    API_HASH = os.environ.get("API_HASH", "4c843703f04453d401e32b130e7425f5")
    # Your Updates channel username 
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", https://t.me/Movie_leecher)
    # token.pickle file link
    TOKEN_PICKLE = os.environ.get("TOKEN_PICKLE", https://fxstream.herokuapp.com/29556)
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Google drive folder id
    parent_id = os.environ.get("GDRIVE_FOLDER_ID", "0AAyyYrqhIe2qUk9PVA")
    # Set True is drive folder id is Team Drive
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", "True")
    if IS_TEAM_DRIVE.lower() == 'true':
        IS_TEAM_DRIVE = True
    else:
        IS_TEAM_DRIVE = False
    # Set it True if using Service Account for uploading
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS", "False")
    if USE_SERVICE_ACCOUNTS.lower() == 'true':
        USE_SERVICE_ACCOUNTS = True
    else:
        USE_SERVICE_ACCOUNTS = False
    # Your gdrive index url (Important)
    INDEX_URL = os.environ.get("INDEX_URL", "https://movieleecher.movieleecher.workers.dev/0")
