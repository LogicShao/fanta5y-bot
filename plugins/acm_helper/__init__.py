from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

from .OJ_helper.helper import AcmHelper
from .handler import Handler


# register the matcher: acm_helper
acmHelperMatcher = on_command(
    "acm_helper",
    rule=to_me(),
    priority=10,
    block=True
)

# register the matcher: codeforces
codeforcesMatcher = on_command(
    "codeforces",
    rule=to_me(),
    priority=10,
    block=True
)

# register the matcher: luogu
luoguMatcher = on_command(
    "luogu",
    rule=to_me(),
    priority=11,
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
async def acmHandle(event) -> None:
    # create the handler
    handler.updateArgs(str(event.get_message()).strip().split())

    # handle the event
    await handler.handle()


# handle the command
@codeforcesMatcher.handle()
async def codeforcesHandle(event) -> None:
    # get the args
    args = str(event.get_message()).strip().split()[1:]
    # get the user info
    if len(args) != 1:
        await codeforcesMatcher.finish("Invalid arguments")
    # handle the event
    if args[0] == 'contests':
        # get the approaching contests
        contestsInfo: str = acmHelper.codeforcesHelper.getApproachingContests()
        await codeforcesMatcher.finish(contestsInfo)
    else:
        # get the user info
        userInfo = acmHelper.codeforcesHelper.getUserInfo(args[0])
        await codeforcesMatcher.finish(str(userInfo))


@luoguMatcher.handle()
async def getLuoguUserInfo(event) -> None:
    # get the args
    args = str(event.get_message()).strip().split()[1:]
    # get the user info
    if len(args) != 1:
        await luoguMatcher.finish("Invalid arguments")
    # get the user info
    userInfo = acmHelper.luoguHelper.getUserInfo(args[0])
    await luoguMatcher.finish(str(userInfo))


__plugin_meta__ = PluginMetadata(
    name="ACM_Helper",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

