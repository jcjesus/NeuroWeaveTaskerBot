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

#### ⊞ Windows
- 🐍 Python 3.8+ ([Download Python](https://www.python.org/downloads/))
  ```bash
  # Verificar versão do Python
  python --version
  ```
- 📦 pip (incluído na instalação do Python)
  - Durante a instalação do Python, marque a opção "Add Python to PATH"
  - Marque também "Install pip"
- 🌐 Git ([Download Git](https://git-scm.com/download/win))
  ```bash
  # Verificar versão do Git
  git --version
  ```
- 🔧 Visual Studio Code ([Download VSCode](https://code.visualstudio.com/download)) ou PyCharm
- 📦 Microsoft Visual C++ Build Tools ([Download](https://visualstudio.microsoft.com/visual-cpp-build-tools/))

#### 🐧 Linux (Ubuntu/Debian)
1. **Atualizar Repositórios**
```bash
sudo apt update
```

2. **Instalar Python**
```bash
sudo apt install python3.8 python3.8-venv python3-pip
```

3. **Instalar Git**
```bash
sudo apt install git
```

4. **Instalar Dependências para o Playwright**
```bash
sudo apt install -y libwoff1
sudo apt install -y libopus0
sudo apt install -y libwebp6
sudo apt install -y libwebpdemux2
sudo apt install -y libenchant1c2a
sudo apt install -y libgudev-1.0-0
sudo apt install -y libsecret-1-0
sudo apt install -y libhyphen0
sudo apt install -y libgdk-pixbuf2.0-0
sudo apt install -y libegl1
sudo apt install -y libnotify4
sudo apt install -y libxslt1.1
sudo apt install -y libevent-2.1-7
sudo apt install -y libgles2
sudo apt install -y libvpx6
```

5. **Verificar Instalações**
```bash
python3 --version
```
```bash
pip3 --version
```
```bash
git --version
```

#### 🍎 MacOS
1. **Instalar Homebrew**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Instalar Python**
```bash
brew install python@3.8
```

3. **Instalar Git**
```bash
brew install git
```

4. **Verificar Instalações**
```bash
python3 --version
```
```bash
pip3 --version
```
```bash
git --version
```

### ⚙️ Configuração do Ambiente

1. **Clone o Repositório**

#### ⊞ Windows
```bash
# Via HTTPS
git clone https://github.com/jcjesus/NeuroWeaveTaskerBot.git
```
```bash
# Via SSH
git clone git@github.com:jcjesus/NeuroWeaveTaskerBot.git
```
```bash
# Entrar no diretório
cd NeuroWeaveTaskerBot
```

#### 🐧 Linux
```bash
# Via HTTPS
git clone https://github.com/jcjesus/NeuroWeaveTaskerBot.git
```
```bash
# Via SSH
git clone git@github.com:jcjesus/NeuroWeaveTaskerBot.git
```
```bash
# Entrar no diretório
cd NeuroWeaveTaskerBot
```

#### 🍎 MacOS
```bash
# Via HTTPS
git clone https://github.com/jcjesus/NeuroWeaveTaskerBot.git
```
```bash
# Via SSH
git clone git@github.com:jcjesus/NeuroWeaveTaskerBot.git
```
```bash
# Entrar no diretório
cd NeuroWeaveTaskerBot
```

2. **Configure o Ambiente Virtual**

#### ⊞ Windows (CMD)
```bash
# Criar ambiente virtual
python -m venv .venv
```
```bash
# Ativar ambiente virtual
.venv\Scripts\activate.bat
```

#### ⊞ Windows (PowerShell)
```bash
# Criar ambiente virtual
python -m venv .venv
```
```bash
# Ativar ambiente virtual
.venv\Scripts\Activate.ps1
```

#### 🐧 Linux
```bash
# Criar ambiente virtual
python3 -m venv .venv
```
```bash
# Ativar ambiente virtual
source .venv/bin/activate
```

#### 🍎 MacOS
```bash
# Criar ambiente virtual
python3 -m venv .venv
```
```bash
# Ativar ambiente virtual
source .venv/bin/activate
```

3. **Instale as Dependências**

#### ⊞ Windows
```bash
# Atualizar pip
python -m pip install --upgrade pip
```
```bash
# Instalar dependências
pip install -r requirements.txt
```
```bash
# Instalar navegadores para o Playwright
playwright install
```
```bash
# Instalar dependências do Playwright
playwright install-deps
```

#### 🐧 Linux
```bash
# Atualizar pip
python -m pip install --upgrade pip
```
```bash
# Instalar dependências
pip install -r requirements.txt
```
```bash
# Instalar navegadores para o Playwright
playwright install
```
```bash
# Instalar dependências do Playwright (requer sudo)
sudo playwright install-deps
```

#### 🍎 MacOS
```bash
# Atualizar pip
python -m pip install --upgrade pip
```
```bash
# Instalar dependências
pip install -r requirements.txt
```
```bash
# Instalar navegadores para o Playwright
playwright install
```
```bash
# Instalar dependências do Playwright
playwright install-deps
```

4. **Configuração do Editor (Recomendado)**

#### Visual Studio Code
- Instale as extensões recomendadas:
  - Python (Microsoft)
  - Pylance
  - Python Test Explorer
  - Python Debugger
  - autoDocstring

#### PyCharm
- Abra o projeto
- Configure o interpretador Python:
  1. File > Settings > Project > Python Interpreter
  2. Adicione o interpretador do ambiente virtual (.venv)

5. **Configure as Variáveis de Ambiente**

#### ⊞ Windows (CMD)
```bash
# Copiar arquivo de exemplo
copy .env.example .env
```
```bash
# Editar arquivo
notepad .env
```

#### ⊞ Windows (PowerShell)
```bash
# Copiar arquivo de exemplo
Copy-Item .env.example .env
```
```bash
# Editar arquivo
notepad .env
```

#### 🐧 Linux
```bash
# Copiar arquivo de exemplo
cp .env.example .env
```
```bash
# Editar com nano
nano .env
```
```bash
# Ou editar com vim
vim .env
```

#### 🍎 MacOS
```bash
# Copiar arquivo de exemplo
cp .env.example .env
```
```bash
# Editar com nano
nano .env
```
```bash
# Ou editar com TextEdit
open -a TextEdit .env
```

### 🔧 Configuração da Aplicação

1. **Configuração dos Horários**

#### ⊞ Windows (CMD)
```bash
# Copiar arquivo de exemplo
copy config\schedule.example.json config\schedule.json
```
```bash
# Editar arquivo
notepad config\schedule.json
```

#### ⊞ Windows (PowerShell)
```bash
# Copiar arquivo de exemplo
Copy-Item config\schedule.example.json config\schedule.json
```
```bash
# Editar arquivo
notepad config\schedule.json
```

#### 🐧 Linux
```bash
# Copiar arquivo de exemplo
cp config/schedule.example.json config/schedule.json
```
```bash
# Editar arquivo
nano config/schedule.json
```

#### 🍎 MacOS
```bash
# Copiar arquivo de exemplo
cp config/schedule.example.json config/schedule.json
```
```bash
# Editar com nano
nano config/schedule.json
```
```bash
# Ou editar com TextEdit
open -a TextEdit config/schedule.json
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

#### ⊞ Windows (CMD)
```bash
# Ativar ambiente virtual
.venv\Scripts\activate.bat
```
```bash
# Executar em modo debug
python main.py --debug
```

#### ⊞ Windows (PowerShell)
```bash
# Ativar ambiente virtual
.venv\Scripts\Activate.ps1
```
```bash
# Executar em modo debug
python main.py --debug
```

#### 🐧 Linux
```bash
# Ativar ambiente virtual
source .venv/bin/activate
```
```bash
# Executar em modo debug
python3 main.py --debug
```

#### 🍎 MacOS
```bash
# Ativar ambiente virtual
source .venv/bin/activate
```
```bash
# Executar em modo debug
python3 main.py --debug
```

### ⚡ Modo de Produção

#### ⊞ Windows (CMD)
```bash
# Executar em background
start /B python main.py > output.log 2>&1
```

#### ⊞ Windows (PowerShell)
```bash
# Executar em background
Start-Process -NoNewWindow python -ArgumentList "main.py" -RedirectStandardOutput "output.log" -RedirectStandardError "error.log"
```

#### 🐧 Linux
```bash
# Executar em background
nohup python3 main.py > output.log 2>&1 &
```

#### 🍎 MacOS
```bash
# Executar em background
nohup python3 main.py > output.log 2>&1 &
```

### 🔄 Atualização de Horários

#### ⊞ Windows
```bash
# Atualizar horários sem reiniciar
python main.py --update-schedule config\new_schedule.json
```

#### 🐧 Linux / 🍎 MacOS
```bash
# Atualizar horários sem reiniciar
python3 main.py --update-schedule config/new_schedule.json
```

## 📊 Monitoramento e Logs

### 📈 Visualização de Logs

#### ⊞ Windows (CMD)
```bash
# Ver conteúdo do arquivo de log
type logs\automacao.log
```
```bash
# Ver últimas 100 linhas
powershell Get-Content -Tail 100 logs\automacao.log
```

#### ⊞ Windows (PowerShell)
```bash
# Ver últimas 100 linhas
Get-Content -Tail 100 logs\automacao.log
```
```bash
# Monitorar em tempo real
Get-Content -Wait logs\automacao.log
```

#### 🐧 Linux
```bash
# Monitorar em tempo real
tail -f logs/automacao.log
```
```bash
# Ver últimas 100 linhas
tail -n 100 logs/automacao.log
```

#### 🍎 MacOS
```bash
# Monitorar em tempo real
tail -f logs/automacao.log
```
```bash
# Ver últimas 100 linhas
tail -n 100 logs/automacao.log
```

### 🔍 Depuração

#### ⊞ Windows
```bash
# Executar em modo verbose sem headless
python main.py --verbose --no-headless
```

#### 🐧 Linux
```bash
# Executar em modo verbose sem headless
python3 main.py --verbose --no-headless
```

#### 🍎 MacOS
```bash
# Executar em modo verbose sem headless
python3 main.py --verbose --no-headless
```

## 🚀 Deploy

### 📦 Deploy Local

#### ⊞ Windows (PowerShell Admin)
```bash
# Criar serviço do Windows
New-Service -Name "NeuroWeaveTasker" -BinaryPathName "python main.py"
```
```bash
# Iniciar serviço
Start-Service NeuroWeaveTasker
```

#### ⊞ Windows (Task Scheduler)
```bash
# Criar tarefa agendada
schtasks /create /tn "NeuroWeaveTasker" /tr "python %CD%\main.py" /sc onstart
```

#### 🐧 Linux (systemd)
```bash
# Copiar arquivo de serviço
sudo cp deploy/neuroweave.service /etc/systemd/system/
```
```bash
# Habilitar serviço
sudo systemctl enable neuroweave
```
```bash
# Iniciar serviço
sudo systemctl start neuroweave
```

#### 🍎 MacOS (launchd)
```bash
# Copiar arquivo plist
cp deploy/com.neuroweave.tasker.plist ~/Library/LaunchAgents/
```
```bash
# Carregar serviço
launchctl load ~/Library/LaunchAgents/com.neuroweave.tasker.plist
```
```bash
# Iniciar serviço
launchctl start com.neuroweave.tasker
```

### 🐳 Deploy com Docker

#### ⊞ Windows
1. **Instalar Docker Desktop**
```bash
# Download Docker Desktop do site oficial
# https://www.docker.com/products/docker-desktop
```
```bash
# Verificar instalação
docker --version
```
```bash
# Iniciar Docker Desktop
# Aguarde o ícone do Docker ficar verde na barra de tarefas
```

2. **Construir Imagem**
```bash
# Navegar até o diretório do projeto
cd NeuroWeaveTaskerBot
```
```bash
# Construir imagem
docker build -t neuroweave .
```

3. **Executar Container**
```bash
# PowerShell
docker run -d `
  --name neuroweave `
  -v ${PWD}/config:/app/config `
  -v ${PWD}/logs:/app/logs `
  neuroweave
```
```bash
# CMD
docker run -d ^
  --name neuroweave ^
  -v %cd%/config:/app/config ^
  -v %cd%/logs:/app/logs ^
  neuroweave
```

#### 🐧 Linux
1. **Instalar Docker**
```bash
# Atualizar pacotes
sudo apt update
```
```bash
# Instalar dependências
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
```bash
# Adicionar chave GPG oficial do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```bash
# Adicionar repositório
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash
# Instalar Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```
```bash
# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER
```
```bash
# Verificar instalação
docker --version
```

2. **Construir Imagem**
```bash
# Navegar até o diretório do projeto
cd NeuroWeaveTaskerBot
```
```bash
# Construir imagem
docker build -t neuroweave .
```

3. **Executar Container**
```bash
# Executar com volumes
docker run -d \
  --name neuroweave \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/logs:/app/logs \
  neuroweave
```

#### 🍎 MacOS
1. **Instalar Docker Desktop**
```bash
# Instalar Homebrew (se ainda não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
```bash
# Instalar Docker Desktop
brew install --cask docker
```
```bash
# Verificar instalação
docker --version
```
```bash
# Iniciar Docker Desktop
open /Applications/Docker.app
```

2. **Construir Imagem**
```bash
# Navegar até o diretório do projeto
cd NeuroWeaveTaskerBot
```
```bash
# Construir imagem
docker build -t neuroweave .
```

3. **Executar Container**
```bash
# Executar com volumes
docker run -d \
  --name neuroweave \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/logs:/app/logs \
  neuroweave
```

#### 🛠️ Comandos Docker Úteis (Todos os SOs)
```bash
# Verificar status do container
docker ps -a
```
```bash
# Ver logs do container
docker logs neuroweave
```
```bash
# Parar container
docker stop neuroweave
```
```bash
# Iniciar container
docker start neuroweave
```
```bash
# Remover container
docker rm neuroweave
```
```bash
# Remover imagem
docker rmi neuroweave
```

## 🔧 Manutenção

### 🔄 Atualização

#### ⊞ Windows (CMD/PowerShell)
```bash
# Atualizar código
git pull origin main
```
```bash
# Atualizar dependências
pip install -r requirements.txt --upgrade
```
```bash
# Reiniciar serviço
Restart-Service NeuroWeaveTasker
```

#### 🐧 Linux
```bash
# Atualizar código
git pull origin main
```
```bash
# Atualizar dependências
pip install -r requirements.txt --upgrade
```
```bash
# Reiniciar serviço
sudo systemctl restart neuroweave
```

#### 🍎 MacOS
```bash
# Atualizar código
git pull origin main
```
```bash
# Atualizar dependências
pip install -r requirements.txt --upgrade
```
```bash
# Reiniciar serviço
launchctl restart com.neuroweave.tasker
```

### 🧹 Limpeza

#### ⊞ Windows (CMD)
```bash
# Limpar logs antigos (mais de 30 dias)
forfiles /p "logs" /s /m *.log /d -30 /c "cmd /c del @path"
```

#### ⊞ Windows (PowerShell)
```bash
# Limpar logs antigos (mais de 30 dias)
Get-ChildItem -Path logs -Filter *.log | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item
```

#### 🐧 Linux / 🍎 MacOS
```bash
# Limpar logs antigos (mais de 30 dias)
find logs/ -name "*.log" -mtime +30 -delete
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