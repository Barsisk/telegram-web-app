<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telegram Mini App - Авторизация</title>
    <meta name="description" content="Мини-приложение для авторизации в Telegram боте">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #0088cc;
            --primary-dark: #0077b3;
            --secondary: #6c757d;
            --success: #28a745;
            --danger: #dc3545;
            --light: #f8f9fa;
            --dark: #343a40;
            --border-radius: 12px;
            --shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: var(--dark);
        }
        
        .container {
            width: 100%;
            max-width: 450px;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .app-card {
            background: white;
            border-radius: var(--border-radius);
            padding: 40px 30px;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }
        
        .app-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--primary-dark));
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .logo {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 50%;
            margin-bottom: 15px;
            color: white;
            font-size: 30px;
            box-shadow: 0 6px 15px rgba(0, 136, 204, 0.3);
        }
        
        .header h1 {
            color: var(--dark);
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
        }
        
        .header p {
            color: var(--secondary);
            font-size: 15px;
        }
        
        .tabs {
            display: flex;
            background: var(--light);
            border-radius: 10px;
            padding: 5px;
            margin-bottom: 25px;
        }
        
        .tab {
            flex: 1;
            text-align: center;
            padding: 12px;
            cursor: pointer;
            color: var(--secondary);
            font-weight: 600;
            font-size: 15px;
            border-radius: 8px;
            transition: var(--transition);
        }
        
        .tab:hover {
            color: var(--primary);
        }
        
        .tab.active {
            background: white;
            color: var(--primary);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        .form {
            display: none;
        }
        
        .form.active {
            display: block;
            animation: slideIn 0.4s ease;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(10px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-label {
            display: block;
            margin-bottom: 8px;
            color: var(--dark);
            font-weight: 500;
            font-size: 14px;
        }
        
        .form-input {
            width: 100%;
            padding: 14px 16px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 15px;
            transition: var(--transition);
            background: white;
        }
        
        .form-input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(0, 136, 204, 0.1);
        }
        
        .form-input::placeholder {
            color: #adb5bd;
        }
        
        .btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0, 136, 204, 0.3);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .telegram-data {
            background: #f0f8ff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            border-left: 4px solid var(--primary);
        }
        
        .telegram-data h3 {
            font-size: 15px;
            color: var(--primary);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .telegram-data p {
            font-size: 14px;
            color: var(--dark);
            margin-bottom: 5px;
        }
        
        .alert {
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: none;
            animation: fadeIn 0.3s ease;
        }
        
        .alert.show {
            display: block;
        }
        
        .alert.success {
            background: #d4edda;
            color: #155724;
            border-left: 4px solid #28a745;
        }
        
        .alert.error {
            background: #f8d7da;
            color: #721c24;
            border-left: 4px solid #dc3545;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .loading.show {
            display: block;
        }
        
        .spinner {
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            border-top: 4px solid var(--primary);
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .footer {
            text-align: center;
            margin-top: 25px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
            color: var(--secondary);
            font-size: 13px;
        }
        
        @media (max-width: 480px) {
            .app-card {
                padding: 30px 20px;
            }
            
            .header h1 {
                font-size: 22px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="app-card">
            <div class="header">
                <div class="logo">
                    <i class="fas fa-lock"></i>
                </div>
                <h1>Авторизация</h1>
                <p>Войдите или создайте аккаунт</p>
            </div>
            
            <div id="telegram-data" class="telegram-data" style="display: none;">
                <h3><i class="fab fa-telegram"></i> Данные Telegram</h3>
                <p id="tg-name"></p>
                <p id="tg-username"></p>
                <p id="tg-id"></p>
            </div>
            
            <div class="tabs">
                <div class="tab active" onclick="showForm('login')">Вход</div>
                <div class="tab" onclick="showForm('register')">Регистрация</div>
            </div>
            
            <div id="login-form" class="form active">
                <div class="form-group">
                    <label class="form-label" for="login-email">Email</label>
                    <input type="email" id="login-email" class="form-input" placeholder="ваш@email.com" required>
                </div>
                <div class="form-group">
                    <label class="form-label" for="login-password">Пароль</label>
                    <input type="password" id="login-password" class="form-input" placeholder="Ваш пароль" required>
                </div>
                <button class="btn" onclick="login()">
                    <i class="fas fa-sign-in-alt"></i> Войти
                </button>
            </div>
            
            <div id="register-form" class="form">
                <div class="form-group">
                    <label class="form-label" for="register-name">Имя</label>
                    <input type="text" id="register-name" class="form-input" placeholder="Ваше имя" required>
                </div>
                <div class="form-group">
                    <label class="form-label" for="register-email">Email</label>
                    <input type="email" id="register-email" class="form-input" placeholder="ваш@email.com" required>
                </div>
                <div class="form-group">
                    <label class="form-label" for="register-password">Пароль</label>
                    <input type="password" id="register-password" class="form-input" placeholder="Придумайте пароль" required>
                </div>
                <div class="form-group">
                    <label class="form-label" for="register-confirm">Подтвердите пароль</label>
                    <input type="password" id="register-confirm" class="form-input" placeholder="Повторите пароль" required>
                </div>
                <button class="btn" onclick="register()">
                    <i class="fas fa-user-plus"></i> Зарегистрироваться
                </button>
            </div>
            
            <div class="alert" id="alert"></div>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Отправка данных в Telegram...</p>
            </div>
            
            <div class="footer">
                <p><i class="fas fa-info-circle"></i> Данные будут отправлены в чат с ботом</p>
            </div>
        </div>
    </div>

    <script>
        // Проверяем, запущено ли приложение в Telegram
        let isTelegram = false;
        let telegramUser = null;
        
        // Функция для проверки Telegram WebApp
        function initTelegramWebApp() {
            if (window.Telegram && window.Telegram.WebApp) {
                isTelegram = true;
                const tg = window.Telegram.WebApp;
                
                // Инициализируем WebApp
                tg.ready();
                tg.expand();
                tg.enableClosingConfirmation();
                
                // Получаем данные пользователя
                telegramUser = tg.initDataUnsafe?.user;
                
                // Показываем данные Telegram, если они есть
                if (telegramUser) {
                    const telegramDataDiv = document.getElementById('telegram-data');
                    document.getElementById('tg-name').textContent = `Имя: ${telegramUser.first_name || ''} ${telegramUser.last_name || ''}`.trim();
                    document.getElementById('tg-username').textContent = `Username: @${telegramUser.username || 'не указан'}`;
                    document.getElementById('tg-id').textContent = `ID: ${telegramUser.id}`;
                    telegramDataDiv.style.display = 'block';
                    
                    // Автозаполнение полей
                    const emailField = document.getElementById('register-email');
                    const nameField = document.getElementById('register-name');
                    const loginEmailField = document.getElementById('login-email');
                    
                    if (emailField && telegramUser.username) {
                        emailField.value = `${telegramUser.username}@telegram.com`;
                    }
                    
                    if (nameField && telegramUser.first_name) {
                        nameField.value = telegramUser.first_name;
                    }
                    
                    if (loginEmailField && telegramUser.username) {
                        loginEmailField.value = `${telegramUser.username}@telegram.com`;
                    }
                }
                
                console.log('Telegram WebApp инициализирован', telegramUser);
                return tg;
            } else {
                console.log('Не в Telegram WebApp. Режим тестирования.');
                showAlert('Режим тестирования. В Telegram данные будут отправляться автоматически.', 'info');
                return null;
            }
        }
        
        // Инициализация при загрузке страницы
        document.addEventListener('DOMContentLoaded', function() {
            initTelegramWebApp();
        });
        
        function showForm(formName) {
            // Переключение табов
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            document.querySelectorAll('.form').forEach(form => {
                form.classList.remove('active');
            });
            
            // Активируем выбранный таб
            if (formName === 'login') {
                document.querySelector('.tab:nth-child(1)').classList.add('active');
                document.getElementById('login-form').classList.add('active');
            } else {
                document.querySelector('.tab:nth-child(2)').classList.add('active');
                document.getElementById('register-form').classList.add('active');
            }
            
            // Скрываем предыдущие сообщения
            hideAlert();
        }
        
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }
        
        function showAlert(message, type = 'error') {
            const alertDiv = document.getElementById('alert');
            alertDiv.textContent = message;
            alertDiv.className = `alert ${type} show`;
            
            // Автоматически скрывать через 5 секунд
            setTimeout(hideAlert, 5000);
        }
        
        function hideAlert() {
            const alertDiv = document.getElementById('alert');
            alertDiv.classList.remove('show');
        }
        
        function showLoading(show) {
            document.getElementById('loading').classList.toggle('show', show);
        }
        
        async function login() {
            const email = document.getElementById('login-email').value.trim();
            const password = document.getElementById('login-password').value;
            
            if (!validateEmail(email)) {
                showAlert('Введите корректный email', 'error');
                return;
            }
            
            if (!password) {
                showAlert('Введите пароль', 'error');
                return;
            }
            
            showLoading(true);
            
            // Создаем объект с данными
            const userData = {
                action: 'login',
                email: email,
                timestamp: new Date().toLocaleString('ru-RU'),
                date_iso: new Date().toISOString(),
                source: 'github_pages_mini_app'
            };
            
            // Добавляем данные Telegram, если они есть
            if (telegramUser) {
                userData.tg_user_id = telegramUser.id;
                userData.tg_username = telegramUser.username;
                userData.tg_first_name = telegramUser.first_name;
                userData.tg_last_name = telegramUser.last_name;
                userData.tg_language_code = telegramUser.language_code;
            }
            
            try {
                // Отправляем данные в Telegram бот
                if (isTelegram && window.Telegram.WebApp) {
                    const tg = window.Telegram.WebApp;
                    tg.sendData(JSON.stringify(userData));
                    
                    showAlert('✅ Успешный вход! Данные отправлены в Telegram.', 'success');
                    
                    // Через 2 секунды закрываем приложение
                    setTimeout(() => {
                        tg.close();
                    }, 2000);
                } else {
                    // Режим тестирования (не в Telegram)
                    showAlert('✅ Данные для входа сформированы. В Telegram они отправятся автоматически.', 'success');
                    console.log('Данные для отправки:', userData);
                    
                    // Сбрасываем форму
                    document.getElementById('login-password').value = '';
                }
                
            } catch (error) {
                showAlert('❌ Ошибка при отправке данных: ' + error.message, 'error');
                console.error(error);
            } finally {
                showLoading(false);
            }
        }
        
        async function register() {
            const name = document.getElementById('register-name').value.trim();
            const email = document.getElementById('register-email').value.trim();
            const password = document.getElementById('register-password').value;
            const confirm = document.getElementById('register-confirm').value;
            
            if (!name) {
                showAlert('Введите ваше имя', 'error');
                return;
            }
            
            if (!validateEmail(email)) {
                showAlert('Введите корректный email', 'error');
                return;
            }
            
            if (!password) {
                showAlert('Введите пароль', 'error');
                return;
            }
            
            if (password !== confirm) {
                showAlert('Пароли не совпадают', 'error');
                return;
            }
            
            if (password.length < 6) {
                showAlert('Пароль должен быть не менее 6 символов', 'error');
                return;
            }
            
            showLoading(true);
            
            // Создаем объект с данными
            const userData = {
                action: 'register',
                name: name,
                email: email,
                timestamp: new Date().toLocaleString('ru-RU'),
                date_iso: new Date().toISOString(),
                source: 'github_pages_mini_app'
            };
            
            // Добавляем данные Telegram, если они есть
            if (telegramUser) {
                userData.tg_user_id = telegramUser.id;
                userData.tg_username = telegramUser.username;
                userData.tg_first_name = telegramUser.first_name;
                userData.tg_last_name = telegramUser.last_name;
                userData.tg_language_code = telegramUser.language_code;
            }
            
            try {
                // Отправляем данные в Telegram бот
                if (isTelegram && window.Telegram.WebApp) {
                    const tg = window.Telegram.WebApp;
                    tg.sendData(JSON.stringify(userData));
                    
                    showAlert('✅ Регистрация успешна! Данные отправлены в Telegram.', 'success');
                    
                    // Через 2 секунды закрываем приложение
                    setTimeout(() => {
                        tg.close();
                    }, 2000);
                } else {
                    // Режим тестирования (не в Telegram)
                    showAlert('✅ Регистрация завершена. В Telegram данные отправятся автоматически.', 'success');
                    console.log('Данные для отправки:', userData);
                    
                    // Сбрасываем форму
                    document.getElementById('register-password').value = '';
                    document.getElementById('register-confirm').value = '';
                }
                
            } catch (error) {
                showAlert('❌ Ошибка при отправке данных: ' + error.message, 'error');
                console.error(error);
            } finally {
                showLoading(false);
            }
        }
        
        // Добавляем отправку по нажатию Enter
        document.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                const activeForm = document.querySelector('.form.active');
                if (activeForm.id === 'login-form') {
                    login();
                } else if (activeForm.id === 'register-form') {
                    register();
                }
            }
        });
    </script>
</body>
</html>
