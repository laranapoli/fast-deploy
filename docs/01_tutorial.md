# Tutorial

Se você chegou até aqui, significa que quer aprender mais sobre o `fast-deploy`.

O objetivo desse tutorial é explicar o básico do funcionamento da aplicação em linha de comando. 


{% include "templates/instalacao.md" %}

## Os comandos

O `fast-deploy`tem um comando principal:

```bash
{{ commands.run }}
```

Esse comando é usado para para disponibilizar uma API com duas rotas:

1. `upload-model`: Rota para fazer o upload do artefado do modelo.
2. `predict`: Rota para consumir os resultados do modelo recém-disponibilizado.

!!! info "Sobre os modelos"
    É possível que a sua classe de modelos não tenha sido implementada para ser carregada pela aplicação ou processar seus resultados. Essa aplicação foi programada de acordo com o princípio de arquitura de interfaces, então basta desenvolver o código e substituir as chamadas dos métodos.

Caso seja invocado sem nenhum parâmetro, a imagem do container Docker terá o nome de `fastdeploy`e terá a porta 8000 exposta. Além disso, o terminal ficará desconectado do container, sem exibição de qualquer log.

## Para saber mais
Caso queira descobrir mais utilidades para os comandos, você pode usar a flag `--help` junto ao comando. Dessa forma irá descobrir novas formas de usar o `fast-deploy`.

```bash
fast-deploy [comando] --help
```

Para visualizar a página de documentações do FastApi, acesse: `0.0.0.0:8000/docs`

## Sobre esse tutorial
Esse tutorial foi escrito em `2024-10-29`. A aplicação pode receber atualizações e, com isso, receber novos comandos. Portanto, consultar o `--help`é uma ótima maneira de se manter atualizado!

Caso tenha encontrado algum erro no tutorial ou deseje melhorar o texto, sinta-se à vontade para contribuir com o projeto:
