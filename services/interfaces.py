from abc import ABC, abstractmethod


class AiService(ABC):

    @abstractmethod
    async def generate_response(self, request_prompt: str) -> str:
        pass
