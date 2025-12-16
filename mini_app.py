import streamlit as st
import time
import urllib.parse

st.set_page_config(page_title="Mini App", layout="centered")

# Заголовок
st.title("📱 Простое Mini App")
st.write("Эта страница открывается из Telegram")

# Простая форма
name = st.text_input("Как тебя зовут?")
email = st.text_input("Твой email")

if st.button("💾 Сохранить данные"):
    if name:
        # Просто показываем данные
        st.success("Данные получены!")
        
        # Создаем сообщение для отправки
        current_time = time.strftime("%H:%M:%S")
        message = f"""
        📋 Новые данные от пользователя:
        
        👤 Имя: {name}
        📧 Email: {email or 'Не указан'}
        ⏰ Время: {current_time}
        
        Чтобы получить эти данные в Telegram, используй команду /getdata
        """
        
        # Показываем данные
        st.info(message)
        
        # Создаем ссылку для отправки данных через Telegram (простой способ)
        telegram_text = urllib.parse.quote(message)
        telegram_url = f"https://t.me/share/url?url=&text={telegram_text}"
        
        st.markdown(f'[📤 Поделиться в Telegram]({telegram_url})', unsafe_allow_html=True)
    else:
        st.warning("Введи хотя бы имя!")

# Инструкция
st.divider()
st.write("""
**Как это работает:**
1. Открой это приложение из Telegram бота
2. Заполни форму
3. Нажми кнопку "Сохранить данные"
4. Используй команду /getdata в боте
""")

# Альтернатива: QR код для быстрого доступа (опционально)
st.divider()
st.write("📲 **Быстрый доступ к боту:**")
st.code("/start", language="bash")
