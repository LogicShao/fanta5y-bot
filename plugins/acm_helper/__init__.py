from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

from .OJ_helper.helper import AcmHelper
from .handler import Handler


# register the command
acmHelperMatcher = on_command(
    "acm_helper",
    rule=to_me(),
    priority=10,
    block=True
)

# create the helper
acmHelper = AcmHelper()

# create the handler
handler = Handler(
    acmHelper=acmHelper,
    matcher=acmHelperMatcher
)

# handle the command
@acmHelperMatcher.handle()
async def handle(event) -> None:
    # create the handler
    handler.updateArgs(str(event.get_message()).split())

    # handle the event
    await handler.handle()


__plugin_meta__ = PluginMetadata(
    name="ACM_Helper",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

