from dataclasses import dataclass


@dataclass
class ContextItem:
    text_data: str



class SystemPrompt(ContextItem):
    ...

class ContextRepository:


    _system_prompt_path = r"repositories/ai_context_system_prompt.txt"

    @staticmethod
    def get_system_prompt() -> SystemPrompt:
        with open(ContextRepository._system_prompt_path, encoding="utf-8") as file:
            return SystemPrompt(text_data=file.read())
