from typing import Optional


class ProblemInfo:
    def __init__(
        self,
        problemID: Optional[str],
        onlineJudge: str,
        title: Optional[str] = None,
        difficulty: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ):
        self.problemID = problemID
        self.onlineJudge = onlineJudge
        self.title = title
        self.difficulty = difficulty
        self.tags = tags

    def __str__(self):
        if self.problemID is None:
            return '御坂没找到这个题目呢，你确定输入的是正确的题目ID吗？'

        problemInfo = f'do! 来自 {self.onlineJudge} 的题目 {self.problemID}：'
        problemInfo += f'题目名称是 {self.title}'
        if self.difficulty is not None:
            problemInfo += f'，难度是 {self.difficulty}'
        if self.tags is not None:
            problemInfo += f'，标签是 {self.tags}'
        problemInfo += '。'

        return problemInfo
