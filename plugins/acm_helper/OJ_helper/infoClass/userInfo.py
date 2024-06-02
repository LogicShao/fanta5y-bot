from typing import Optional


class UserInfo:
    def __init__(
        self,
        username: Optional[str] = None,
        onlineJudge: Optional[str] = None,
        solvedProblems: Optional[int] = 0,
        rating: Optional[int] = None,
        rating_rank: Optional[int] = None,
        maxRating: Optional[int] = None,
        error: Optional[str] = None
    ):
        self.username = username
        self.onlineJudge = onlineJudge
        self.solvedProblems = solvedProblems
        self.rating = rating
        self.rating_rank = rating_rank
        self.maxRating = maxRating
        self.error = error

    def __str__(self):
        if self.username is None:
            if self.error is not None:
                return self.error
            return '御坂没找到这个用户呢，你确定输入的是正确的用户名吗？'

        userInfo = f'do! 亲爱的 {self.onlineJudge} 用户 {self.username}：'
        userInfo += f'你已经解决了 {self.solvedProblems} 道题目'
        if self.rating is not None:
            userInfo += f'，你现在的 rating 是 {self.rating} 分'
        if self.rating_rank is not None:
            userInfo += f'，你现在的 rating排名 是 {self.rating_rank} 名'
        if self.maxRating is not None:
            userInfo += f'，你的历史最高 rating 是 {self.maxRating} 分'
        userInfo += '。'

        return userInfo
