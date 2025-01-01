<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <img src="https://github.com/WStudioGroup/hifumi-plugins/blob/main/remove.photos-removed-background.png" width="200">
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-simple-block

_✨ 屏蔽某个群聊或只相应某个群聊，方便开发者进行插件测试 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/captain-wangrun-cn/nonebot-plugin-simple-block.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-simple-block">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-simple-block.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

## 📖 介绍

屏蔽某个群聊或只相应某个群聊，方便开发者进行插件测试

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-simple-block

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-simple-block

</details>


打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_simple_block"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项          | 类型   | 必填 | 默认值 | 说明                  |
|:------------:|:----:|:---:|:---:|:-------------------:|
| group_blacklist | list | 否  | [ ]  | 黑名单，添加在黑名单内的群将不会响应 |
| group_whitelist | list | 否  | [ ]  | 白名单，只会响应白名单内的群    |

>[!IMPORTANT]
>当黑名单和白名单同时配置时，将会优先使用黑名单

## 📃 更新日志
### 1.0.1（2025.01.01）
- 📃修复了一些问题
### 1.0.0（2024.12.20）
- 🧋发布插件
