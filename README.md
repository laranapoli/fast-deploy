# FastDeploy
FastDeploy é uma ferramenta CLI que simplifica o deploy de modelos de machine learning como APIs REST em containers Docker.

## Instalação
Clone o repositório e execute:
```bash
poetry install
```

## Pré-requisitos

Antes de executar a aplicação, verifique se você possui os reguintes pré-requisitos instalados:

- **Docker**: Certifique-se de que o Docker está instalado e em funcionamento em sua máquina. Você pode verificar isso executando o seguinte comando no terminal:

    ```bash
    docker --version
    ```

    Se o Docker não estiver instalado, você pode seguir as instruções de instalação na [documentação oficial do Docker](https://docs.docker.com/engine/install/)

## Comando Principal
 
### deploy

Inicia um container Docker uma API com as rotas para fazer o upload de seu modelo e para obter seus resultados.

**Uso**:
```bash
poetry run deploy [image_name] [port] [--verbose]
```
- image_name: Nome da imagem Docker (default: 'fastdeploy')
- port: Porta da API (default: 8000)
- --verbose: Exibe logs detalhados (e conecta container ao terminal)

> [!IMPORTANT]  
> Atualmente a única implementação de carregamento de modelos é para classificadores treinados com Scikit-Learn!