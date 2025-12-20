import asyncio
import logging
import json
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Конфигурация
BOT_TOKEN = "8082157697:AAFvNbZcqzI4HHuVhlsTUUpagpxo6V1wdb0"
ADMIN_ID = 913096630  # ID администратора
GITHUB_HTML_URL = "https://barsisk.github.io/telegram-web-app/"

# Инициализация
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Хранилище запросов
requests_log = []

@dp.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📱 Открыть Mini App",
                    web_app=WebAppInfo(url=GITHUB_HTML_URL)
                )
            ]
        ]
    )
    
    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Нажми кнопку ниже, чтобы открыть мини-приложение.\n"
        "В мини-приложении будет кнопка для отправки уведомления администратору."
    )
    
    await message.answer(welcome_text, reply_markup=keyboard)

@dp.message(Command("admin"))
async def cmd_admin(message: Message):
    """Команда для администратора"""
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ У вас нет доступа к этой команде.")
        return
    
    if not requests_log:
        await message.answer("📭 Лог пуст. Запросов еще не было.")
        return
    
    log_text = "📋 <b>Лог запросов:</b>\n\n"
    for i, req in enumerate(requests_log[-10:], 1):  # Последние 10 запросов
        log_text += f"{i}. От {req['user_name']} (ID: {req['user_id']})\n"
        log_text += f"   Время: {req['time']}\n"
        log_text += f"   Сообщение: {req['message']}\n\n"
    
    await message.answer(log_text)

@dp.message()
async def handle_web_app_data(message: Message):
    """Обработка данных из Web App"""
    if message.text and message.text.startswith("NOTIFY_ADMIN:"):
        try:
            # Извлекаем данные
            data_str = message.text.replace("NOTIFY_ADMIN:", "")
            data = json.loads(data_str)
            
            user_id = message.from_user.id
            user_name = message.from_user.full_name
            username = f"@{message.from_user.username}" if message.from_user.username else "без username"
            
            # Логируем запрос
            request_data = {
                "user_id": user_id,
                "user_name": user_name,
                "username": username,
                "time": datetime.now().strftime("%H:%M:%S %d.%m.%Y"),
                "message": data.get("message", "Нет сообщения")
            }
            requests_log.append(request_data)
            
            # Отправляем уведомление пользователю
            await message.answer(
                "✅ <b>Уведомление отправлено администратору!</b>\n\n"
                f"Ваше сообщение: <i>{data.get('message')}</i>\n"
                f"Время отправки: {request_data['time']}"
            )
            
            # Отправляем уведомление администратору
            admin_message = (
                "🚨 <b>НОВОЕ УВЕДОМЛЕНИЕ ИЗ MINI APP</b>\n\n"
                f"👤 <b>От пользователя:</b>\n"
                f"• Имя: {user_name}\n"
                f"• Username: {username}\n"
                f"• ID: {user_id}\n\n"
                f"💬 <b>Сообщение:</b>\n"
                f"<i>{data.get('message')}</i>\n\n"
                f"🕒 <b>Время:</b> {request_data['time']}\n\n"
                f"ID запроса: {len(requests_log)}"
            )
            
            await bot.send_message(
                chat_id=ADMIN_ID,
                text=admin_message,
                parse_mode=ParseMode.HTML
            )
            
            logger.info(f"Notification sent to admin from user {user_id}")
            
        except json.JSONDecodeError:
            await message.answer("❌ Ошибка: неверный формат данных.")
        except Exception as e:
            logger.error(f"Error processing notification: {e}")
            await message.answer("❌ Произошла ошибка при отправке уведомления.")

async def main():
    """Запуск бота"""
    logger.info("Starting notification bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
