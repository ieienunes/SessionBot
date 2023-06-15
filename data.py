from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("❣️ Gerar Session ❣️", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" 🥀 ʙᴀᴄᴋ 🥀 ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Desenvolvedor  ✨", url="https://t.me/ondanegra")],
        [
            InlineKeyboardButton(" ❔ Ajuda ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Sobre 🎪", callback_data="about")
        ],
        
    ]

    START = """
Hᴏɪ {}

Tʜɪs ɪs {}

Gerador Sessions Telegram Para Telethon

por : [Onda](https://t.me/ondanegra)
    """

    HELP = """
✨ **Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs** ✨

/about - Aʙᴏᴜᴛ Tʜᴇ Bᴏᴛ
/help - Tʜɪs Mᴇssᴀɢᴇ
/start - Sᴛᴀʀᴛ ᴛʜᴇ Bᴏᴛ
/generate - Gᴇɴᴇʀᴀᴛᴇ Sᴇssɪᴏɴ
/cancel - Cᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - Cᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    ABOUT = """
**Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ** 
  
  T
  Bot Telegram Gerador progama e telethon string
  
  Fʀᴀᴍᴇᴡᴏʀᴋ : [Pʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)
  
  Lᴀɴɢᴜᴀɢᴇ : [Pʏᴛʜᴏɴ](https://www.python.org)
  
  Dᴇᴠᴇʟᴏᴘᴇʀ : [Λnanya](https://t.me/anu_pi)
      """
