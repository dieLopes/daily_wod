
# Daily WOD API

Este serviço oferece uma API para gerenciar treinos de CrossFit (WODs) e suas variações diárias. A API permite criar, listar, atualizar e excluir informações sobre os treinos e seus detalhes diários.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para criação da API, baseado em Python.
- **SQLAlchemy**: ORM (Object-Relational Mapping) utilizado para interagir com o banco de dados PostgreSQL.
- **Alembic**: Ferramenta de migração de banco de dados.
- **PostgreSQL**: Banco de dados utilizado para persistir os dados.
- **Docker**: Utilizado para containerizar a aplicação e facilitar o deploy.
- **pytest**: Framework de testes para garantir que a API e seus componentes funcionem corretamente.
- **Swagger (via FastAPI)**: Para documentação automática da API e testes interativos.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/daily_wod.git
```

2. Criar o arquivo .env:
   
   Crie o arquivo .env com as variáveis de ambiente necessários. É possível utilizar o arquivo .env.example como exemplo.

3. Instale as dependências do projeto:

   Para produção:

```bash
pip install -r requirements.txt
```

4. Rode os containers com Docker Compose:

```bash
docker-compose up --build
```

5. Acesse a API via Swagger UI:
   
   Após subir os containers, a API estará disponível em:

```
http://localhost:8000/docs
```

## Endpoints

### 1. WODs

- **GET /wods/**: Lista todos os WODs disponíveis.
  
  **Exemplo de resposta:**
  ```json
  [
    {
      "id": 1,
      "type": "FOR_TIME",
      "time_cap": 20,
      "description": "Complete 5 rounds of 10 push-ups, 15 squats, and 20 burpees"
    },
    {
      "id": 2,
      "type": "AMRAP",
      "time_cap": 30,
      "description": "Complete as many rounds as possible of 10 pull-ups, 15 sit-ups, and 20 lunges"
    }
  ]
  ```

- **GET /wods/{id}**: Busca um WOD específico pelo ID.
  
  **Exemplo de resposta:**
  ```json
  {
    "id": 1,
    "type": "FOR_TIME",
    "time_cap": 20,
    "description": "Complete 5 rounds of 10 push-ups, 15 squats, and 20 burpees"
  }
  ```

- **POST /wods/**: Cria um novo WOD.
  
  **Exemplo de payload:**
  ```json
  {
    "type": "AMRAP",
    "time_cap": 30,
    "description": "Complete as many rounds as possible of 10 push-ups, 20 squats"
  }
  ```

- **PUT /wods/{id}**: Atualiza um WOD existente pelo ID.
  
  **Exemplo de payload:**
  ```json
  {
    "type": "EMOM",
    "time_cap": 25,
    "description": "Complete 5 rounds of 10 push-ups every minute"
  }
  ```

- **DELETE /wods/{id}**: Deleta um WOD pelo ID.

### 2. Daily WODs

- **GET /daily_wods/**: Lista todos os WODs diários.
  
  **Exemplo de resposta:**
  ```json
  [
    {
      "id": 1,
      "warm_up": "5 minutes of jump rope",
      "skill": "Handstand push-ups",
      "wod_id": 1,
      "date": "2025-04-28",
      "wod": {
        "id": 1,
        "type": "FOR_TIME",
        "time_cap": 20,
        "description": "Complete 5 rounds of 10 push-ups, 15 squats, and 20 burpees"
      }
    }
  ]
  ```

- **GET /daily_wods/{id}**: Busca um WOD diário pelo ID.
  
  **Exemplo de resposta:**
  ```json
  {
    "id": 1,
    "warm_up": "5 minutes of jump rope",
    "skill": "Handstand push-ups",
    "wod_id": 1,
    "date": "2025-04-28",
    "wod": {
      "id": 1,
      "type": "FOR_TIME",
      "time_cap": 20,
      "description": "Complete 5 rounds of 10 push-ups, 15 squats, and 20 burpees"
    }
  }
  ```

## Testes

Para rodar os testes do projeto, utilize o comando abaixo:

```bash
pytest
```

Isso irá rodar os testes e garantir que todos os endpoints estão funcionando corretamente.

## Contribuição

1. Faça o fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
