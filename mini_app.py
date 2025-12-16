import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем токен бота
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

st.set_page_config(
    page_title="Telegram Mini App",
    page_icon="🤖",
    layout="centered"
)

# Функция для получения данных из Telegram WebApp
def get_init_data():
    """Получаем данные из Telegram WebApp"""
    # В реальном приложении данные приходят через query parameters
    # Для демонстрации используем фиктивные данные
    return {
        'user_id': 123456789,
        'first_name': 'Иван',
        'last_name': 'Иванов',
        'username': 'ivanov',
        'language_code': 'ru'
    }

# Получаем данные пользователя
init_data = get_init_data()

# Отображаем данные пользователя
st.title("🤖 Telegram Mini App")
st.divider()

st.subheader("Информация о пользователе:")
st.write(f"**ID:** {init_data.get('user_id', 'Не указан')}")
st.write(f"**Имя:** {init_data.get('first_name', 'Не указано')}")
st.write(f"**Фамилия:** {init_data.get('last_name', 'Не указана')}")
st.write(f"**Username:** @{init_data.get('username', 'Не указан')}")
st.write(f"**Язык:** {init_data.get('language_code', 'Не указан')}")

st.divider()

# Кнопка для отправки данных в Telegram
if st.button("📤 Отправить данные в Telegram", type="primary", use_container_width=True):
    try:
        # В реальном приложении вам нужно получить chat_id из данных WebApp
        # Здесь используем фиктивный chat_id для демонстрации
        chat_id = init_data.get('user_id')
        
        # Подготовка данных для отправки
        user_data = {
            "User ID": init_data.get('user_id'),
            "First Name": init_data.get('first_name'),
            "Last Name": init_data.get('last_name'),
            "Username": f"@{init_data.get('username')}",
            "Language": init_data.get('language_code'),
            "Platform": "Telegram WebApp"
        }
        
        # Отправляем данные на сервер бота
        # В реальном приложении лучше использовать веб-хук или API
        st.success("✅ Данные отправлены в Telegram!")
        st.json(user_data)
        
        # Для реальной интеграции с ботом:
        # 1. Сохраните данные в базе данных
        # 2. Отправьте через API бота или веб-хук
        # 3. Используйте метод send_message бота
        
    except Exception as e:
        st.error(f"Ошибка при отправке данных: {str(e)}")

# Дополнительная информация
st.divider()
st.info("""
    **Как это работает:**
    1. Пользователь открывает мини-приложение из Telegram
    2. Приложение получает данные пользователя из Telegram WebApp
    3. При нажатии кнопки данные отправляются обратно в чат
""")