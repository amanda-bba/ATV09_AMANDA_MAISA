# ATV09 - Migração do Portal Web Black Coquette para Django

## Dupla
* Amanda Bispo Barros de Araújo
* Maisa Bezerra Azarias
* Turma: 513 

## Sobre o Projeto
Nesta atividade, pegamos o portal web Black Coquette(que tínhamos criado na ATV07) e migramos a estrutura toda para o framework Django.

A principal mudança é que agora o site não é mais estático: ele roda dinamicamente integrado a um banco de dados SQLite. Isso significa que conseguimos cadastrar, editar e gerenciar as páginas e os menus de navegação direto pelo painel de administração nativo do Django (`/admin`).

## Tecnologias e Ferramentas
* **Linguagem:** Python 3
* **Framework:** Django 5.x
* **Front-end:** HTML5, CSS3 (com Flexbox) e JavaScript (para os efeitos de brilho)
* **Banco de Dados:** SQLite3

## Como Rodar o Projeto na Sua Máquina

Para testar o projeto localmente, siga os passos abaixo no terminal:

#1. Entrar na pasta do projeto

cd ~/ATV09_AMANDA_MAISA

#2. Configurar o ambiente virtual

Crie a venv rodando:

python3 -m venv venv

Agora ative o ambiente virtual conforme o seu sistema operacional:

Linux ou macOS:
source venv/bin/activate

Windows (PowerShell):
PowerShell
.\venv\Scripts\Activate.ps1

#3. Instalar as dependências

Com a venv ativa, instale o Django:

pip install django

#4. Rodar as migrações do banco de dados

Acesse a pasta onde está o arquivo manage.py e aplique os arquivos de migração:

cd amanda_maisa
python manage.py makemigrations
python manage.py migrate

#5. Criar o superusuário (Acesso ao Admin)

Para ter acesso ao painel administrativo do Django e gerenciar os conteúdos, crie uma conta com o comando:

python manage.py createsuperuser

O terminal vai pedir um nome de usuário, e-mail e uma senha.

#6. Iniciar o servidor
Por fim, ligue o servidor local:

python manage.py runserver

##Links de Acesso

Com o servidor rodando, abra o seu navegador e acesse:

Site Principal: http://127.0.0.1:8000/
Painel Administrativo: http://127.0.0.1:8000/admin/ (Use as credenciais criadas no passo 5 para entrar)

