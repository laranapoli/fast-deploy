# FastDeploy
FastDeploy é uma ferramenta CLI que simplifica o deploy de modelos de machine learning como APIs REST em containers Docker.

## Instalação
Clone o repositório e execute:
```bash
poetry install
```

## Comando Principal
 
### serve

Inicia um container Docker com seu modelo.

**Uso**:
```bash
poetry run serve [image_name] [port] [--verbose]
```
- image_name: Nome da imagem Docker (default: 'fastdeploy')
- port: Porta da API (default: 8000)
- --verbose: Exibe logs detalhados (e conecta container ao terminal)

> [!IMPORTANT]  
> Atualmente a única implementação de carregamento de modelos é para classificadores treinados com Scikit-Learn!