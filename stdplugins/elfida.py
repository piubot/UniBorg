"""Emoji

Available Commands:

.e"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "e":
        await event.edit(input_str)
        animation_chars = [
            "ⒺⓁⒻⒾⒹⒶ",
            "🅔🅛🅕🅘🅓🅐",
            "ɆⱠ₣łĐ₳",
            "E҉L҉F҉I҉D҉A҉",
            "єℓfι∂α*",
            "ĔĹŦĨĎĂ",
            "εℓғι∂α",
            "ᗴᒪᖴᎥᗪᗩ",
            "€ℓƒɨďą",
            "£Ƚƒȋďå",
            "ᙍᒪᖴᓿᗫᗅ",
            "ҽӀƒíժɑ",
            "ꏂ꒒ꄟ꒐ꂟꋬ",
            "ȝʅԲɿԺԹ",
            "ᘿᒪᖴᓰᕲᗩ",
            "ꍟ꒒ꎇꀤꀸꍏ",
            "ỆĿḞÏĎÄ",
            "🄴🄻🄵🄸🄳🄰",
            "E̷L̷F̷I̷D̷A̷",
            "E͓̽L͓̽F͓̽I͓̽D͓̽A͓̽",
            "E̶L̶F̶I̶D̶A̶",
            "E̴L̴F̴I̴D̴A̴",
            "ᏋᏝᎦᎥᎴᏗ",
            "ＥＬＦＩＤＡ",
            "E͓̽L͓̽F͓̽I͓̽D͓̽A͓̽",
            "**♛__ᎬᏞfᎥᎠᎪ__😎♛**"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
