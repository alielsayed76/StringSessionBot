from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🔥 اضغط لبدا استخراج الكود 🔥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 رجوع", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "✨ Dev Ali ✨", url="https://t.me/G5_7B"
            )
        ],
        [
            InlineKeyboardButton("🤔 طريقة الاستخدام 🤔", callback_data="help"),
            InlineKeyboardButton("🎪 معلومات 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("💌 قناة السورس 💌", url="https://t.me/G5_7A")],
    ]

    START = """
هلو {}
اهلا بك في {}
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت
ʙʏ @G5_7A
    """

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/repo - ɢᴇᴛ ʀᴇᴘᴏ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @G5_7A 

السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/G5_7A)
المكاتب : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغه : [ᴘʏᴛʜᴏɴ](www.python.org)
المالك : @G5_7B 
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️Abo Elmaged 🔥
━━━━━━━━━━━━━━━━━
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ المطور [Ali](https://t.me/G5_7B)
┣★ للعظمة  [ʜᴇᴀʀᴛ ❤️](https://t.me/G5_7A)
┣★ بار التيم [رغي](https://t.me/G5_7F)
┣★ السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/G5_7A)
┣★ بار السورس [Abo Elmaged team](https://t.me/G5_7F)
┗━━━━━━━━━━━━━━━━━┛
💞 
لو عند اساله تعاله بف » TO » MY » [OWNER] @G5_7B 
   """
