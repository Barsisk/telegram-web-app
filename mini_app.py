import streamlit as st
import urllib.parse
import datetime

# Настройка страницы
st.set_page_config(
    page_title="Telegram Mini App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Получаем параметры из URL
query_params = st.query_params
user_id = query_params.get("user_id", "")
first_name = query_params.get("first_name", "")

# Заголовок
st.title("🤖 Telegram Mini App")
st.markdown("---")

# Проверка, открыто ли через Telegram
if not user_id:
    st.error("⚠️ Это приложение работает только через Telegram!")
    st.info("""
    ### Как открыть:
    1. Найдите бота в Telegram
    2. Отправьте команду `/start`
    3. Нажмите кнопку "Открыть мини-приложение"
    
    ### Для тестирования:
    Вы можете заполнить форму ниже, но данные не сохранятся в Telegram.
    """)
    
    # Режим демо (без user_id)
    demo_mode = True
    user_id = "demo_user"
    first_name = "Гость"
else:
    demo_mode = False
    st.success(f"✅ Привет, {first_name}!")

# Показываем информацию о пользователе
with st.sidebar:
    st.header("👤 Информация")
    st.write(f"**ID:** `{user_id}`")
    st.write(f"**Имя:** {first_name}")
    st.write(f"**Режим:** {'🚫 Демо' if demo_mode else '✅ Реальный'}")
    
    if not demo_mode:
        st.info("""
        ### 📝 Инструкция:
        1. Заполните форму
        2. Нажмите "Сохранить данные"
        3. Скопируйте сгенерированный текст
        4. Вернитесь в Telegram
        5. Отправьте текст боту
        6. Используйте `/getdata` для просмотра
        """)

# Основная форма
st.header("📝 Форма для заполнения")

with st.form("user_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Ваше имя*", value=first_name if first_name else "")
        age = st.number_input("Ваш возраст", min_value=1, max_value=120, value=25)
    
    with col2:
        email = st.text_input("Email", placeholder="example@mail.com")
        city = st.text_input("Город", placeholder="Москва")
    
    interests = st.multiselect(
        "Ваши интересы",
        ["Программирование", "Дизайн", "Маркетинг", "Аналитика", "Управление"],
        default=["Программирование"]
    )
    
    message = st.text_area("Дополнительная информация", height=100)
    
    submitted = st.form_submit_button("💾 Сохранить данные", type="primary")

# Обработка отправки формы
if submitted:
    if name:
        # Создаем словарь с данными
        from datetime import datetime
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        
        user_data = {
            "Имя": name,
            "Возраст": str(age),
            "Email": email if email else "Не указан",
            "Город": city if city else "Не указан",
            "Интересы": ", ".join(interests) if interests else "Не указаны",
            "Сообщение": message if message else "Нет",
            "Дата заполнения": timestamp
        }
        
        # Сохраняем в сессии
        st.session_state.user_data = user_data
        
        # Показываем успешное сообщение
        st.success("✅ Данные готовы к отправке!")
        
        # Показываем данные
        st.subheader("📋 Ваши данные:")
        for key, value in user_data.items():
            st.write(f"**{key}:** {value}")
        
        st.markdown("---")
        
        # Создаем текст для отправки в Telegram
        if not demo_mode:
            st.subheader("📤 Отправка в Telegram")
            
            # Способ 1: Форматированный текст для копирования
            st.markdown("### Способ 1: Скопируйте и отправьте")
            
            # Создаем текст в удобном формате
            telegram_text = f"""Данные из формы:
имя: {name}
возраст: {age}
email: {email if email else 'не указан'}
город: {city if city else 'не указан'}
интересы: {', '.join(interests) if interests else 'не указаны'}
сообщение: {message if message else 'нет'}
время: {timestamp}"""
            
            st.code(telegram_text)
            
            st.info("""
            ### Как отправить:
            1. Скопируйте текст выше (Ctrl+C / Cmd+C)
            2. Вернитесь в чат с ботом
            3. Вставьте текст и отправьте (Ctrl+V / Cmd+V)
            4. Используйте команду `/getdata` для просмотра
            """)
            
            # Способ 2: Ссылка для быстрой отправки
            st.markdown("### Способ 2: Быстрая отправка")
            
            # Кодируем текст для URL
            encoded_text = urllib.parse.quote(telegram_text)
            
            # Создаем ссылку на Telegram
            telegram_url = f"https://t.me/share/url?url=&text={encoded_text}"
            
            st.markdown(f"""
            <a href="{telegram_url}" target="_blank">
                <button style='
                    background-color: #0088cc;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    width: 100%;
                '>
                    📤 Открыть Telegram и отправить
                </button>
            </a>
            """, unsafe_allow_html=True)
            
            st.caption("Эта кнопка откроет Telegram с готовым сообщением")
            
        else:
            st.warning("""
            ⚠️ **Демо-режим**
            
            В демо-режиме данные не могут быть отправлены в Telegram.
            Откройте это приложение через Telegram бота для полной функциональности.
            """)
            
    else:
        st.error("❌ Пожалуйста, введите ваше имя!")

# Информация в футере
st.markdown("---")
st.caption("""
**ℹ️ Примечание:** Это мини-приложение для Telegram. 
Данные сохраняются только при отправке через Telegram бота.
""")

# Стили CSS
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
    }
    .stAlert {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)
