from .OJ_helper import UserInfo
from .OJ_helper import ContestInfo
from .OJ_helper import OJHelper

import time


class CodeforcesHelper(OJHelper):
    # codeforces API doc is here: https://codeforces.com/apiHelp
    def getSubmission(self, username: str) -> list:
        # get the submission of the user
        url: str = 'https://codeforces.com/api/user.status?handle={username}'.format(
            username=username)
        data: dict = self.handleRequest(url)
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
        url: str = 'https://codeforces.com/api/user.rating?handle={username}'.format(
            username=username)
        data: dict = self.handleRequest(url)
        return [r['newRating'] for r in data['result']]

    def getContests(self) -> list:
        # get all contests
        url: str = 'https://codeforces.com/api/contest.list'
        data: dict = self.handleRequest(url)
        return data['result']

    def getApproachingContestsList(self, days: int = 10) -> list[ContestInfo]:
        # get the approaching contests
        contests: list = self.getContests()
        approachingContests: list = []
        now: int = int(time.time())
        for contest in contests:
            if contest['phase'] == 'BEFORE' and contest['startTimeSeconds'] - now <= days * 24 * 3600:
                approachingContests.append(ContestInfo(
                    oj_name='codeforces',
                    contest_name=contest['name'],
                    start_time=contest['startTimeSeconds'],
                    end_time=contest['durationSeconds'] + contest['startTimeSeconds']
                ))
        return sorted(approachingContests)

    def getApproachingContestsInfo(self, days: int = 10) -> str:
        # get the approaching contests
        approachingContests: list[ContestInfo] = self.getApproachingContestsList(days=days)
        
        msg = "CF{days}日内有{cnt}场比赛:\n\n".format(days=days, cnt=len(approachingContests))
        for i, contest in enumerate(approachingContests):
            month, day, hour, minute = time.strftime(
                '%m %d %H %M', time.localtime(contest.start_time)).split()
            duration: str = time.strftime(
                '%H:%M', time.gmtime(contest.end_time - contest.start_time))
            
            msg += '比赛 {i}:{contest_name}\n'\
                '开始时间: {month}月{day}日{hour}:{minute}\n'\
                '持续时间: {duration}\n'\
                .format(
                    i=i+1,
                    contest_name=contest.contest_name,
                    month=month,
                    day=day,
                    hour=hour,
                    minute=minute,
                    duration=duration,
                )

            if i != len(approachingContests) - 1:
                msg += '\n'
        
        return msg.removesuffix('\n')

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
