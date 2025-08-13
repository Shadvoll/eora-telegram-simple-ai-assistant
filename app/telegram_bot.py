import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import settings
from use_cases.answer import AnswerUseCase
from services import YandexAiService, YandexAiServiceParams
from repositories.ai_context import ContextRepository

BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN


async def process_question(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    message_text = update.message.text
    answer_use_case: AnswerUseCase = context.application.answer_use_case
    response_text = await answer_use_case.execute(message_text)
    await update.message.reply_text(response_text)

if __name__ == "__main__":
    context_repo = ContextRepository()
    ai_service = YandexAiService(
        params=YandexAiServiceParams(
            api_key=settings.YANDEX_API_KEY,
            folder_id=settings.YANDEX_FOLDER_ID,
            system_prompt=context_repo.get_system_prompt(),
            context_ad=context_repo.get_ad_context(),
            context_cases=context_repo.get_case_context(),
        )
    )    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.answer_use_case = AnswerUseCase(
        ai_service=ai_service
    )

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_question))

    print("Bot started. Press Ctrl+C to stop.")
    app.run_polling()
