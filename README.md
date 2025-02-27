# Projeto Django: Controle de Estoque
Descrição: Processo para criação de um projeto de controle de estoque contenado apps
01. Criação do repositório
> mkdir name_da_pasta

02. acessar o repositório
> cd nome_da_pasta

03. criar o ambiente virtual
> python -m venv nome do ambiente virtual

04. acessar o ambiente virtual
> nome_do_ambiente_virtual\Scripts\activate

05. instalar o pacote (django,...)
-instalando um pacote específico
> pip install django
- instalando lista de pacotes
> pip install -r requeriments.txt

06. Criação de projeto
> django-admin startproject nome_projeto .

07. criação de app
> django-admin startapp nome_app

08. Criação de model.py[name_app/models.py] e configuração no arquivo settings.py[nome_projeto/settings.py]
> 

09. Realizar as migrações no banco de dados
- Faz as migrações do models
> python manage.py makemigrations
- Aplica as migrações no banco de dados
> python manage.py migrate

10. Criação do Super Usuário
> python manage.py createsuperuser

11. startar o servidor de desenvolvimento
> python manage.py runserver

