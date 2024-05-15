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

codeforcesHelperCmd = on_command(
    "codeforces",
    rule=to_me(),
    priority=10,
    block=True
)

luoguHelperCmd = on_command(
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
async def handle(event) -> None:
    # create the handler
    handler.updateArgs(str(event.get_message()).strip().split())

    # handle the event
    await handler.handle()


# handle the command
@codeforcesHelperCmd.handle()
async def get_ac_submissions(event) -> None:
    # get the username
    username = str(event.get_message()).strip().split(' ')[-1]
    # 下面检测空字段的代码其实没用,但是这里想写的话可以写的东西太多了,空字段,多字段...我先注释掉了
    '''if not username:
        await acmHelperCmd.finish("请输入用户名")'''
    
    # get the solved submissions from codeforces
    solved_problems = acmHelper.get_online_judge_accepted_submissions(username, 'codeforces')

    # return the result
    # infor_str = "用户 {username} 在 codeforces 上的 AC 提交数为 {ac_num}".format(username=username, ac_num=len(ac_submissions))
    infor_str = "用户 {username} 在 codeforces 上的 AC 提交数为 {ac_num}".format(username=username, ac_num=len(solved_problems))
    await codeforcesHelperCmd.finish(infor_str)


@luoguHelperCmd.handle()
async def getLuoguUserInfo(event) -> None:
    # get the uid
    uid = str(event.get_message()).strip().split()[-1]
    # get the user info
    userInfo = acmHelper.getUserInfo(uid, 'luogu')
    # return the user info
    await luoguHelperCmd.finish(str(userInfo))


__plugin_meta__ = PluginMetadata(
    name="ACM_Helper",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

