from typing import Optional
from abc import ABC, abstractmethod

from .userinfo import UserInfo


class OJHelper(ABC):
    # the abstract class for the online judge helper
    def __init__(self, url: Optional[str]='127.0.0.1', port: Optional[int]=7890):
        # set the url and port for the proxy
        if url is None:
            self.proxies: dict = None
        else:
            self.proxies: dict = {
                'http': 'http://{url}:{port}'.format(url=url, port=port),
                'https': 'http://{url}:{port}'.format(url=url, port=port),
            }
    
    @abstractmethod
    def getUserInfo(self, username: str) -> UserInfo:
        pass

    @abstractmethod
    def getApproachingContestsInfo(self) -> str:
        pass
