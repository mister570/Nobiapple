from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),   
        ],[InlineKeyboardButton(text="👑✨ 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ✨👑", callback_data="settings_back_helper")],
        #[InlineKeyboardButton(text=_["ST_B_3"], callback_data="LG"),],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],        [InlineKeyboardButton(text="👑✨ 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ✨👑", callback_data="settings_back_helper")],
        #[InlineKeyboardButton(text=_["ST_B_3"], callback_data="LG"),],
    ]
    return buttons
