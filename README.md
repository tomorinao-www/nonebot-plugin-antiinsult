<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-antiinsult

_✨ NoneBot 反嘴臭插件 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/tkgs0/nonebot-plugin-antiinsult.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-antiinsult">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-antiinsult.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
</a>
<a href="https://nonebot.dev">
    <img src="https://img.shields.io/badge/nonebot-2.3.1+-red.svg" alt="nonebot">
</a>
<a href="https://onebot.adapters.nonebot.dev">
    <img src="https://img.shields.io/badge/OneBot-11-black?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAMAAADxPgR5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAxQTFRF////29vbr6+vAAAAk1hCcwAAAAR0Uk5T////AEAqqfQAAAKcSURBVHja7NrbctswDATQXfD//zlpO7FlmwAWIOnOtNaTM5JwDMa8E+PNFz7g3waJ24fviyDPgfhz8fHP39cBcBL9KoJbQUxjA2iYqHL3FAnvzhL4GtVNUcoSZe6eSHizBcK5LL7dBr2AUZlev1ARRHCljzRALIEog6H3U6bCIyqIZdAT0eBuJYaGiJaHSjmkYIZd+qSGWAQnIaz2OArVnX6vrItQvbhZJtVGB5qX9wKqCMkb9W7aexfCO/rwQRBzsDIsYx4AOz0nhAtWu7bqkEQBO0Pr+Ftjt5fFCUEbm0Sbgdu8WSgJ5NgH2iu46R/o1UcBXJsFusWF/QUaz3RwJMEgngfaGGdSxJkE/Yg4lOBryBiMwvAhZrVMUUvwqU7F05b5WLaUIN4M4hRocQQRnEedgsn7TZB3UCpRrIJwQfqvGwsg18EnI2uSVNC8t+0QmMXogvbPg/xk+Mnw/6kW/rraUlvqgmFreAA09xW5t0AFlHrQZ3CsgvZm0FbHNKyBmheBKIF2cCA8A600aHPmFtRB1XvMsJAiza7LpPog0UJwccKdzw8rdf8MyN2ePYF896LC5hTzdZqxb6VNXInaupARLDNBWgI8spq4T0Qb5H4vWfPmHo8OyB1ito+AysNNz0oglj1U955sjUN9d41LnrX2D/u7eRwxyOaOpfyevCWbTgDEoilsOnu7zsKhjRCsnD/QzhdkYLBLXjiK4f3UWmcx2M7PO21CKVTH84638NTplt6JIQH0ZwCNuiWAfvuLhdrcOYPVO9eW3A67l7hZtgaY9GZo9AFc6cryjoeFBIWeU+npnk/nLE0OxCHL1eQsc1IciehjpJv5mqCsjeopaH6r15/MrxNnVhu7tmcslay2gO2Z1QfcfX0JMACG41/u0RrI9QAAAABJRU5ErkJggg==" alt="onebot">
</a>

</div>

## TODO list

- [ ] 概率不回复，防止高峰期被 tx 针对

## 📖 介绍

**本插件为被动插件**

检测到有用户 `@机器人` 并嘴臭时将其临时屏蔽(bot 重启后失效)  
当 bot 为群管理时会请对方喝昏睡红茶(禁言)

- 超级用户不受临时屏蔽影响 _~~但是会被昏睡红茶影响~~_
- 当 bot 的群权限比超级用户高的时候, 超级用户也有机会品尝昏睡红茶
- 被 bot 灌了昏睡红茶的用户不会进临时黑名单
- 开启 **`对线模式`** 后不会被 bot 灌昏睡红茶和临时拉黑 (~~因为要对线~~)

## 💿 安装

**nb-cli 安装, 包管理器安装 二选一**

<details>
<summary>使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-antiinsult

</details>

<details>
<summary>使用包管理器安装</summary>

在 nonebot2 项目的插件目录下, 打开命令行,

**根据你使用的包管理器, 输入相应的安装命令**

<details>
<summary>pip</summary>

    pip install nonebot-plugin-antiinsult

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-antiinsult

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-antiinsult

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-antiinsult

</details>

打开 bot 项目下的 `pyproject.toml` 文件,

在其 `plugins` 里加入 `nonebot_plugin_antiinsult`

    plugins = ["nonebot_plugin_antiinsult"]

</details>
</details>

## 🎉 使用

在 Bot 目录下的 `.env` 文件内可添加以下变量以设置禁言时长:

```env
ANTI_INSULT_BAN_TIME=720
```

单位为分钟, 默认值 720 分钟(12 小时)

### 指令表

<table> 
  <tr align="center">
    <th> 指令 </th>
    <th> 权限 </th>
    <th> 需要@ </th>
    <th> 范围 </th>
    <th> 说明 </th>
  </tr>
  <tr align="center">
    <td> ^(添加|删除)屏蔽词 xxx </td>
    <td> 主人 </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
    <td rowspan="2"> 可输入多个,<br>用空格隔开 </td>
  </tr>
  <tr align="center">
    <td> 解除屏蔽 qq </td>
    <td> 主人 </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
  </tr>
  <tr align="center">
    <td> 查看临时黑名单 </td>
    <td> 主人 </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
    <td> </td>
  </tr>
  <tr align="center">
    <td> ^(禁用|启用)飞(妈|马|🐴|🐎)令 </td>
    <td> 主人 </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
    <td> 开启/关闭对线模式 </td>
</table>

P.S. `解除屏蔽` 可以解除临时屏蔽, 也可以解除禁言(当然, 需要 bot 为群管理).

你说从聊天界面查看屏蔽词库? 噢, 我亲爱的老伙计, 你怕是疯了!

## 配置

| 配置项            | 类型  | 必填吗 | 默认值 | 说明                                               |
| ----------------- | ----- | ------ | ------ | -------------------------------------------------- |
| antiinsult_mode   | int   | 否     | 1      | 限流策略，详见下                                   |
| antiinsult_limits | int   | 否     | 10     | 每分钟最多服务 10 次                               |
| antiinsult_prob   | float | 否     | 0.2    | 高峰期的回复概率。设置为 0 时 mode 2 等价于 mode 1 |

```python
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

```

## ⚠️ 注意事项

**本插件目前仅支持 nonebot2 + onebot.v11 的使用方式, 一切非此二者结合的使用方式造成的问题请自行探索解决, 或者使用其他插件**
