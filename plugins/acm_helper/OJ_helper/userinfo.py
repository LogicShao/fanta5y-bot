from typing import Optional

class UserInfo:
    def __init__(
        self,
        username: str,
        onlineJudge: str,
        solvedProblems: int,
        rating: Optional[int] = None,
        maxRating: Optional[int] = None
    ):
        self.username = username
        self.onlineJudge = onlineJudge
        self.solvedProblems = solvedProblems
        self.rating = rating
        self.maxRating = maxRating
    
    def __str__(self):
        userInfo = f'听好了！{self.onlineJudge} 用户 {self.username}：'
        userInfo += f'你已经解决了 {self.solvedProblems} 道题目'
        if self.rating is not None:
            userInfo += f'，你现在的 rating 是 {self.rating} 分'
        if self.maxRating is not None:
            userInfo += f'，你的历史最高 rating 是 {self.maxRating} 分'
        userInfo += '。'
        return userInfo
