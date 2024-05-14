import requests

class LuoguHelper:
    def __init__(self):
        # 因为国内网站所以直连
        pass

    def get_passed_problem_count(self, uid: str) -> int:
        # get the submission of the user
        url: str = 'https://www.luogu.com.cn/user/{uid}?_contentOnly=1'.format(uid=uid)
        headers : dict = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36", 
        }
        response: requests.Response = requests.get(url , headers = headers)
        response.raise_for_status()
        data = response.json()
        return data['currentData']['user']['passedProblemCount']
