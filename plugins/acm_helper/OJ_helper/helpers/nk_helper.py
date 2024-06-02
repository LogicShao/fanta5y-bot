from .OJ_helper import OJHelper
from ..infoClass import UserInfo

from pyquery import PyQuery as pq
from datetime import datetime, timedelta
import requests


class NowCoderHelper(OJHelper):

    def get_data(self, uid: str) -> str:
        # get the general data of the user
        url: str = 'https://ac.nowcoder.com/acm/contest/profile/{uid}/practice-coding'.format(
            uid=uid)
        # 喜报, 不需要加 header(
        response: requests.Response = requests.get(url, proxies=self.proxies)
        response.raise_for_status()
        return response.text

    def gatgatInfo(self, uid: str) -> dict:
        doc = pq(self.get_data(uid)) # pq是pyquery的一个函数，用于解析html文档
        data = {}  # 写完才发现data其实是字典...本来是按列表写的
        # data 格式 [username, rating, rating_rank, solvedProblems], 均为字符串
        data['username'] = doc(
            '.coder-info-detail .coder-name').text()  # 用户名, 查找不到返回空字符串
        if data['username'] == '':
            return {'username': None}
        data['rating'] = doc(
            '.nk-container .status-item .state-num').text()  # Rating
        data['rating_rank'] = [i for i in doc(
            '.nk-container .status-item').items()][1].text()[:-9]  # Rating 排名
        data['solvedProblems'] = [i for i in doc(
            '.nk-main .my-state-main .my-state-item .state-num').items()][1].text()  # 解出的题目数
        return data

    def getUserInfo(self, uid: str) -> UserInfo:
        # check the uid
        if not uid.isdigit():
            return '暂时只支持 uid 查询。do! 御坂如是说。'
        # get the user info
        info = self.gatgatInfo(uid)
        # check if the user exists
        username = info['username']
        if username is None:
            return UserInfo(username=None, onlineJudge='NowCoder')

        return UserInfo(
            username=info['username'],
            onlineJudge='NowCoder',
            rating=int(info['rating']),
            rating_rank=int(info['rating_rank']),
            solvedProblems=int(info['solvedProblems']),
        )

    def gechapoints(self, days: int) -> list:
        doc1=pq(requests.get('https://ac.nowcoder.com/acm/contest/vip-index').text)
        doc2=pq(requests.get('https://ac.nowcoder.com/acm/contest/vip-index?topCategoryFilter=14').text)
        contests=[i.text() for i in [i for i in doc1('.platform-mod.js-current .platform-item-main .btn.btn-primary.btn-xxs').siblings().items()][:len([i for i in doc1('.platform-mod.js-current .platform-item-main .btn.btn-primary.btn-xxs').items()])]] + [i.text() for i in [i for i in doc2('.platform-mod.js-current .platform-item-main .btn.btn-primary.btn-xxs').siblings().items()][:len([i for i in doc2('.platform-mod.js-current .platform-item-main .btn.btn-primary.btn-xxs').items()])]]
        times=[i.text() for i in [i for i in doc1('.platform-mod.js-current .match-time-icon').items()]]+[i.text() for i in [i for i in doc2('.platform-mod.js-current .match-time-icon').items()]]
        data=[]
        for i in range(len(times)):
            start_time = datetime.strptime(times[i].split('： ')[1].split(' 至 ')[0], '%Y-%m-%d %H:%M')
            if 0 <= (start_time - datetime.now()).days <= days:
                formatted_start_time = start_time.strftime('开始时间: %m 月 %d 日 %H:%M')
                data.append([contests[i],formatted_start_time])
        return data

    def getApproachingContestsInfo(self, days: int) -> UserInfo:
        data=self.gechapoints(days)
        if len(data) == 0:
            return '暂无即将开始的比赛。do! 御坂如是说。'
        # cf 和 luogu 实现比赛的代码有一点区别, 这里我又自己瞎写了一种(
        msg: str = 'nk {days} 天内即将开始的比赛有 {cnt} 场：\n'.format(days=days, cnt=len(data))
        for contest in data:
            msg += contest[0]+'\n'+'开始时间'+contest[1]+'\n'
        msg-='\n'
        return msg
