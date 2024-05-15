from .userinfo import UserInfo


class OJHelper:
    def __init__(self, url: str='127.0.0.1', port: int=7890):
        # set the url and port for the proxy
        self.proxies: dict = {
            'http': 'http://{url}:{port}'.format(url=url, port=port),
            'https': 'http://{url}:{port}'.format(url=url, port=port),
        }

    def getData(self, uid: str) -> dict:
        pass

    def getSolvedProblems(self, uid: str) -> list:
        pass

    def getRatingList(self) -> list:
        pass

    def getApproachingContests(self) -> list:
        pass

    def getUserInfo(self, username: str) -> UserInfo:
        pass
