import requests

class LuoguHelper:
    def __init__(self):
        # 因为国内网站所以直连
        pass

    def get_data(self, uid: str) -> dict:
        # get the general data of the user
        url: str = 'https://www.luogu.com.cn/user/{uid}?_contentOnly=1'.format(uid=uid)
        headers : dict = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36", 
        }
        response: requests.Response = requests.get(url , headers = headers)
        response.raise_for_status()
        return response.json()

    def get_solved_problems(self, uid: str) -> list:
        # extract the list of solved problems 
        return self.get_data(uid)['currentData']['passedProblems']
