from .OJ_helper.helper import AcmHelper
from typing import Optional
from nonebot.matcher import Matcher
from .OJ_helper.helper import UserInfo


# it using to handle the acm_helper Matcher event
class Handler:
    def __init__(self, acmHelper: AcmHelper, matcher: Matcher, args: Optional[list[str]] = None) -> None:
        # it would accept a list of arguments which is from event.get_message()
        # and store it in self.args
        # the args will remove the first element which is the command itself
        if args is None:
            self.args = []
        else:
            self.args = args[1:]
        # get the number of arguments
        self.cntArgs = len(self.args)

        # set the acmHelper
        self.acmHelper = acmHelper
        # set the matcher
        self.matcher = matcher

    def updateArgs(self, args: list[str]) -> None:
        # update the arguments
        self.args = args[1:]
        self.cntArgs = len(self.args)

    async def handleUserInfo(self) -> None:
        # handle the user information
        # if the arguments are invalid, return "Invalid arguments"
        if self.cntArgs != 2:
            await self.matcher.finish("Invalid arguments")

        username: str = self.args[0]
        onlineJudge: str = self.args[1]
        userInfo: UserInfo = self.acmHelper.getUserInfo(username, onlineJudge)

        await self.matcher.finish(str(userInfo))

    async def handleContests(self) -> None:
        # handle the contests
        # if the arguments are invalid, return "Invalid arguments"
        if self.cntArgs != 0:
            await self.matcher.finish("Invalid arguments")

        contests: list = self.acmHelper.getApproachingContests()
        await self.matcher.finish(str(contests))

    async def handle(self) -> None:
        # handle the arguments and return the result
        # if the arguments are invalid, return "Invalid arguments"
        if self.cntArgs == 0:
            await self.matcher.finish("Invalid arguments")

        if self.cntArgs == 2:
            await self.handleUserInfo()
            return

        if self.args[0] == 'contests':
            await self.handleContests()
            return

        await self.matcher.finish("Invalid arguments")
