import streamlit as st
import requests
import time

st.set_page_config(page_title="Mini App", layout="centered")

st.title("📱 Mini App для Telegram")
st.write("Заполни форму и отправь данные в Telegram")

# Получаем user_id из параметров URL
query_params = st.query_params
user_id = query_params.get("user_id", "")

if not user_id:
    st.warning("⚠️ Открой это приложение через Telegram бота!")
    st.info("Используйте команду /start в боте")
    st.stop()

st.success(f"✅ Привет, пользователь #{user_id}!")

# Простая форма
with st.form("user_form"):
    name = st.text_input("Ваше имя", placeholder="Иван")
    age = st.number_input("Ваш возраст", min_value=1, max_value=100, value=25)
    city = st.text_input("Ваш город", placeholder="Москва")
    
    submitted = st.form_submit_button("💾 Сохранить в Telegram")

if submitted:
    if name:
        # Подготавливаем данные
        user_data = {
            "Имя": name,
            "Возраст": age,
            "Город": city,
            "Время сохранения": time.strftime("%H:%M:%S %d.%m.%Y")
        }
        
        # Сохраняем локально (в сессии Streamlit)
        st.session_state.user_data = user_data
        
        # Показываем данные
        st.success("✅ Данные готовы к отправке!")
        
        # Показываем что мы сохранили
        st.subheader("📋 Ваши данные:")
        for key, value in user_data.items():
            st.write(f"**{key}:** {value}")
        
        # Инструкция как получить данные
        st.divider()
        st.info("""
        **Как получить данные в Telegram:**
        
        1. Вернитесь в чат с ботом
        2. Отправьте команду **/getdata**
        3. Бот покажет ваши сохраненные данные
        
        Или нажмите кнопку ниже для автоматической отправки:
        """)
        
        # Кнопка для имитации отправки (в реальности нужно API)
        if st.button("📤 Отправить данные сейчас"):
            st.info("""
            ⚠️ Для реальной отправки нужен API сервер!
            
            В реальном приложении здесь был бы POST запрос к вашему серверу,
            который сохранил бы данные в базу и связал с user_id={user_id}
            
            Пока что просто используйте команду /getdata в боте
            """)
            
    else:
        st.warning("⚠️ Введите хотя бы имя!")

# Показываем текущий user_id
st.sidebar.info(f"👤 User ID: `{user_id}`")
