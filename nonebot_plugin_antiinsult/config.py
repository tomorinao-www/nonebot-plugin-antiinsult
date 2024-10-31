from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    class ScopedConfig(BaseModel):
        # 高峰期限制回复策略mode:
        # 1. 不允许回复频率高于阈值，保持每分钟回复数量低于阈值
        # 2. 允许回复频率高于阈值，但回复概率降低为：固定值 prob
        # 3. 允许回复频率高于阈值，但回复概率降低为: 动态的 limit_send_msg / real_send_msg
        mode: int = 1
        # 阈值，每分钟服务多少次。
        limits: int = 10
        # 高峰期的回复概率。设置为 0 时 mode 2 等价于 mode 1
        prob: float = 0.2

    antiinsult: ScopedConfig


conf = get_plugin_config(Config).antiinsult
