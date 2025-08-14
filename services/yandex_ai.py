from dataclasses import dataclass
from typing import TYPE_CHECKING

from yandex_cloud_ml_sdk import YCloudML

from repositories.ai_context import SystemPrompt
from services.interfaces import AiService

if TYPE_CHECKING:
    from yandex_cloud_ml_sdk._threads.domain import Threads


@dataclass
class YandexAiServiceParams:
    api_key: str
    folder_id: str
    system_prompt: SystemPrompt


class YandexAiAssistantService(AiService):
    BASE_URL = "https://rest-assistant.api.cloud.yandex.net"

    def __init__(self, params: YandexAiServiceParams) -> None:
        self.sdk = YCloudML(
            folder_id=params.folder_id,
            auth=params.api_key,
        )
        model = self.sdk.models.completions("yandexgpt", model_version="rc")
        self.assistant = self.sdk.assistants.create(
            model,
            instruction=params.system_prompt.text_data,
            ttl_days=1,
            expiration_policy="since_last_active",
            max_tokens=500,
        )
        self._threads: dict[str, Threads] = {}

    def generate_response(self, user_message: str, user_id: str) -> str:
        if user_id not in self._threads:
            user_thread: Threads = self.sdk.threads.create(
                name="yandex-ai-assistant",
                ttl_days=1,
                expiration_policy="static",
            )
            self._threads[user_id] = user_thread
        else:
            user_thread: Threads = self._threads[user_id]

        user_thread.write(user_message)
        run = self.assistant.run(user_thread)
        return " ".join(run.wait().parts)


    def __del__(self) -> None:
        for user_id in self._threads:
            self._threads[user_id].delete()
        self.assistant.delete()
