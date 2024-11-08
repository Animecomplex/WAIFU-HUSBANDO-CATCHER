class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "2061656269"
    sudo_users = "2061656269"
    GROUP_ID = -1002258030598
    TOKEN = "7956261083:AAE2tNx5bD6Fb4ZFRm1VbVVbpo3IlxVQFyk"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Chat_Spartan"
    UPDATE_CHAT = "Chat_Spartan"
    BOT_USERNAME = "Sparta_Waifu_bot"
    CHARA_CHANNEL_ID = "-1002258030598"
    api_id = 20478011
    api_hash = "0e4dcf39643e83c3c174a0d2370e5b4a"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
