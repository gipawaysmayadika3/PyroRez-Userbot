# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from ProjectMan import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from ProjectMan.helpers.misc import git, heroku

MSG_ON = """
🔥 **PyroRez-Userbot udah nyala anjing🔥**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}Rez` **untuk Mengecheck Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("musikku21")
            await bot.join_chat("SharingUserbot")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("RezaProject").info("Starting RezaProject")
    LOGGER("RezaProject").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("RezaProject").info(f"RezaProject v{BOT_VER} [🔥 Reza userbot sudah aktif masse! 🔥]")
    LOOP.run_until_complete(main())
