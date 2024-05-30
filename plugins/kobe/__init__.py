from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot.adapters.console import Message, MessageSegment

from .config import Config
from nonebot import on_message


# register the command
kobe = on_message(
    priority=15,
    block=True
)

# 将要匹配的字符串列表
match_strings = ['老大', '牢大','我没意见','我有意见','坠机','直升机','肘击','别肘','想我了吗','我回来了','孩子','what can i say','whatcanisay','manba','曼巴','想你了','24','闪电旋风劈','极空寒冰砍','天宇屠龙舞','泰山陨石坠','man']

@kobe.handle()
async def handle_message(bot, event) -> None:
    message: Message = event.get_message()
    message: str = message.extract_plain_text().lower()
    username = event.get_user_id()
    matchedWords = list(filter(lambda x: x in message, match_strings))
    if len(matchedWords) > 0:
        infor_str = "检测到关键词 {matchedWords}。御坂想说：孩子们，特别是你 @{username}，这并不好笑".format(matchedWords=' '.join(matchedWords), username=username)
        await kobe.finish(infor_str)

__plugin_meta__ = PluginMetadata(
    name="kobe",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)
