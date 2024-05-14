import requests


class CodeforcesHelper:
    def __init__(self, url: str='127.0.0.1', port: int=7890):
        # set the url and port for the proxy
        self.proxies: dict = {
            'http': 'http://{url}:{port}'.format(url=url, port=port),
            'https': 'http://{url}:{port}'.format(url=url, port=port),
        }
    
    def get_submission(self, username: str) -> list:
        # get the submission of the user
        url: str = 'https://codeforces.com/api/user.status?handle={username}'.format(username=username)
        response: requests.Response = requests.get(url, proxies=self.proxies)
        response.raise_for_status()
        data = response.json()
        return data['result']
    
    def get_accepted_submissions(self, username: str) -> list:
        # get the accepted submissions of the user
        submissions: list = self.get_submission(username)
        return [s for s in submissions if s['verdict'] == 'OK']
