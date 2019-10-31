from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd("ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("pinging............")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("My bot is working \nperfectly.....  😎\nat speed of  \n{} 🚀gb/s".format(ms))
