from typing import Optional

import time


class ContestInfo:
    def __init__(
        self,
        oj_name: str,
        contest_name: str,
        start_time: int,  # Unix timestamp
        end_time: int,  # Unix timestamp
        description: Optional[str] = None
    ):
        self.oj_name = oj_name
        self.contest_name = contest_name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def __str__(self):
        month, day, hour, minute = time.strftime(
            '%m %d %H %M', time.localtime(self.start_time)).split()
        duration: str = time.strftime(
            '%H:%M', time.gmtime(self.end_time - self.start_time))

        result: str = '{oj_name}:{contest_name}\n'\
            '开始时间: {month}月{day}日{hour}:{minute}\n'\
            '持续时间: {duration}\n'\
            .format(
                oj_name=self.oj_name,
                contest_name=self.contest_name,
                month=month,
                day=day,
                hour=hour,
                minute=minute,
                duration=duration,
            )
        return result

    def __repr__(self):
        return self.__str__()

    # 小于号 按照起始时间比较
    def __lt__(self, other):
        return self.start_time < other.start_time

    # 等于号 按照起始时间比较
    def __eq__(self, other):
        return self.start_time == other.start_time

    # 大于号 按照起始时间比较
    def __gt__(self, other):
        return self.start_time > other.start_time
