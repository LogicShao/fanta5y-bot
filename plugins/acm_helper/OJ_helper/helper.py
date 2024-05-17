from .codeforces_helper import CodeforcesHelper
from .luogu_helper import LuoguHelper
from .userinfo import UserInfo


class AcmHelper:
    def __init__(self, url: str='127.0.0.1', port: int=7890):
        # set codeforces helper
        self.codeforcesHelper = CodeforcesHelper(url, port)
        # set luogu helper
        self.luoguHelper = LuoguHelper(url, port)
        # set the helper dictionary
        # using the online judge to get the helper
        self.helperDict = {
            'codeforces': self.codeforcesHelper,
            'luogu' : self.luoguHelper
        }

    def getUserInfo(self, username: str, onlineJudge: str) -> UserInfo:
        OJhelper = self.helperDict[onlineJudge]
        return OJhelper.getUserInfo(username)
    
    def getApproachingContestsInfo(self, onlineJudge: str) -> str:
        OJhelper = self.helperDict[onlineJudge]
        return OJhelper.getApproachingContestsInfo()
