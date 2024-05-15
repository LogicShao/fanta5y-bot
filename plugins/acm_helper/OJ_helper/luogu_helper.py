from .OJ_helper import OJHelper
from .userinfo import UserInfo

import requests

class LuoguHelper(OJHelper):
    def getData(self, uid: str) -> dict:
        # get the general data of the user
        url: str = 'https://www.luogu.com.cn/user/{uid}?_contentOnly=1'.format(uid=uid)
        headers : dict = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36", 
        }
        response: requests.Response = requests.get(url, headers=headers, proxies=self.proxies)
        response.raise_for_status()
        return response.json()

    def getInfo(self, uid: str) -> list:
        # extract the list of solved problems
        data = self.getData(uid)
        # get the user info
        # info[0] is the username
        # info[1:] is the list of solved problems
        info = [data['currentData']['user']['name']] + data['currentData']['passedProblems']
        return info

    def getSolvedProblems(self, uid: str) -> list:
        return self.getInfo(uid)[1:]

    def getUserInfo(self, uid: str) -> UserInfo:
        # get the user info
        info = self.getInfo(uid)
        return UserInfo(
            username=info[0],
            onlineJudge='luogu',
            solvedProblems=len(info[1:])
        )