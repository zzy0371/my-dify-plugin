from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class MyDifyPluginTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        try:
            access_token = self.runtime.credentials["my_plugin_access_token"]
            if access_token != "123456":
                raise Exception("My Plugin Access Token 未配置或无效。请在插件设置中提供。")
        except KeyError:
            raise Exception("My Plugin Access Token 未配置或无效。请在插件设置中提供。")


        for k, v in tool_parameters.items():
            print(f"获取到查询信息 {k},  {v}")


        yield self.create_json_message({
            "result": "Hello, world!"
        })
