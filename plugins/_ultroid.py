
from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
▢ **Zydn UBot** •\n
▢ Owner - [Klik disini](https://t.me/CouldNotFoundUser)
▢ Group - [Klik disini](https://t.me/JooxSupport)
▢ Support - @JooxSupport
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://t.me/JooxSupport"),
        Button.url("Developer", "https://t.me/CouldNotFoundUser"),
    ],
    [Button.url("Support Group", "t.me/JooxSupport")],
]

ULTSTRING = """🎇 **Thanks for Deploying Zydn Ubot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="Image URL: https://mallucampaign.in/images/img_1712083086.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Kilik Disini!]({msg.message_link})**")
