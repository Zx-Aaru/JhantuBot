from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from SONALI_MUSIC import app

class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("ᴄʜᴧᴛ-ɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
            InlineKeyboardButton("ᴧᴄᴛɪon", callback_data="TOOL_BACK HELP_14"),
            InlineKeyboardButton("ᴄᴏᴜᴘʟᴇs", callback_data="TOOL_BACK HELP_08"),
        ],
        [
            InlineKeyboardButton("sᴇᴧʀᴄʜ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("ᴛʀᴧɴsʟᴧᴛᴇ", callback_data="TOOL_BACK HELP_24"),
            InlineKeyboardButton("ɪɴꜰᴏ", callback_data="TOOL_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ꜰᴏɴᴛ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("ᴡʜɪsᴘᴇʀ", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("ᴛᴧɢᴧʟʟ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ꜰᴜɴ", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("ǫυᴏᴛʟʏ", callback_data="TOOL_BACK HELP_12"),
            InlineKeyboardButton("ᴛ-ɢʀᴧᴘʜ", callback_data="TOOL_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("ɢᴧᴍᴇ", callback_data="TOOL_BACK HELP_21"),
            InlineKeyboardButton("sᴇᴛᴜᴘ", callback_data="TOOL_BACK HELP_17"),
            InlineKeyboardButton("sᴧɴɢᴍᴧᴛᴧ", callback_data="TOOL_BACK HELP_23"),
        ],
        [
            InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="TOOL_BACK HELP_25"),
            InlineKeyboardButton("ʙᴧᴄᴋ", callback_data=f"MAIN_CP"),
            InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="TOOL_BACK HELP_10"),
        ]
    ]

    



    
    ALPHABUTTON = [
        [
            InlineKeyboardButton("ᴧɪ | ᴄʜᴧᴛɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
        ],
        [
            InlineKeyboardButton("sᴇᴧʀᴄʜ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("ᴛᴛs", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("ɪɴꜰᴏ", callback_data="TOOL_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ꜰᴏɴᴛ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("ᴍᴧᴛʜ", callback_data="TOOL_BACK HELP_06"),
            InlineKeyboardButton("ᴛᴧɢᴧʟʟ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ɪᴍᴧɢᴇ", callback_data="TOOL_BACK HELP_08"),
            InlineKeyboardButton("ʜᴧsᴛᴧɢ", callback_data="TOOL_BACK HELP_09"),
            InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="TOOL_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("ꜰᴜɴ", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("ǫυᴏᴛʟʏ", callback_data="TOOL_BACK HELP_12"),
            InlineKeyboardButton("ᴛ-ᴅ", callback_data="TOOL_BACK HELP_13"),
        ],
        [   
            InlineKeyboardButton("ʙᴧᴄᴋ", callback_data=f"MAIN_CP"),]
        ]
    
    MBUTTON = [
                [
            InlineKeyboardButton("ᴇxᴛʀᴧ", callback_data="MANAGEMENT_BACK HELP_25"),
        ],
        [
            InlineKeyboardButton("ʙᴧɴ", callback_data="MANAGEMENT_BACK HELP_14"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="MANAGEMENT_BACK HELP_15"),
            InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="MANAGEMENT_BACK HELP_16"),
        ],
        [
            InlineKeyboardButton("ᴘɪɴ", callback_data="MANAGEMENT_BACK HELP_17"),
            InlineKeyboardButton("sᴛꜰꜰ", callback_data="MANAGEMENT_BACK HELP_18"),
            InlineKeyboardButton("sᴇᴛ-υᴘ", callback_data="MANAGEMENT_BACK HELP_19"),
        ],
        [
            InlineKeyboardButton("ᴢᴏᴍʙɪᴇ", callback_data="MANAGEMENT_BACK HELP_20"),
            InlineKeyboardButton("ɢᴧᴍᴇ", callback_data="MANAGEMENT_BACK HELP_21"),
            InlineKeyboardButton("ɪᴍᴘᴏsᴛᴇʀ", callback_data="MANAGEMENT_BACK HELP_22"),
        ],
        [
            InlineKeyboardButton("sɢ", callback_data="MANAGEMENT_BACK HELP_23"),
            InlineKeyboardButton("ᴛʀ", callback_data="MANAGEMENT_BACK HELP_24"),
            InlineKeyboardButton("ɢʀᴧᴘʜ", callback_data="MANAGEMENT_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("ʙᴧᴄᴋ", callback_data=f"MAIN_CP"), 
        ]
        ]
    PBUTTON = [
        [
            InlineKeyboardButton("- ᴋ ᴧ ʀ ᴍ ᴧ › ᴏᴘ 𝃵⎯̽⇢🎫", url="https://t.me/Swagger_Soul")
        ],
        [
            InlineKeyboardButton("ʙᴧᴄᴋ", callback_data="MAIN_CP"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("⌯ sυᴘᴘᴏʀᴛ ⌯", url="https://t.me/AarumiChat"),
            InlineKeyboardButton("⌯ υᴘᴅᴧᴛᴇs ⌯", url="https://t.me/AarumiBots"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
        [
            InlineKeyboardButton("ᴍᴜѕɪᴄ", callback_data="settings_back_helper"),
            InlineKeyboardButton("ᴍᴧɴᴧɢᴇᴍᴇɴᴛ", callback_data="TOOL_CP"),
        ],
        [
            InlineKeyboardButton("ᴧʟʟ ʙᴏᴛ's", callback_data="MAIN_BACK HELP_ABOUT"),
            InlineKeyboardButton("ᴘʀᴏᴍᴏᴛɪᴏɴ", callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("ʙᴧᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="settingsback_helper"),
            
        ]
        ]



