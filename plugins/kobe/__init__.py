from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_message

# register the command
kobe = on_message(
    priority=15,
    block=True
)

# 将要匹配的字符串列表
match_strings = ['老大','牢大','我没意见','我有意见','坠机','直升机','肘击','别肘','想我了吗','我回来了','孩子','what can i say','whatcanisay','manba','曼巴','想你了','24','闪电旋风劈','极空寒冰砍','天宇屠龙舞','泰山陨石坠','man']

@kobe.handle()
async def handle_message(bot, event) -> None:
    message = str(event.get_message()).lower()  # 获取消息内容
    username = event.sender.nickname
    if any(word in message for word in match_strings):
        infor_str = ("孩子们，特别是你 @{username}，这并不好笑").format(username=username)
        await kobe.finish(infor_str)

__plugin_meta__ = PluginMetadata(
    name="kobe",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)
