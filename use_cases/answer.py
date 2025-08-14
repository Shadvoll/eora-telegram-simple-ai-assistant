from services.interfaces import AiService


class AnswerUseCase:

    def __init__(
        self,
        ai_service: AiService,
    ) -> None:
        self.ai_service = ai_service

    async def execute(self, user_message: str, user_id: str) -> str:
        return self.ai_service.generate_response(user_message, user_id=user_id)

