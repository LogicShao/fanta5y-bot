from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me


self_intro = on_command(
    "whoami",
    rule=to_me(),
    aliases={"自我介绍", "介绍自己"},
    priority=10,
    block=True
)


async def get_self_intro():
    infor_str = "我是御坂0x3f3f3f3f号，一个不存在的御坂妹。我的主人是@Eternal_Fanta5y。"
    return infor_str


@self_intro.handle()
async def handle_function():
    self_intro_info = await get_self_intro()
    await self_intro.finish(self_intro_info)

__plugin_meta__ = PluginMetadata(
    name="self_intro",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)
