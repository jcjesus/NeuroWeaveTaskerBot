# 🤖 NeuroWeaveTaskerBot

## 🌟 Sobre o Projeto
Bot de automação web inteligente desenvolvido para executar tarefas programadas de forma autônoma e confiável, com agendamento personalizado de horários.

### 🎯 Principais Funcionalidades
- 🔄 Execução em horários personalizados
- 🔐 Login automático seguro
- 🎯 Navegação inteligente
- ⚡ Ações programadas
- 📊 Logging detalhado

## 🚀 Guia de Instalação e Configuração

### 📋 Pré-requisitos do Sistema
- 🐍 Python 3.8+ ([Download Python](https://www.python.org/downloads/))
- 📦 pip (gerenciador de pacotes Python)
- 🌐 Git ([Download Git](https://git-scm.com/downloads))
- 🔧 Visual Studio Code ou PyCharm (recomendado)
- 🌐 Conexão com internet

### ⚙️ Configuração do Ambiente

1. **Clone o Repositório**
```bash
# Via HTTPS
git clone https://github.com/jcjesus/NeuroWeaveTaskerBot.git

# Via SSH
git clone git@github.com:jcjesus/NeuroWeaveTaskerBot.git

cd NeuroWeaveTaskerBot
```

2. **Configure o Ambiente Virtual**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as Dependências**
```bash
# Atualizar pip
python -m pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt

# Instalar navegadores para o Playwright
playwright install
```

4. **Configure as Variáveis de Ambiente**
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar arquivo com suas configurações
# Windows
notepad .env

# Linux/Mac
nano .env
```

### 🔧 Configuração da Aplicação

1. **Configuração dos Horários**
```bash
# Criar arquivo de configuração de horários
cp config/schedule.example.json config/schedule.json

# Editar horários conforme necessidade
# Exemplo de schedule.json:
{
    "schedule": [
        {"hour": "08", "minute": "00"},
        {"hour": "12", "minute": "30"},
        {"hour": "15", "minute": "45"},
        {"hour": "19", "minute": "15"}
    ]
}
```

2. **Configuração dos Seletores**
Edite o arquivo `.env` com os seletores corretos:
```env
LOGIN_USERNAME_SELECTOR=#username
LOGIN_USERNAME_BT_NEXT=#next
LOGIN_PASSWORD_SELECTOR=#password
LOGIN_PASSWORD_BT_SELECTOR=#login
TARGET_TASK_BUTTON_SELECTOR=#task
TARGET_PAGE_SELECTOR=#page
```

## 🚀 Executando a Aplicação

### 🎮 Modo de Desenvolvimento
```bash
# Ativar ambiente virtual (se ainda não estiver ativo)
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Executar em modo debug
python main.py --debug

# Executar com configuração específica
python main.py --config config/custom_schedule.json
```

### ⚡ Modo de Produção
```bash
# Executar em background
nohup python main.py > output.log 2>&1 &

# Ou usando o supervisor (recomendado)
supervisord -c supervisor.conf
```

### 🔄 Atualização de Horários
```bash
# Atualizar horários sem reiniciar
python main.py --update-schedule config/new_schedule.json
```

## 📊 Monitoramento e Logs

### 📈 Visualização de Logs
```bash
# Ver logs em tempo real
tail -f logs/automacao.log

# Ver últimos 100 logs
tail -n 100 logs/automacao.log
```

### 🔍 Depuração
```bash
# Executar em modo verbose
python main.py --verbose

# Executar com navegador visível
python main.py --no-headless
```

## 🚀 Deploy

### 📦 Deploy Local
1. **Configurar Serviço do Sistema**
```bash
# Windows (PowerShell Admin)
New-Service -Name "NeuroWeaveTasker" -BinaryPathName "python main.py"

# Linux (systemd)
sudo cp deploy/neuroweave.service /etc/systemd/system/
sudo systemctl enable neuroweave
sudo systemctl start neuroweave
```

### ☁️ Deploy em Servidor
1. **Preparar Ambiente**
```bash
# Instalar dependências do sistema
sudo apt-get update
sudo apt-get install python3-venv supervisor

# Clonar repositório
git clone https://github.com/jcjesus/NeuroWeaveTaskerBot.git
cd NeuroWeaveTaskerBot

# Configurar ambiente
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. **Configurar Supervisor**
```ini
[program:neuroweave]
command=/path/to/.venv/bin/python main.py
directory=/path/to/NeuroWeaveTaskerBot
user=www-data
autostart=true
autorestart=true
stderr_logfile=/var/log/neuroweave.err.log
stdout_logfile=/var/log/neuroweave.out.log
```

3. **Iniciar Serviço**
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start neuroweave
```

### 🐳 Deploy com Docker
1. **Construir Imagem**
```bash
docker build -t neuroweave .
```

2. **Executar Container**
```bash
docker run -d \
  --name neuroweave \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/logs:/app/logs \
  neuroweave
```

## 🔧 Manutenção

### 🔄 Atualização
```bash
# Atualizar código
git pull origin main

# Atualizar dependências
pip install -r requirements.txt --upgrade

# Reiniciar serviço
sudo systemctl restart neuroweave  # Linux
Restart-Service NeuroWeaveTasker   # Windows
```

### 🧹 Limpeza
```bash
# Limpar logs antigos
find logs/ -name "*.log" -mtime +30 -delete

# Limpar cache
python clean.py
```

## 🤝 Contribuição
1. 🍴 Fork o projeto
2. 🔄 Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit suas mudanças (`git commit -m 'Add: nova feature'`)
4. 📤 Push para a Branch (`git push origin feature/AmazingFeature`)
5. 🔍 Abra um Pull Request

## 📞 Suporte

### 🆘 Precisa de Ajuda?
- 📧 Email: suporte@exemplo.com
- 💬 Issues: [GitHub Issues](https://github.com/jcjesus/NeuroWeaveTaskerBot/issues)
- 📚 Wiki: [Documentação](https://github.com/jcjesus/NeuroWeaveTaskerBot/wiki)

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.