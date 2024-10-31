<!-- ![logo do projeto](assets/logo.png){ width="300" .center} -->
# FastDeploy

O objetivo desse projeto é ajudar cientistas de dados e engenheiros de machine learning a disponibilizar e utilizar facilmente seus modelos. Isso é feito via comandos no CLI!

FastDeploy é um CLI que facilita o processo de deploy de modelos de machine learning via Docker, disponibilizando-os em uma API REST com uma linha de comando.

{% include "templates/cards.html" %}

{% include "templates/instalacao.md" %}

## Como usar?

### deploy

Esse comando cria e inicia um container Docker com seu modelo de machine learning.

**Uso**:
```bash
{{ commands.run }} [OPÇÕES] [ARGUMENTOS]
```
#### Argumentos
* image_name: (str) — Nome da imagem Docker a ser criada e utilizada.
    - Default: 'fastdeploy'
    - Exemplo: `{{ commands.run }} fastdeploy`

* port: (int) — Porta para expor a API REST no host.
    - Default: 8000
    - Exemplo: `{{ commands.run }} fastdeploy 8080`

#### Opções
* --verbose: (bool) — Habilita a exibição de logs completos do container (e conexão do terminal com o container).
    - Exemplo: `{{ commands.run }} fastdeploy 8000 --verbose`

## Exemplos de Uso
Para criar e executar a imagem Docker 'fastdeploy' na porta 8000, com logs:
```bash
{{ commands.run }} --verbose
```

Caso deseje rodar o container em background e sem logs:
```bash
{{ commands.run }}
```