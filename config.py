#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6950294857:AAF7BOUVCswz3TnFnhLzPJggCiNWNTL81Wk")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7685644"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a713f30f5a21716e6bff334e8ac19b17")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001862263552"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1854576276"))

#Port
PORT = os.environ.get("PORT", "8220")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nas20221996:nayaungsoe14@cluster0.pgedpqc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nရုပ်ရှင်များပို့ပေးတဲ့ Bot ဖြစ်ပါတယ်😁😁")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1854576276 1457995605").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>ရုပ်ရှင်ရရှိဖို့အတွက် ဒီချန်နယ်လေးကိုJoinထားရမှာပါနော်😊\n\nKindly Please join Channel😇😇</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Bot ကိုစာပို့လို့မရပါဘူးနော်😅။ရုပ်ရှင်သီးသန့်ပဲပို့ပေးတာပါ။"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
