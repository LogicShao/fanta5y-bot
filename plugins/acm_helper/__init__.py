from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

from .OJ_helper import AcmHelper
from .handler import Handler

import requests


# load the port
with open("acmhelper.env", "r") as f:
    file = f.readlines()
    for line in file:
        if line.startswith("port"):
            port = line.split("=")[1].strip()
            break
    else:
        port = None

# check the port
if port is not None and port.isdigit() and 0 <= int(port) <= 65535:
    port = int(port)
else:
    port = None


# register the matcher: acm_helper
acmHelperMatcher = on_command(
    "acm",
    rule=to_me(),
    priority=10,
    block=True
)

# register the matcher: codeforces
codeforcesMatcher = on_command(
    "CF",
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

# register the matcher: nowcoder also nk
nowcoderMatcher = on_command(
    "nk",
    rule=to_me(),
    priority=11,
    block=True
)

# register the matcher: atcoder
atcoderMatcher = on_command(
    "atc",
    rule=to_me(),
    priority=11,
    block=True
)

# create the helper
acmHelper = AcmHelper(port=port)

# create the handler
handler = Handler(
    acmHelper=acmHelper,
    matcher=acmHelperMatcher
)


@acmHelperMatcher.handle()  # handle the command
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
        await codeforcesMatcher.finish("或许你应该输入一个用户名或者向我查询比赛信息。do! 御坂如是说。")
    # handle the event
    if args[0] == 'contests':
        # get the approaching contests
        try:
            contestsInfo: str = acmHelper.codeforcesHelper.getApproachingContestsInfo()
        except requests.Timeout:
            await codeforcesMatcher.finish("似乎请求超时了呢，御坂感到有点困惑。")
        except requests.RequestException as e:
            await codeforcesMatcher.finish("请求失败，御坂感到抱歉...")

        await codeforcesMatcher.finish(contestsInfo)
    else:
        # get the user info
        try:
            userInfo = acmHelper.codeforcesHelper.getUserInfo(args[0])
        except requests.Timeout:
            await codeforcesMatcher.finish("似乎请求超时了呢，御坂感到有点困惑。")
        except requests.RequestException as e:
            await codeforcesMatcher.finish("请求失败，御坂感到抱歉...")

        await codeforcesMatcher.finish(str(userInfo))


@luoguMatcher.handle()
async def getLuoguUserInfo(event) -> None:
    # get the args
    args = str(event.get_message()).strip().split()[1:]
    # get the user info
    if len(args) != 1:
        await luoguMatcher.finish("或许你应该输入一个用户名或者向我查询比赛信息。do! 御坂如是说。")
    # handle the event
    if args[0] == 'contests':
        # get the approaching contests
        contestsInfo: str = acmHelper.luoguHelper.getApproachingContestsInfo()
        await luoguMatcher.finish(contestsInfo)
    else:
        # get the user info
        userInfo = acmHelper.luoguHelper.getUserInfo(args[0])
        await luoguMatcher.finish(str(userInfo))


@nowcoderMatcher.handle()
async def getNowCoderUserInfo(event) -> None:
    # get the args
    args = str(event.get_message()).strip().split()[1:]
    # get the user info
    if len(args) != 1:
        await nowcoderMatcher.finish("或许你应该输入一个用户名或者向我查询比赛信息。do! 御坂如是说。")
    # handle the event
    if args[0] == 'contests':
        # get the approaching contests
        contestsInfo: str = acmHelper.nowCoderHelper.getApproachingContestsInfo()
        await nowcoderMatcher.finish(contestsInfo)
    else:
        # get the user info
        userInfo = acmHelper.nowCoderHelper.getUserInfo(args[0])
        await nowcoderMatcher.finish(str(userInfo))


@atcoderMatcher.handle()
async def getAtCoderUserInfo(event) -> None:
    # get the args
    args = str(event.get_message()).strip().split()[1:]
    # get the user info
    if len(args) != 1:
        await atcoderMatcher.finish("或许你应该输入一个用户名或者向我查询比赛信息。do! 御坂如是说。")
    # handle the event
    if args[0] == 'contests':
        # get the approaching contests
        contestsInfo: str = acmHelper.atCoderHelper.getApproachingContestsInfo().removesuffix('\n')
        await atcoderMatcher.finish(contestsInfo)
    else:
        # get the user info
        userInfo = acmHelper.atCoderHelper.getUserInfo(args[0])
        await atcoderMatcher.finish(str(userInfo))


__plugin_meta__ = PluginMetadata(
    name="ACM_Helper",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)
