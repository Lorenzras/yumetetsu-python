import os

from dotenv import load_dotenv
load_dotenv()

#TODO
# Refactor redundant code.

def getGroupIdByMailBox(mailBox):
  if (mailBox in ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp"]):
    return os.getenv('SLACK_CHANNEL_ID_FUJISAWA')
  elif (mailBox in ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]):
    return os.getenv('SLACK_CHANNEL_ID_TOYOKAWA')
  else:
    return os.getenv('SLACK_CHANNEL_ID_TEST')

def getAppIdByMailBox(mailBox):
  print("Resolving ID for ", mailBox)

  if (mailBox in ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp"]):
    return os.getenv('KINTONE_APP_ID_FUJISAWA')
  elif (mailBox in ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]):
    return os.getenv('KINTONE_APP_ID_TOYOKAWA')
  else:
    print("Invalid mailbox, defaulting to TEST.")
    return os.getenv('KINTONE_APP_ID_TEST')

def getAppTokenByMailBox(mailBox):
  if (mailBox in ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp"]):
    return os.getenv('KINTONE_APP_TOKEN_FUJISAWA')
  elif (mailBox in ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]):
    return os.getenv('KINTONE_APP_TOKEN_TOYOKAWA')
  else:
    return os.getenv('KINTONE_APP_TOKEN_TEST')