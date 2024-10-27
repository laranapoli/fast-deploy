<!-- ![logo do projeto](assets/logo.png){ width="300" .center} -->
# FastDeploy

FastDeploy é um CLI que facilita o processo de deploy de modelos de machine learning via Docker, disponibilizando-os em uma API REST com uma linha de comando.

## Comandos

### serve

Esse comando cria e inicia um container Docker com seu modelo de machine learning.

**Uso**:
```bash
poetry run serve [OPÇÕES] [ARGUMENTOS]
```
#### Argumentos
* image_name: (str) — Nome da imagem Docker a ser criada e utilizada.
    - Default: 'fastdeploy'
    - Exemplo: `poetry run serve fastdeploy`

* port: (int) — Porta para expor a API REST no host.
    - Default: 8000
    - Exemplo: `poetry run serve fastdeploy 8080`

#### Opções
* --verbose: (bool) — Habilita a exibição de logs completos do container (e conexão do terminal com o container).
    - Exemplo: `poetry run serve fastdeploy 8000 --verbose`

## Exemplos de Uso
Para criar e executar a imagem Docker 'fastdeploy' na porta 8000, com logs:
```bash
poetry run serve --verbose
```

Caso deseje rodar o container em background e sem logs:
```bash
poetry run serve
```