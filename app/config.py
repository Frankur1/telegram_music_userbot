import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# Группа, куда бот будет писать напоминания
TARGET_CHAT = "p6jDlRYdgIllNDU6"  # твой invite-link помещение

# Время Армении = UTC+4
REMINDER_HOUR = 10
REMINDER_MINUTE = 0
TIMEZONE = "Etc/GMT-4"  # UTC+4 наоборот записывается как -4
