from .helpers import OJHelper
from .helpers import CodeforcesHelper
from .helpers import LuoguHelper
from .helpers import NowCoderHelper

from .infoClass import UserInfo
from .infoClass import ContestInfo

from typing import Optional
from functools import reduce


class AcmHelper:
    def __init__(
        self,
        url: Optional[str] = '127.0.0.1',
        port: Optional[int] = 7890
    ):
        # set codeforces helper
        self.codeforcesHelper = CodeforcesHelper(url, port)
        # set luogu helper
        self.luoguHelper = LuoguHelper(url, port)
        # set nk helper
        self.nowCoderHelper = NowCoderHelper(url, port)
        # set the helper dictionary
        # using the online judge to get the helper
        self.helperDict: dict[str, OJHelper] = {
            'codeforces': self.codeforcesHelper,
            'luogu': self.luoguHelper,
            'nowcoder': self.nowCoderHelper,
        }

    def getUserInfo(self, username: str, onlineJudge: str) -> UserInfo:
        OJhelper: OJHelper = self.helperDict[onlineJudge]
        return OJhelper.getUserInfo(username)

    def getApproachingContestsInfo(self, onlineJudge: str) -> str:
        OJhelper: OJHelper = self.helperDict[onlineJudge]
        return OJhelper.getApproachingContestsInfo()

    def mergeTwoSortedList(self, info1: list[ContestInfo], info2: list[ContestInfo]) -> list[ContestInfo]:
        # merge two sorted list
        res: list[ContestInfo] = []
        point1: int = 0
        point2: int = 0

        while point1 < len(info1) and point2 < len(info2):
            if info1[point1] < info2[point2]:
                res.append(info1[point1])
                point1 += 1
            else:
                res.append(info2[point2])
                point2 += 1

        while point1 < len(info1):
            res.append(info1[point1])
            point1 += 1

        while point2 < len(info2):
            res.append(info2[point2])
            point2 += 1

        return res

    def getApproachingContests(self) -> list[ContestInfo]:
        contests: list[ContestInfo] = reduce(
            self.mergeTwoSortedList,
            (list(filter(lambda contest: contest.error is None,
                         helper.getApproachingContestsList())
                  )
                for helper in self.helperDict.values())
        )
        return contests
