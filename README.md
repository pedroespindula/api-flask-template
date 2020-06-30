# api-flask-template

Esse é o repositorio é um template de uma API Flask. Ele contem os arquivos de configuração do `Docker` e `docker-compose` que rodam todos os projetos.

Esse documento assume que você possui instalado na sua maquina o `docker`, o `docker-compose` e o `git`.

## Rodando

### Desenvolvimento

1. Clone o repositorio:

```sh
$ git clone https://github.com/pedroespindula/api-flask-template api-flask-template
```

2. Entre no projeto recem clonado:

```sh
$ cd api-flask-template
```

3. Copie as variaveis de ambiente:

```sh
$ cp .env.example .env
```

4. Atualize as variaveis de ambiente vazias com as os valores corretos (IDs, chaves e segredos)
5. Rode o `docker-compose` na raiz do projeto com o arquivo de configuração principal:

```sh
$ docker-compose up
```

### Observações

1. Caso seja necessário, force o _build_ dos containers com o seguinte comando:

```sh
$ docker-compose up --build
```

## WIKI

### Caso haja um erro de dependencia de instalação de um serviço

Execute o seguinte comando para ele buildar de novo o serviço:

```sh
$ docker-compose up --build -V --force-recreate <NOME DO SERVICO QUE ESTÁ QUEBRANDO>
```

Após isso, pare o comando que acabou de rodar e execute o fluxo normal de execução.

### Caso haja um erro de timeout no docker

Adicione a seguinte variavel de ambiente no .env:

```yml
COMPOSE_HTTP_TIMEOUT=200
```

Após isso, rode o fluxo normal de execução
