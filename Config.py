import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29877739")
    API_HASH = os.environ.get("API_HASH", "ea18f22aab7d5c09e784d5dbc607edd3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5965084738:AAEREPx_tYGX469CY9SoLdlmbUMxsyABLrU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLcBuw428AfH1dHruy7nSSKGVkRDo7_n3KSvU9tm3svXThbwiQQb6rlWgt7kRPZwSV5Tm9IEdjt8wefCGKuojXmWuQnK5OyyNirUoMA5xXkVtE8q2RItVHkWvXQYtlifsMRBikJCRyOpx9zilYaczHSHuhBqqlbSE2dcwLBrJ59UgAeU3FAZxNA0Hh5ctgD65wEDbKEOz5G0EDzIbhvGGu7iy2zokcLP0f0CKaxMd6GeygtRqSZftxsyDGIOAWgGjPE0_e55bqOy6REA4glshGGrx5UH0srdc7trDodHAhRc6nf0N6XozGien4XVMnXDUj5PRGTqkAdI-S_hrQK9KQbe-eM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Et3rn_MuSic_Bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5883862005")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
