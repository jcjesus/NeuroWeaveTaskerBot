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

##### Opção 1: Docker Desktop ⚠️

> ⚠️ **Aviso de Performance**: Esta opção consome mais recursos do sistema e tem performance computacional reduzida em comparação com a Opção 2 (WSL2). Recomendada apenas se você precisar da interface gráfica do Docker Desktop.

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

##### Opção 2: Docker com WSL2 ⚠️

> ⚠️ **Recomendação de Performance**: Esta é a opção mais eficiente para Windows em termos de consumo de memória e processamento. O Docker Desktop (Opção 1) pode consumir significativamente mais recursos do sistema devido à sua interface gráfica e serviços adicionais, enquanto o WSL2 oferece performance nativa similar ao Linux.

1. **Requisitos Mínimos WSL2**
- Windows 10 Home ou Pro versão 2004 (Build 19041) ou superior
- Windows 11
- Processador com suporte para virtualização habilitada na BIOS

2. **Instalar WSL2**
```bash
# Habilitar recursos necessários (PowerShell como Administrador)
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Reiniciar o computador

# Definir WSL2 como versão padrão
wsl --set-default-version 2
```

# Download do Pacote de Atualização do WSL2:
[📥 Clique aqui para baixar o pacote de atualização do WSL2](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

3. **Instalar Ubuntu no WSL2**
```bash
# Instalar Ubuntu via Microsoft Store
# Ou via comando:
wsl --install -d Ubuntu
```

4. **Instalar Docker Engine no Ubuntu WSL2**
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

5. **Configurar Inicialização Automática**
```bash
# Editar arquivo wsl.conf
sudo tee /etc/wsl.conf <<EOF
[boot]
command = service docker start
EOF
```

6. **Otimizações (Opcional)**
```bash
# Criar/editar arquivo .wslconfig no Windows
# Em %UserProfile%\.wslconfig
[wsl2]
memory=8GB
processors=4
networkingMode=mirrored

[experimental]
autoMemoryReclaim=gradual
```

7. **Verificar Instalação**
```bash
# Reiniciar WSL
wsl --shutdown
```
```bash
# Verificar versão do Docker
docker --version
```
```bash
# Testar Docker
docker run hello-world
```

8. **Construir e Executar no WSL2**
```bash
# Navegar até o diretório do projeto
cd NeuroWeaveTaskerBot
```
```bash
# Construir imagem
docker build -t neuroweave .
```
```bash
# Executar container
docker run -d \
  --name neuroweave \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/logs:/app/logs \
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
# Listar containers em execução
docker ps

# Listar todos os containers (incluindo parados)
docker ps -a

# Parar container
docker stop neuroweave

# Iniciar container
docker start neuroweave

# Ver logs do container
docker logs neuroweave

# Ver logs em tempo real
docker logs -f neuroweave

# Remover container
docker rm neuroweave

# Listar imagens
docker images

# Remover imagem
docker rmi neuroweave

# Verificar uso de recursos
docker stats

# Executar comando dentro do container
docker exec -it neuroweave bash

# Atualizar container com nova imagem
docker pull neuroweave:latest
docker stop neuroweave
docker rm neuroweave
docker run -d --name neuroweave -v $(pwd)/config:/app/config -v $(pwd)/logs:/app/logs neuroweave

# Limpar recursos não utilizados
docker system prune -a  # Remove containers parados, redes não utilizadas, imagens e cache

# Verificar informações do sistema Docker
docker info

# Verificar versão do Docker
docker version