from .userinfo import UserInfo
from .OJ_helper import OJHelper

import requests


class CodeforcesHelper(OJHelper):
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
    
    def getContests(self) -> list:
        # get all contests
        url: str = 'https://codeforces.com/api/contest.list'
        response: requests.Response = requests.get(url, proxies=self.proxies)
        response.raise_for_status()
        data = response.json()
        return data['result']

    def getApprochingContests(self, timedelta: int=10) -> list:
        # get the approaching contests in the next timedelta days
        contests: list = self.getContests()
        return [c for c in contests if c['phase'] == 'BEFORE' and c['durationSeconds'] < timedelta * 86400]

    def getUserInfo(self, username: str) -> UserInfo:
        # get the user information
        solvedProblems: int = len(self.getSolvedProblems(username))
        rating: int = 1300
        maxRating: int = 1300
        return UserInfo(
            username=username,
            onlineJudge='codeforces',
            solvedProblems=solvedProblems,
            rating=rating,
            maxRating=maxRating
        )
