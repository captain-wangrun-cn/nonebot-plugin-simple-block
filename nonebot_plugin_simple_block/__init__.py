from nonebot import get_plugin_config, get_driver
from nonebot.message import run_preprocessor
from nonebot.exception import IgnoredException
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="简易群聊屏蔽",
    description="屏蔽某个群聊或只相应某个群聊，方便开发者进行插件测试",
    usage="",
    type="application",
    homepage="https://github.com/captain-wangrun-cn/nonebot-plugin-simple-block",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

plugin_config = get_plugin_config(Config)
group_blacklist,group_whitelist = plugin_config.group_blacklist,plugin_config.group_whitelist

@run_preprocessor
async def preprocessor(event: GroupMessageEvent):
    gid = str(event.group_id)

    if group_blacklist:
        # 存在黑名单，优先使用黑名单
        if gid in group_blacklist:
            raise IgnoredException("群聊屏蔽")
    else:
        # 使用白名单
        if gid not in group_whitelist:
            raise IgnoredException("群聊屏蔽")
