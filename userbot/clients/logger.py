# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CLOWN2, CLOWN3, CLOWN4, CLOWN5, bot, branch, tgbot
from userbot.utils import clownscrt

MSG_ON = """
🤡**Clown-Userbot Berhasil Diaktifkan**!!
━━━━━━━━━━━━━━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}ping` **untuk Mengecheck Bot**
━━━━━━━━━━━━━━━
➠ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :** @ChannelClown
"""


async def clown_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            ClownUBOT = await tgbot.get_me()
            BOT_USERNAME = ClownUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            ClownUBOT = await tgbot.get_me()
            BOT_USERNAME = ClownUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await clownscrt(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CLOWN2:
            await clownscrt(CLOWN2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CLOWN2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CLOWN3:
            await clownscrt(CLOWN3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CLOWN3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CLOWN4:
            await clownscrt(CLOWN4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CLOWN4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CLOWN5:
            await clownscrt(CLOWN5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CLOWN5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
