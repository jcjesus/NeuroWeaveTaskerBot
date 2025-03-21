import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Site
SITE_URL = os.getenv('SITE_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
TARGET_PAGE_SELECTOR = os.getenv('TARGET_PAGE_SELECTOR')

# Seletores da Página
SELECTORS = {
    'username': os.getenv('LOGIN_USERNAME_SELECTOR'),
    'username_next_button': os.getenv('LOGIN_USERNAME_BT_NEXT'),
    'password': os.getenv('LOGIN_PASSWORD_SELECTOR'),
    'password_button': os.getenv('LOGIN_PASSWORD_BT_SELECTOR'),
    'target_task_button': os.getenv('TARGET_TASK_BUTTON_SELECTOR'),
    'target_page': os.getenv('TARGET_PAGE_SELECTOR')
}

# Configurações do Agendador
EXECUTION_INTERVAL = int(os.getenv('EXECUTION_INTERVAL_HOURS', 6))

# Configurações de Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'logs/automacao.log') 