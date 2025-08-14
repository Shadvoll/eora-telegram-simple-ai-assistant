from services.interfaces import AiService


class AnswerUseCase:

    def __init__(
        self,
        ai_service: AiService,
    ) -> None:
        self.ai_service = ai_service

    async def execute(self, user_message: str) -> str:
        return await self.ai_service.generate_response(user_message)

