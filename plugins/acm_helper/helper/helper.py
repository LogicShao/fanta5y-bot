from .codeforces_helper import CodeforcesHelper


class ACMHelper:
    def __init__(self, url: str='127.0.0.1', port: int=7890):
        # set codeforces helper
        self.codeforces_helper = CodeforcesHelper(url, port)
        # set luogu helper
        self.luogu_helper = LuoguHelper()

        self.helper_dict = {
            'codeforces': self.codeforces_helper
            'luogu' : self.luogu_helper
        }
    
    def get_online_judge_accepted_submissions(self, username: str, online_judge: str) -> list:
        # get the accepted submissions of the user from the online judge
        # return self.helper_dict[online_judge].get_accepted_submissions(username)
        return self.helper_dict[online_judge].get_solved_problems(username)

