# Workshop Fábrica 2024.2

Este é um projeto Django desenvolvido para o workshop Fábrica 2024.2.

## Requisitos

- Python 3.x
- Django 5.1

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/Joelsonsmendonca/workshop-fabrica-2024.2.git
    cd workshop-fabrica-2024.2
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Criar um Superusuário

Para acessar o painel de administração do Django, você precisará criar um superusuário. Siga os passos abaixo:

1. No terminal, execute o comando:
    ```bash
    python manage.py createsuperuser
    ```

2. Você será solicitado a fornecer um nome de usuário, endereço de e-mail e senha. Preencha as informações conforme solicitado.

3. Após criar o superusuário, você poderá acessar o painel de administração em `http://127.0.0.1:8000/admin/` usando as credenciais do superusuário.

## Uso

- Acesse o servidor de desenvolvimento em `http://127.0.0.1:8000/`.
- Faça login no painel de administração em `http://127.0.0.1:8000/admin/` com as credenciais do superusuário.

## Estrutura do Projeto

- `manage.py`: Utilitário de linha de comando do Django.
- `project/`: Diretório do projeto Django.
- `app/`: Diretório do aplicativo Django.

## Licença

Este projeto não está licenciado.