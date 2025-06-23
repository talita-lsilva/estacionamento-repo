# Estacionamento Flask

Este projeto é uma aplicação web desenvolvida em Flask para gerenciar um estacionamento com 150 vagas. Cada vaga é representada como um quadradinho na interface do usuário.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de diretórios:

```
estacionamento-flask
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── index.html
├── requirements.txt
├── config.py
└── README.md
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd estacionamento-flask
   ```

2. Crie um ambiente virtual:
   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute a aplicação:
   ```
   flask run
   ```

2. Acesse a aplicação no seu navegador em `http://127.0.0.1:5000`.

## Funcionalidades

- Visualização das 150 vagas de estacionamento.
- Indicação de vagas ocupadas e livres.
- Interface responsiva e amigável.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Faça um fork do repositório e envie suas pull requests.

## Licença

Este projeto está licenciado sob a MIT License.