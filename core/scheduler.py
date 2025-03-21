from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
from datetime import datetime
from config.settings import EXECUTION_INTERVAL, SITE_URL
from .browser_manager import BrowserManager

class AutomationScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def executar_automacao(self):
        logging.info(f'Iniciando automação em {datetime.now()}')
        try:
            with BrowserManager() as browser:
                browser.realizar_login()
                browser.navegar_e_clicar(f"{SITE_URL}/destino")
            logging.info('Automação concluída com sucesso')
        except Exception as e:
            logging.error(f'Erro durante a execução da automação: {str(e)}')

    def iniciar(self):
        """Inicia o agendador com intervalo configurado"""
        self.scheduler.add_job(
            self.executar_automacao,
            trigger=IntervalTrigger(hours=EXECUTION_INTERVAL),
            next_run_time=datetime.now()  # Executa imediatamente na primeira vez
        )
        self.scheduler.start()
        logging.info(f'Agendador iniciado. Executando a cada {EXECUTION_INTERVAL} horas')

    def parar(self):
        """Para o agendador"""
        self.scheduler.shutdown()
        logging.info('Agendador finalizado') 