from dataclasses import dataclass
from services.interfaces import AiService, AiServiceParams


@dataclass
class YandexAiServiceParams(AiServiceParams):
    api_key: str
    folder_id: str
    system_prompt: str
    context_ad: str
    context_cases: str


class YandexAiService(AiService):

    def __init__(self, params: YandexAiServiceParams) -> None:
        self.api_key = params.api_key
        self.folder_id = params.folder_id
        self.system_prompt = params.system_prompt
        self.context_ad = params.context_ad
        self.context_cases = params.context_cases

    async def generate_response(self, request_prompt: str) -> str:
        return "Not implemented"
