from .OJ_helper import OJHelper
from ..infoClass.userinfo import UserInfo
from ..infoClass.contestInfo import ContestInfo

import requests

class LuoguHelper(OJHelper):    

    # 返回所有的用户信息 json
    def getUserData(self, uid: str) -> dict:
        url: str = 'https://www.luogu.com.cn/user/{uid}?_contentOnly=1'.format(uid=uid)
        headers : dict = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36", 
        }
        response: requests.Response = requests.get(url, headers=headers, proxies=self.proxies)
        response.raise_for_status()
        return response.json()

    # 返回用户信息 [username, solvedProblems...]
    def getProblemInfo(self, uid: str) -> list:
        # extract the list of solved problems
        data = self.getUserData(uid)
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

    # 返回用户已解决题目列表
    def getSolvedProblems(self, uid: str) -> list:
        return self.getProblemInfo(uid)[1:]

    # 返回用户信息 UserInfo
    def getUserInfo(self, uid: str) -> UserInfo:
        # check the uid
        if not uid.isdigit():
            return '暂时只支持 uid 查询。do! 御坂如是说。'
        # get the user info
        info = self.getProblemInfo(uid)
        # check if the user exists
        username = info[0]
        if username is None:
            return UserInfo(username=None, onlineJudge='luogu')
        
        return UserInfo(
            username=info[0],
            onlineJudge='luogu',
            solvedProblems=len(info[1:])
        )
    
    # 获取即将开始的比赛信息
    def getApproachingContestsInfoList(self) -> list[ContestInfo]:
        url: str = 'https://www.luogu.com.cn/contest/list?_contentOnly=1'
        headers : dict = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36", 
        }
        response: requests.Response = requests.get(url, headers=headers, proxies=self.proxies)
        response.raise_for_status()
        data: dict = response.json()
        contests: list[ContestInfo] = []
        for contest in data['current']:
            contests.append(ContestInfo(
                oj_name='luogu',
                contest_id=contest['id'],
                contest_name=contest['name'],
                start_time=contest['startTime'],
                end_time=contest['endTime'],
                description=contest['description']
            ))
        return contests
    
    def getApproachingContestsInfo(self) -> str:
        return super().getApproachingContestsInfo()
