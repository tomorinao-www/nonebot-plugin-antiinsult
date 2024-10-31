import time
from random import random

from nonebot.matcher import Matcher
from nonebot.exception import IgnoredException
from nonebot.message import run_preprocessor

from .config import conf


class Data:
    time_ls = []  # 记录每次服务时间戳, len 就是服务频率


data = Data()


async def update():
    """通用服务更新函数"""
    data.time_ls = filter(lambda t: t + 60 < time.time(), data.time_ls)
    data.time_ls.append(time.time())


async def ban1():
    """mode1 处理函数
    不允许回复频率高于阈值，保持每分钟回复数量低于阈值"""
    # 如果 len 大于阈值，那么需要 ban, 返回 True
    return len(data.time_ls) >= conf.limits


async def ban2():
    """mode2 处理函数
    允许回复频率高于阈值，但回复概率降低为：固定值 prob"""
    if len(data.time_ls) >= conf.limits:
        # 随机数如果 大于 设定的 回复概率，那么返回True, 需要ban
        return random() > conf.prob
    else:
        return True


async def ban3():
    """mode3 处理函数
    允许回复频率高于阈值，但回复概率降低为:
            动态的 limit_send_msg / real_send_msg"""
    length = len(data.time_ls)
    if length >= conf.limits:
        # 随机数如果 大于 当前回复概率，那么返回True, 需要ban
        return random() > (conf.limits / length)
    else:
        return True


func_list = (ban1, ban2, ban3)


@run_preprocessor
async def limit_server():
    # 1. 根据mode拿到func
    ban = func_list[conf.mode]
    # 2. 判断是否需要阻断，随后抛出异常
    if await ban():
        raise IgnoredException(f"人家1分钟已经接待了{1}位宝宝啦，等妈妈忙完哦！")
    else:
        # 3.正常服务的话，更新服务时间列表
        await update()
