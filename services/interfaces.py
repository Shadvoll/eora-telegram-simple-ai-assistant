from abc import ABC, abstractmethod


class AiService(ABC):

    @abstractmethod
    def generate_response(self, request_prompt: str, user_id: str) -> str:
        pass
