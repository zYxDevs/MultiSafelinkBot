from os import environ
from requests import get
from pyrogram import Client, filters

API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS").split())
DLINK_KEY = environ.get("DLINK_KEY", None)
SNACKLINK_KEY = environ.get("SNACKLINK_KEY", None)
ADTIVAL_KEY = environ.get("ADTIVAL_KEY", None)
SHRINKADS_KEY = environ.get("SHRINKADS_KEY", None)


bot = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    sleep_threshold=10,
)


@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, message):
    await message.reply(
        f"""**Hi {message.chat.first_name}!**
I'm MultiSafelinkBot. Just send me a link with some command below.

Here is my command:
/start - Start me
/help - See my help
/dlink <link> - Get a shortlink using droplink
/adtival <link> - Get a shortlink using adtival/wtspw
/snack <link> - Get a shortlink using snacklink
/sads <link> - Get a shortlink using shrinkads

More features will added soon

Maintenance by @Yoga_CIC
**Join here:**
@YBotsSupport
@SpreadNetworks"""
    )


@bot.on_message(filters.command(["adtival", "wts"]) & ~filters.edited)
async def adtival_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if ADTIVAL_KEY is None:
        return await message.reply(
            "Get `ADTIVAL_KEY` from adtival.network and fill it on vars!"
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://www.adtival.network/api?api={ADTIVAL_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy - <code>{short_link}</code>.\nHere is your [short link]({short_link})""",
            quote=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("dlink") & ~filters.edited)
async def dlink_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if DLINK_KEY is None:
        return await message.reply(
            "Get `DLINK_KEY` from droplink.co and fill it on vars!"
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://droplink.co/api?api={DLINK_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy - <code>{short_link}</code>.\nHere is your [short link]({short_link})""",
            quote=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("snack") & ~filters.edited)
async def snack_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if SNACKLINK_KEY is None:
        return await message.reply(
            "Get `SNACKLINK_KEY` from snacklink.id and fill it on vars!"
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        short_link = "https://ponselharian.com/st/?api={SNACKLINK_KEY}&url={link}"
        return await message.reply(
            f"""Click to copy - <code>{short_link}</code>.\nHere is your [short link]({short_link})""",
            quote=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("sads") & ~filters.edited)
async def sads_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if SHRINKADS_KEY is None:
        return await message.reply(
            "Get `SHRINKADS_KEY` from snacklink.id and fill it on vars!"
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://www.shrinkads.com/api?api={SHRINKADS_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy - <code>{short_link}</code>.\nHere is your [short link]({short_link})""",
            quote=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


bot.run()
