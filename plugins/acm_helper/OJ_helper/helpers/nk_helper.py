from .OJ_helper import OJHelper
from ..infoClass.userinfo import UserInfo

import requests


class NowCoderHelper(OJHelper):
    # NowCoder API doc is here: https://ac.nowcoder.com/help
    def getData(self, uid: str) -> dict:
        # get the general data of the user
        url: str = 'https://ac.nowcoder.com/acm/contest/profile/{uid}'.format(uid=uid)
        headers: dict = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36",
        }
        response: requests.Response = requests.get(url, headers=headers, proxies=self.proxies)
        response.raise_for_status()
        return response.json()

    def getInfo(self, uid: str) -> list:
        # extract the list of solved problems
        data = self.getData(uid)
        # check if the user exists
        if 'username' not in data:
            return [None]
        # get the user info
        info: list = [data['username']]
        # get the solved problems
        solvedProblems: list = data['solvedProblems']
        for problem in solvedProblems:
            info.append(problem['pid'])
        return info

    def getSolvedProblems(self, uid: str) -> list:
        return self.getInfo(uid)[1:]

    def getUserInfo(self, uid: str) -> UserInfo:
        # check the uid
        if not uid.isdigit():
            return '暂时只支持 uid 查询。do! 御坂如是说。'
        # get the user info
        info = self.getInfo(uid)
        # check if the user exists
        username = info[0]
        if username is None:
            return UserInfo(username=None, onlineJudge='NowCoder')

        return UserInfo(
            username=info[0],
            onlineJudge='NowCoder',
            solvedProblems=len(info[1:])
        )

    def getApproachingContestsInfo(self) -> str:
        return '暂时没有实现 NowCoder 的比赛查询功能。do! 御坂抱歉说。'
