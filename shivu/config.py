class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "2061656269"
    sudo_users = "2061656269"
    GROUP_ID = -1002237016385
    TOKEN = "7248959755:AAFjDhuxqoOIw0492tYbk7BCu4wpN9I-nCQ"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Ekdkekdekdke_bot"
    CHARA_CHANNEL_ID = "-1002237016385"
    api_id = 20478011
    api_hash = "0e4dcf39643e83c3c174a0d2370e5b4a"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
