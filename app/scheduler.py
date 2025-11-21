from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timedelta
from storage import load_posts
from config import TARGET_CHAT
import pytz

ARM_TZ = pytz.timezone("Etc/GMT-4")

scheduler = AsyncIOScheduler()

async def send_reminder(bot):
    msg = (
        "Սիրելիներ, հիշեցում ենք անում, որ այսօր ժամը 22:00 "
        "կունենանք աղոթքի ժամանակ։ Թող Տիրոջ խաղաղությունը լինի բոլորիդ վրա։"
    )
    await bot.send_message(TARGET_CHAT, msg)

async def check_posts(bot):
    posts = load_posts()
    today = datetime.now(ARM_TZ).date()

    for d in posts:
        date_obj = datetime.strptime(d, "%Y-%m-%d").date()

        if today == date_obj - timedelta(days=3):
            await bot.send_message(
                TARGET_CHAT,
                "Սիրելիներ, երեք օրից միասին մտնում ենք ծոմի։"
            )

        if today == date_obj - timedelta(days=1):
            await bot.send_message(
                TARGET_CHAT,
                "Վաղը մեր համատեղ ծոմի օրն է։"
            )

        if today == date_obj:
            await bot.send_message(
                TARGET_CHAT,
                "Այսօր մեր ծոմի օրն է։ Հանդիպումը՝ ժամը 17:00։"
            )

def setup_schedulers(bot):
    scheduler.add_job(
        send_reminder,
        CronTrigger(day_of_week='thu', hour=10, minute=0, timezone=ARM_TZ),
        args=[bot]
    )

    scheduler.add_job(
        check_posts,
        CronTrigger(hour=0, minute=5, timezone=ARM_TZ),
        args=[bot]
    )

    scheduler.start()
