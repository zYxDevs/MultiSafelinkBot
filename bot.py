from os import environ
from requests import get
from pyrogram import Client, filters

API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
AUTH_USERS = {int(x) for x in environ.get("AUTH_USERS").split()}
DLINK_KEY = environ.get("DLINK_KEY", None)
SNACKLINK_KEY = environ.get("SNACKLINK_KEY", None)
ADTIVAL_KEY = environ.get("ADTIVAL_KEY", None)
SHRINKADS_KEY = environ.get("SHRINKADS_KEY", None)
ZAGL_KEY = environ.get("ZAGL_KEY", None)
YOUSHORT_KEY = environ.get("YOUSHORT_KEY", None)
PFL_KEY = environ.get("PFL_KEY", None)
SEARN_KEY = environ.get("SEARN_KEY", None)
CFLY_KEY = environ.get("CFLY_KEY", None)
SHZON_KEY = environ.get("SHZON_KEY", None)
CLKSH_KEY = environ.get("CLKSH_KEY", None)


bot = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


@bot.on_message(filters.command(["start", "help"]) & ~filters.edited)
async def start(_, message):
    await message.reply(
        f"""**Hi {message.chat.first_name}!**
I'm **MultiSafelinkBot**, Just send me a link with some command below.

**Here is my command:**
/adtival <link> - Get a shortlink using adtival
/cfly <link> - Get a shortlink using clicksfly
/clksh <link> - Get a shortlink using clksh
/dlink <link> - Get a shortlink using droplink
/sads <link> - Get a shortlink using shrinkads
/sarn <link> - Get a shortlink using shrinkearn
/snack <link> - Get a shortlink using snacklink
/shzon <link> - Get a shortlink using shortzon
/pfl <link> - Get a shortlink using paid4link
/yshort <link> - Get a shortlink using yourshort
/zagl <link> - Get a shortlink using zagl

More features will added soon:)

**Join here:**
@YBotsSupport
@SpreadNetworks

Maintenance by @Yoga_CIC"""
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
            "Get `ADTIVAL_KEY` from [adtival](https://www.adtival.network/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://www.adtival.network/api?api={ADTIVAL_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
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
            "Get `DLINK_KEY` from [droplink](https://droplink.co/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://droplink.co/api?api={DLINK_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
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
            "Get `SNACKLINK_KEY` from [snacklink](https://snacklink.co/ref/AdamLuwis) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        short_link = "https://ponselharian.com/st/?api={SNACKLINK_KEY}&url={link}"
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
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
            "Get `SHRINKADS_KEY` from [shrinkads](https://www.shrinkads.com/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://www.shrinkads.com/api?api={SHRINKADS_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("zagl") & ~filters.edited)
async def zagl_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if ZAGL_KEY is None:
        return await message.reply(
            "Get `ZAGL_KEY` from [zagl](https://zee.gl/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://za.gl/api?api={ZAGL_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("yshort") & ~filters.edited)
async def yshort_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if YOUSHORT_KEY is None:
        return await message.reply(
            "Get `YOUSHORT_KEY` from [youshort](https://youshort.me/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://youshort.me/api?api={YOUSHORT_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("pfl") & ~filters.edited)
async def pfl_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if PFL_KEY is None:
        return await message.reply(
            "Get `PFL_KEY` from [paid4link](https://paid4link.com/ref/zYxDevs) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://paid4link.com/api?api={PFL_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("sarn") & ~filters.edited)
async def searn_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if SEARN_KEY is None:
        return await message.reply(
            "Get `SEARN_KEY` from [shrinkearn](https://shrinkearn.com/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://shrinkearn.com/api?api={SEARN_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("cfly") & ~filters.edited)
async def cfly_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if CFLY_KEY is None:
        return await message.reply(
            "Get `CFLY_KEY` from [clicksfly](https://clicksfly.com/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://clicksfly.com/api?api={CFLY_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("shzon") & ~filters.edited)
async def shzon_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if SHZON_KEY is None:
        return await message.reply(
            "Get `SHZON_KEY` from [shortzon](https://shortzon.com/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://shortzon.com/api?api={SHZON_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


@bot.on_message(filters.command("clksh") & ~filters.edited)
async def clksh_handler(_, message):
    if len(message.command) < 2:
        return await message.reply("Give me url to short!")
    if message.from_user.id not in AUTH_USERS:
        return await message.reply(
            "You are not allowed to use me!\n\nContact @Yoga_CIC"
        )
    if CLKSH_KEY is None:
        return await message.reply(
            "Get `CLKSH_KEY` from [clksh](https://clk.sh/ref/YogaPranata) and fill it on vars!",
            disable_web_page_preview=True,
        )
    link = message.text.split(None, 1)[1].strip()
    link = link.replace(" ", "")
    try:
        r = get(f"https://clk.sh/api?api={CLKSH_KEY}&url={link}").json()
        short_link = r["shortenedUrl"]
        return await message.reply(
            f"""Click to copy:\n\n<code>{short_link}</code>.\n\nHere is your [short link]({short_link}).""",
            quote=True,
            disable_web_page_preview=True,
        )
    except Exception as e:
        return await message.reply(f"Error: {e}\n\nReport to @Yoga_CIC", quote=True)


bot.run()
