from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

from .helper.helper import ACMHelper


# register the command
acmHelperCmd = on_command(
    "acm_helper",
    rule=to_me(),
    priority=10,
    block=True
)

# create the helper
acmHelper = ACMHelper()

# handle the command
@acmHelperCmd.handle()
async def get_ac_submissions(bot, event) -> None:
    # get the username
    username = str(event.get_message()).strip().split(' ')[-1]
    # 下面检测空字段的代码其实没用,但是这里想写的话可以写的东西太多了,空字段,多字段...我先注释掉了
    '''if not username:
        await acmHelperCmd.finish("请输入用户名")'''
    
    # get the accepted submissions from codeforces
    # ac_submissions = acmHelper.get_online_judge_accepted_submissions(username, 'codeforces')
    solved_problems = acmHelper.get_online_judge_accepted_submissions(username, 'codeforces')

    
    # return the result
    # infor_str = "用户 {username} 在 codeforces 上的 AC 提交数为 {ac_num}".format(username=username, ac_num=len(ac_submissions))
    infor_str = "用户 {username} 在 codeforces 上的 AC 提交数为 {ac_num}".format(username=username, ac_num=len(solved_problems))
    await acmHelperCmd.finish(infor_str)


__plugin_meta__ = PluginMetadata(
    name="ACM_Helper",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

