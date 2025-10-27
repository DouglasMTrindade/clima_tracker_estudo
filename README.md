# Clima Tracker — Sistema de Consulta e Histórico Climático

Aplicação em Python 3 que consulta informações do clima em tempo real usando a API OpenWeatherMap, identifica automaticamente a localização via ipinfo.io, registra as consultas em um banco de dados SQLite e permite visualizar ou gerenciar o histórico pelo terminal.

---

## Sumário

- Funcionalidades
- Estrutura do Projeto
- Tecnologias Utilizadas
- Configuração de Ambiente
- Como Executar
- Exemplo de Uso
- Estrutura do Banco de Dados
- Descrição dos Módulos
- Próximos Passos
- Autor
- Licença

---

## Funcionalidades

- Detecta automaticamente a localização do usuário (cidade, região e país)
- Consulta o clima atual via API OpenWeatherMap
- Armazena os dados em um banco de dados SQLite
- Lista e filtra o histórico de consultas
- Permite apagar registros específicos
- Gera logs locais (log.txt e log.json)
- Interface simples e interativa no terminal

---
## Tecnologias Utilizadas

- Python 3.12+
- SQLite3
- Requests (requisições HTTP)
- python-dotenv (variáveis de ambiente)
- JSON (armazenamento de logs estruturados)

---

## Configuração de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

- IPINFO_API_KEY=sua_chave_ipinfo
- OPENWEATHERMAP_API_KEY=sua_chave_openweather

---
Onde obter as chaves:

- ipinfo.io — gera chave gratuita para localização
- openweathermap.org/api — chave gratuita para clima

Atenção: nunca envie o arquivo `.env` para o GitHub.  
Adicione-o ao `.gitignore` para proteger suas credenciais.

Fluxo de execução:

1. Ao escolher a opção [1], o programa:
   - Detecta automaticamente a localização do usuário
   - Consulta o clima atual via API OpenWeatherMap
   - Salva os dados no banco consultas.db
   - Gera registros em log.txt e log.json

2. As demais opções permitem listar, filtrar ou apagar registros armazenados.

---

## Estrutura do Banco de Dados

Tabela: consultas

| Campo       | Tipo     | Descrição                              |
|--------------|----------|----------------------------------------|
| id           | INTEGER  | Identificador único (auto increment)   |
| cidade       | TEXT     | Nome da cidade                         |
| temperatura  | TEXT     | Temperatura atual                      |
| descricao    | TEXT     | Descrição do clima                     |
| data_hora    | TEXT     | Data e hora da consulta                |

---

## Descrição dos Módulos

### main.py
Arquivo principal do projeto.  
Exibe o menu principal, recebe a opção do usuário e chama as funções adequadas de outros módulos.

### clima_agora.py
Conecta à API do OpenWeatherMap e retorna um dicionário com as informações do clima atual, incluindo temperatura, sensação térmica, vento e descrição.

### clima_historico.py
Cria e gerencia o banco de dados SQLite (consultas.db).  
Permite salvar novas consultas, listar o histórico completo, filtrar registros por cidade e apagar registros por ID.

### localizacao.py
Obtém a localização do usuário (cidade, região e país) utilizando a API ipinfo.io.  
Retorna um dicionário com os dados de localização.

### valida_entrada.py
Controla o menu principal e valida entradas do usuário.  
Garante que apenas opções válidas sejam aceitas, evitando erros de digitação.

### log.py
Gera registros de log em dois formatos:
- log.txt — resumo legível das consultas realizadas
- log.json — formato estruturado com todos os dados detalhados da consulta

---