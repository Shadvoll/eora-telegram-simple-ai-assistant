

На задание было потрачено 2 вечера (~6-7 часов).
Задачу разделил на три основных этапа:

- Парсинг Данных
- Архитектура
- Подключение сервиса AI

### Парсинг Данных
Так как на детальный парсинг, извлчение и систматизирование данных не было. Честно использовал ChatGPT. И он справился средне, но справился. Как итог, это сэкономило очень много времени. Такой процесс для меня был немного в новинку. 
Минусы - не смог спарсить одним запросом все кейсы. Надо было парсить по 3-4 кейса. В рамках тестового, я не стал дальше парсить. Цель была оценить такой способ. 

### Архитектура

Разделил на repositories, services, use_cases.

Repositories - с целью хранения и получения AI промптов. Использовал простое хранение в .txt файлах. Однако, при дальнейшем усложнении можно использовать другие способы хранения. 
Изначально думал, чтобы отдельно хранить отдельно кейсы (их описание в промпте), отдельно рекламный рассказ о компании, отдельно описание роли. Однако, отказался от этой идеи, так как можно всё было поместить в один промпт. 

Services - Ответственен за взаимодействие с AI. 

UseCase - Использование Services. Возможно, в данной реализации избыточно.

### Подключение сервиса AI
~~Использовал YandexCloud FoundationsModels.~~
~~Есть опыт использования, но не в таком формате.~~
Переписал с использованием YCloudML для более простого использования Threads для хранения контекста.

### Осталось сделать:
- ~~Добавить запоминание чата (хотя бы 10-15 сообщений). Threads на основании telegram_id~~
- Улучшить промпты. Посмотреть результаты. 
- Отдельное локальное хранения для Threads. Думаю, что при большом наплыве пользователей может увеличиться RAM usage. 
- Пересмотреть архитектуру. Возможно, она избыточна
- Покрыть тестами. pytest

### Различные Идеи. 
Задача мне понравилась! Я чуть детальнее прикоснулся к промпт-инженерингу. 
Улучшить промпт для более точных ответов.

Хранить *слепок* AI ассистентов в виде промптов в некой хранилке (например, Postgres). Использоваль фабрики для создания AI-Assistant c различными **характерами** для быстрого запуска. 




# Telegram Bot with AI Integration

This project implements a Telegram bot that integrates with AI services (Yandex) to provide intelligent responses to user messages.

## Features

- Telegram bot integration
- AI-powered responses using Yandex AI
- Asynchronous message handling
- Environment-based configuration

## Prerequisites

- Python 3.12+
- Telegram Bot Token
- Yandex API credentials (API Key and Folder ID)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd eora_test_task
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
YANDEX_API_KEY=your_yandex_api_key
YANDEX_FOLDER_ID=your_yandex_folder_id
```

## Project Structure

- `app/` - Contains the main Telegram bot implementation
- `services/` - AI service integrations and interfaces
- `repositories/` - AI context and prompt management
- `use_cases/` - Business logic implementation
- `config.py` - Application configuration

## Running the Bot

### Using Python directly

To start the bot:

```bash
python -m app.telegram_bot
```

### Using Docker Compose (Recommended)

1. Make sure you have Docker and Docker Compose installed
2. Create a `.env` file with your configuration (see above)
3. Run the bot:

```bash
docker compose up --build
```

To run in detached mode:

```bash
docker compose up -d --build
```

To stop the bot:

```bash
docker compose down
```

## Development

For development, you can install additional development dependencies:

```bash
pip install -r requirements-dev.txt
```


-------


