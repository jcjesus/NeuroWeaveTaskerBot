from playwright.sync_api import sync_playwright
import logging
from config.settings import SITE_URL, USERNAME, PASSWORD, SELECTORS

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def realizar_login(self):
        try:
            self.page.goto(SITE_URL)
            self.page.fill(SELECTORS['username'], USERNAME)
            self.page.fill(SELECTORS['password'], PASSWORD)
            self.page.click(SELECTORS['login_button'])
            self.page.wait_for_load_state('networkidle')
            logging.info('Login realizado com sucesso')
        except Exception as e:
            logging.error(f'Erro ao realizar login: {str(e)}')
            raise

    def navegar_e_clicar(self, url_destino):
        try:
            self.page.goto(url_destino)
            self.page.wait_for_load_state('networkidle')
            self.page.click(SELECTORS['target_button'])
            logging.info('Ação realizada com sucesso')
        except Exception as e:
            logging.error(f'Erro ao navegar e clicar: {str(e)}')
            raise 