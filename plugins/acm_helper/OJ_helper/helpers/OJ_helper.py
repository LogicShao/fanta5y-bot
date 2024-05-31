from typing import Optional
from abc import ABC, abstractmethod

from ..infoClass.userinfo import UserInfo

import requests


class OJHelper(ABC):
    # the abstract class for the online judge helper
    def __init__(self, url: Optional[str]='127.0.0.1', port: Optional[int]=7890):
        # set the url and port for the proxy
        if url is None or port is None:
            self.proxies: dict = None
        else:
            self.proxies: dict = {
                'http': 'http://{url}:{port}'.format(url=url, port=port),
                'https': 'http://{url}:{port}'.format(url=url, port=port),
            }
    
    def handleRequest(self, url: str) -> dict:
        # handle the request to the url
        try:
            response = requests.get(url, proxies=self.proxies, timeout=10)
        except requests.Timeout:
            raise requests.Timeout('Request to {url} timed out'.format(url=url))
        except requests.RequestException as e:
            raise requests.RequestException('Request to {url} failed: {e}'.format(url=url, e=e))
        
        response.raise_for_status()
        return response.json()
    
    @abstractmethod
    def getUserInfo(self, username: str) -> UserInfo:
        pass

    @abstractmethod
    def getApproachingContestsInfo(self) -> str:
        pass
