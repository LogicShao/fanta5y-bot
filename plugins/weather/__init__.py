from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

from random import choice

weather = on_command(
    "天气",
    rule=to_me(),
    aliases={"weather", "查天气"},
    priority=10,
    block=True
)

async def get_weather():
    # 随机给出一个天气
    weather_list = ["晴天", "多云", "阴天", "小雨", "中雨", "大雨", "暴雨", "雷阵雨", "雾", "雪", "冰雹"]
    # 随机给出一个温度 单位：摄氏度
    temperature = choice(range(-10, 40))
    # 随机给出一个湿度 单位：%
    humidity = choice(range(0, 100))
    # 随机给出一个风力 单位：m/s
    wind = choice(range(0, 20))

    weather_info: str = f"{choice(weather_list)}，温度{temperature}℃，湿度{humidity}%，风力{wind}m/s"
    return weather_info

@weather.handle()
async def handle_function():
    # await weather.send("天气是...")
    weather_now = await get_weather()
    info = "今天的天气是：" + weather_now + "！"
    await weather.finish(info)

__plugin_meta__ = PluginMetadata(
    name="weather",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

