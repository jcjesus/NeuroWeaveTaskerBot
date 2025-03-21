import signal
import sys
from core.scheduler import AutomationScheduler

def signal_handler(signum, frame):
    print('\nFinalizando o programa...')
    scheduler.parar()
    sys.exit(0)

if __name__ == "__main__":
    # Registra o handler para CTRL+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Inicia o agendador
    scheduler = AutomationScheduler()
    scheduler.iniciar()
    
    print("Programa iniciado. Pressione CTRL+C para finalizar.")
    
    # Mantém o programa rodando
    try:
        signal.pause()
    except AttributeError:
        # signal.pause() não está disponível no Windows
        while True:
            pass 