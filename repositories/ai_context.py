from abc import abstractmethod
from dataclasses import dataclass
import aiofiles

@dataclass
class ContextItem:
    text_data: str


class ContextAd(ContextItem):
    ...

class ContextCase(ContextItem):
    ...

class SystemPrompt(ContextItem):
    ...

class ContextRepository:

    _ad_path = r"repositories/ai_context_ad.txt"
    _case_path = r"repositories/ai_context_cases.txt"
    _system_prompt_path = r"repositories/ai_context_system_prompt.txt"

    @staticmethod
    def get_ad_context() -> ContextAd:
        with open(ContextRepository._ad_path, encoding='utf-8') as file:
            return ContextAd(text_data=file.read())

    @staticmethod
    def get_case_context() -> ContextCase:
        with open(ContextRepository._case_path, encoding='utf-8') as file:
            return ContextCase(text_data=file.read())
        
    @staticmethod
    def get_system_prompt() -> SystemPrompt:
        with open(ContextRepository._system_prompt_path, encoding='utf-8') as file:
            return SystemPrompt(text_data=file.read())
