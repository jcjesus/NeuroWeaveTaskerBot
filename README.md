# 🤖 NeuroWeaveTaskerBot

## 🌟 Sobre o Projeto
Bot de automação web inteligente desenvolvido para executar tarefas programadas de forma autônoma e confiável, com agendamento personalizado de horários.

### 🎯 Principais Funcionalidades
- 🔄 Execução em horários personalizados
- 🔐 Login automático seguro
- 🎯 Navegação inteligente
- ⚡ Ações programadas
- 📊 Logging detalhado

## 🚀 Quick Start

### 📋 Pré-requisitos
- 🐍 Python 3.8+
- 📦 pip (gerenciador de pacotes Python)
- 🌐 Conexão com internet

### ⚙️ Instalação

1. **Clone o Repositório**
```bash
git clone https://seu-repositorio/NeuroWeaveTaskerBot.git
cd NeuroWeaveTaskerBot
```

2. **Configure o Ambiente Virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as Dependências**
```bash
pip install -r requirements.txt
playwright install
```

4. **Configure o Ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 🛠️ Tecnologias Utilizadas

### 🎭 Playwright
- 🚀 Automação web moderna
- 🌐 Suporte multi-navegador
- 🛡️ Gestão de contexto segura

### ⏰ APScheduler
- 📅 Agendamento preciso
- 🔄 Execução periódica
- 💾 Persistência de jobs

### 🔐 dotenv
- 🔒 Gestão segura de credenciais
- ⚙️ Configuração flexível
- 🔑 Proteção de dados sensíveis

## 📊 Status do Projeto

### 🎯 Versão Atual
```
[██████████████⠀⠀⠀⠀⠀⠀⠀⠀] 45%
```
- 📦 **Versão**: 0.1.0
- 🔄 **Status**: Em Desenvolvimento
- 📅 **Última Atualização**: Março 2024

### 📈 Status das Features
- ✅ Estrutura base do projeto
- ✅ Configuração de ambiente
- ⏳ Sistema de agendamento
- ⬜ Interface de configuração
- ⬜ Sistema de logs
- ⬜ Dashboard de monitoramento

## 🔧 Configuração

### 🔐 Variáveis de Ambiente
```env
# Configurações do Site
SITE_URL=https://exemplo.com
USERNAME=seu_usuario
PASSWORD=sua_senha

# Seletores
LOGIN_USERNAME_SELECTOR=#username
LOGIN_USERNAME_BT_NEXT=#next
LOGIN_PASSWORD_SELECTOR=#password
LOGIN_PASSWORD_BT_SELECTOR=#login
TARGET_TASK_BUTTON_SELECTOR=#task
TARGET_PAGE_SELECTOR=#page

# Agendamento (arquivo schedule.json)
SCHEDULE_CONFIG_PATH=config/schedule.json
```

### ⏰ Configuração de Horários
Crie um arquivo `config/schedule.json` com seus horários desejados:
```json
{
    "schedule": [
        {"hour": "08", "minute": "00"},
        {"hour": "12", "minute": "30"},
        {"hour": "15", "minute": "45"},
        {"hour": "19", "minute": "15"}
    ]
}
```

## 🚀 Uso

### 🎮 Comandos Básicos
```bash
# Iniciar o bot
python main.py

# Atualizar configuração de horários
python main.py --update-schedule config/new_schedule.json

# Parar o bot
Ctrl + C
```

### ⏰ Agendamento
- 🕒 Horários totalmente configuráveis
- 📊 Quantidade flexível de execuções diárias
- ⚡ Primeira execução no próximo horário programado
- 🔄 Atualização dinâmica de horários

## 📁 Estrutura do Projeto
```