from ..infoClass.userinfo import UserInfo
from .OJ_helper import OJHelper

import requests
import time


class CodeforcesHelper(OJHelper):
    # codeforces API doc is here: https://codeforces.com/apiHelp
    def getSubmission(self, username: str) -> list:
        # get the submission of the user
        url: str = 'https://codeforces.com/api/user.status?handle={username}'.format(username=username)
        response: requests.Response = requests.get(url, proxies=self.proxies)
        response.raise_for_status()
        data = response.json()
        return data['result']
    
    def getAcceptedSubmissions(self, username: str) -> list:
        # get the accepted submissions of the user
        submissions: list = self.getSubmission(username)
        return [s for s in submissions if s['verdict'] == 'OK']

    def getSolvedProblems(self, username: str) -> list:
        # get the solved problems of the user
        ac_submissions: list = self.getAcceptedSubmissions(username)
        ac_problems = set(s['problem']['name'] for s in ac_submissions)
        return list(ac_problems)

    def getRatingList(self, username: str) -> list[int]:
        # get the rating list of the user
        url: str = 'https://codeforces.com/api/user.rating?handle={username}'.format(username=username)
        response: requests.Response = requests.get(url, proxies=self.proxies)
        response.raise_for_status()
        data = response.json()
        return [r['newRating'] for r in data['result']]
    
    def getContests(self) -> list:
        # get all contests
        url: str = 'https://codeforces.com/api/contest.list'
        response: requests.Response = requests.get(url, proxies=self.proxies)
        response.raise_for_status()
        data = response.json()
        return data['result']

    def getApprochingContestsList(self, days: int=10) -> list:
        # get the approaching contests in the next N days
        contests: list = self.getContests()
        approachingContests: list = []
        now: int = int(time.time())
        for contest in contests:
            if contest['phase'] == 'BEFORE' and contest['startTimeSeconds'] - now <= days * 24 * 3600:
                approachingContests.append(contest)
        return approachingContests

    def getApproachingContestsInfo(self, days: int=10) -> str:
        # get the approaching contests
        approachingContests: list = self.getApprochingContestsList(days=days)
        # sort the contests by start time
        approachingContests.sort(key=lambda x: x['startTimeSeconds'])
        result: str = 'codeforces {days} 日内有 {cnt} 场比赛:\n\n'.format(days=days, cnt=len(approachingContests))
        cnt: int = 0
        for contest in approachingContests:
            month, day, hour, minute = time.strftime('%m %d %H %M', time.localtime(contest['startTimeSeconds'])).split()
            result += '比赛 {cnt}: {name}\n'.format(cnt=(cnt:=cnt+1), name=contest['name'])
            result += '开始时间: {month} 月 {day} 日 {hour}:{minute}\n'.format(month=month, day=day, hour=hour, minute=minute)
            result += '\n'
        return result

    def getUserInfo(self, username: str) -> UserInfo:
        # get the user information
        solvedProblems: int = len(self.getSolvedProblems(username))
        ratingList: list[int] = self.getRatingList(username)
        rating: int = ratingList[-1]
        maxRating: int = max(ratingList)
        return UserInfo(
            username=username,
            onlineJudge='codeforces',
            solvedProblems=solvedProblems,
            rating=rating,
            maxRating=maxRating
        )
