from .OJ_helper import OJHelper
from .OJ_helper import UserInfo
from .OJ_helper import ContestInfo

import pytz
from requests import get
from pyquery import PyQuery as pq
from datetime import datetime,timedelta


class NowCoderHelper(OJHelper):

    def get_data(self, username: str) -> str:
        # Atcoder 使用 Username 来获取信息
        # get the general data of the user
        url: str = 'https://atcoder.jp/users/{username}'.format(
            username=username)
        # 国外网站, 这里暂且加上 proxy
        response = get(url, proxies=self.proxies)
        response.raise_for_status()
        return response.text

    def gatgatInfo(self, username: str) -> list:
        # 作为 get_data 的 ⭐😡 ,输入 Username , 输出列表, 格式 [Rank, Rating], 均为字符串
        doc = pq(self.get_data(username))
        return [[i.text()[5:-2] for i in doc('.dl-table.mt-2').children().siblings().items()][0]]+[[i.text()[7:] for i in doc('.dl-table.mt-2').children().siblings().items()][1]]

    def getUserInfo(self, username: str) -> UserInfo:
        # 输出模块
        if username.isdigit():
            return UserInfo(error='暂时只支持 uid 查询。do! 御坂如是说。')
        # get the user info
        #由于涉及到列表和字符串的切片, 如果用户不存在会报 IndexError: list index out of range
        try:
            info = self.gatgatInfo(username)
        except IndexError:
            return UserInfo(error='用户不存在。do! 御坂如是说。')
        return UserInfo(
            username=username,
            onlineJudge='AtCoder',
            rating=int(info[1]),
            rating_rank=int(info[0]),
        )

    # 时间部分的代码由 AI 完成, 现在看到 time 有点反胃
    # Function to convert duration to timedelta
    def duration_to_timedelta(self, duration_str):
        hours, minutes = map(int, duration_str.split(':'))
        return timedelta(hours=hours, minutes=minutes)

    def getApproachingContestsList(self) -> list[ContestInfo]:
        return [ContestInfo(error='暂时没有实现 NowCoder 的比赛查询功能。do! 御坂抱歉说。')]

    def gechapoints(self, days: int) -> list[ContestInfo]:
        doc = pq(get(
            'https://atcoder.jp/contests/').text)
        # contests 为列表, 格式 [比赛一, 比赛二....]
        contests = [j for i, j in enumerate([i.text() for i in doc('#contest-table-upcoming').find('a').items()]) if (i+1)%2==0]
        # times 同为列表, 格式 [比赛一开始时间, 比赛一持续时间, 比赛二开始时间...]
        '''示例:
        ['2024-06-08 21:00:00+0900', '01:40', '2024-06-15 21:00:00+0900', '01:40', '2024-06-16 15:00:00+0900', '04:00', '2024-06-29 21:00:00+0900', '02:00', '2024-06-30 21:00:00+0900', '01:40', '2024-07-06 21:00:00+0900', '01:40']
        '''
        times = [j for i, j in enumerate([i.text() for i in doc('#contest-table-upcoming .text-center').items()][4:]) if (i+1)%3!=0]
        data: list[ContestInfo] = [];current_time = datetime.now(pytz.utc)
        for i in range(0, len(times), 2):
            start_time = datetime.strptime(times[i], '%Y-%m-%d %H:%M:%S%z')
            duration = self.duration_to_timedelta(times[i+1])
            end_time = start_time + duration
    
            if current_time <= start_time <= current_time + timedelta(days=days):
                data.append(ContestInfo(
                oj_name='AtCoder',
                contest_name=contests[i], # type: ignore
                start_time=int(start_time.timestamp()),
                end_time=int(end_time.timestamp())
            ))
        return data

    def getApproachingContestsInfo(self, days: int = 10) -> str:
        data = self.gechapoints(days)
        if len(data) == 0:
            return '暂时没有即将开始的比赛。do! 御坂如是说。'

        msg = 'AtCoder {days} 天内即将的比赛有 {cnt} 场：\n'.format(
            days=days, cnt=len(data))
        
        msg += '\n'.join(map(str, data))
        
        # 移除最后一个换行符
        if len(data) > 0 and msg[-1] == '\n':
            msg = msg[:-1]
        return msg
