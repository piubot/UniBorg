from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"\.x", outgoing=True))
async def payf(event):
    if event.fwd_from:
        return   
    paytext=event.text[6:]
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.edit(pay)