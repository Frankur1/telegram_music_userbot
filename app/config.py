import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# чат, куда бот будет отправлять напоминания
TARGET_CHAT = "p6jDlRYdgIllNDU6"    # invite hash

REMINDER_HOUR = 10
REMINDER_MINUTE = 0
TIMEZONE = "Etc/GMT-4"   # Армения UTC+4
