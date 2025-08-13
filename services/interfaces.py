from abc import ABC, abstractmethod
from dataclasses import dataclass



class AiServiceParams(ABC):
    ...


class AiService(ABC):

    def __init__(
        self,
        params: AiServiceParams,
    ) -> None:
        ...

    @abstractmethod
    async def generate_response(self, request_prompt: str) -> str:
        pass
