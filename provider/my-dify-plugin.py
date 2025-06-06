from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class MyDifyPluginProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            token = credentials.get("my_plugin_access_token")
            if token != "123456":
                raise ToolProviderCredentialValidationError("授权失败")

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
