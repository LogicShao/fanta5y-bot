from .OJ_helper import OJHelper
from .OJ_helper import UserInfo
from .OJ_helper import ContestInfo

import requests
import time


class LuoguHelper(OJHelper):

    # 返回所有的用户信息 json
    def getUserData(self, uid: str) -> dict:
        url: str = 'https://www.luogu.com.cn/user/{uid}?_contentOnly=1'.format(
            uid=uid)
        headers: dict = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36",
        }
        response: requests.Response = requests.get(
            url, headers=headers, proxies=self.proxies)
        response.raise_for_status()
        return response.json()['currentData']['user']

    # 返回用户信息 UserInfo
    def getUserInfo(self, uid: str) -> UserInfo:
        # check the uid
        if not uid.isdigit():
            return UserInfo(error='暂时只支持 uid 查询。do! 御坂如是说。')
        data: dict = self.getUserData(uid)
        if 'code' in data and data['code'] == 404:
            return UserInfo(error='用户不存在。do! 御坂如是说。')
        # get user name
        user_name: str = data['name']
        # get solved problems
        solved_problems: int = data['passedProblemCount']
        user: UserInfo = UserInfo(
            username=user_name,
            onlineJudge='luogu',
            solvedProblems=solved_problems
        )
        return user

    # 获取即将开始的比赛信息
    def getApproachingContestsList(self) -> list[ContestInfo]:
        url: str = 'https://www.luogu.com.cn/contest/list?_contentOnly=1'
        headers: dict = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36",
        }
        response: requests.Response = requests.get(
            url, headers=headers, proxies=self.proxies)
        response.raise_for_status()
        data: dict = response.json()['currentData']
        contests: list[ContestInfo] = []
        for contest in data['contests']['result']:
            contest_name: str = contest['name']
            contest_start_time: int = contest['startTime']
            contest_end_time: int = contest['endTime']

            if contest_start_time < time.time():
                continue

            contests.append(ContestInfo(
                oj_name='洛谷',
                contest_name=contest_name,
                start_time=contest_start_time,
                end_time=contest_end_time
            ))
        return contests

    # 获取 days 天内即将开始的比赛信息
    def getApproachingContestsInfo(self, days=10) -> str:
        contests: list[ContestInfo] = sorted(list(
            filter(lambda contest: contest.start_time < time.time() + days * 24 * 60 * 60,
                   self.getApproachingContestsList())
        ))

        if len(contests) == 0:
            return '暂无即将开始的比赛。do! 御坂如是说。'

        msg: str = '{days} 天内即将开始的比赛信息：\n'.format(days=days)
        msg += ''.join(map(str, contests))

        # 移除最后一个换行符
        return msg.removesuffix('\n')
