"""Warn Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("warn0", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    temp = event.text
    warn = temp[6:]
    mentions = "`Your Warnings Have Been Reset To 0...\nReason: "+warn+"`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
    
@borg.on(admin_cmd("warn1", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    temp = event.text
    warn = temp[6:]
    warncount=0
    warncount = warncount+1
    mentions = "`You Have "+str(warncount)+"/3  Warnings...\nWatch Out!....\nReason For Last Warn: "+warn+"`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("warn2", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    temp = event.text
    warn = temp[6:]
    warncount=1
    warncount = warncount+1
    mentions = "`You Have "+str(warncount)+"/3  Warnings...\nWatch Out!....\nReason For Last Warn: "+warn+"`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("warn3", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    temp = event.text
    warn = temp[6:]
    warncount=2
    warncount = warncount+1
    mentions = "`You Have "+str(warncount)+"/3  Warnings...\nYou Are Muted!!!....\nReason For Last Warn: "+warn+"`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("gbun", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    temp = event.text
    gbun = temp[5:]
    mentions = "`Warning!! User has been 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By @Muttahir...\nReason For Gban: "+gbun+"`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
