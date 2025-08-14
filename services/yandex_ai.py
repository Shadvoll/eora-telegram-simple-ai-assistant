from dataclasses import dataclass

import httpx

from repositories.ai_context import SystemPrompt
from services.interfaces import AiService, AiServiceParams


@dataclass
class YandexAiServiceParams(AiServiceParams):
    api_key: str
    folder_id: str
    system_prompt: SystemPrompt


class YandexAiService(AiService):

    YANDEX_GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    def __init__(self, params: YandexAiServiceParams) -> None:
        self.api_key = params.api_key
        self.folder_id = params.folder_id
        self.system_prompt = params.system_prompt.text_data

    async def generate_response(self, request_prompt: str) -> str:
        headers = {
            "Authorization": f"Api-Key {self.api_key}",
            "Content-Type": "application/json",
            "x-folder-id": self.folder_id,
        }
        payload = {
            "modelUri": f"gpt://{self.folder_id}/yandexgpt/latest",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": 2000,
            },
            "messages": [
                {"role": "system", "text": self.system_prompt},
                {"role": "user", "text": request_prompt},
            ],
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.YANDEX_GPT_URL, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            # Ответ содержит список choices, берем первый
            return data["result"]["alternatives"][0]["message"]["text"]
