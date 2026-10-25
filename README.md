# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), desenvolvido em Python 3 para a
disciplina **Bootcamp II** (CEUB EAD) e empacotado com **Docker** na entrega final.

**Autor:** Thiago Castro Barreto, Ciências de Dados, **RA:** 22301452.

## Sumário
- [Visão geral](#visão-geral)
- [Funcionalidades e regras de negócio](#funcionalidades-e-regras-de-negócio)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Execução com Docker (recomendado)](#execução-com-docker-recomendado)
- [Execução sem Docker](#execução-sem-docker)
- [Exemplo de uso](#exemplo-de-uso)
- [Decisões técnicas da conteinerização](#decisões-técnicas-da-conteinerização)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Solução de problemas](#solução-de-problemas)
- [Versionamento e fases do projeto](#versionamento-e-fases-do-projeto)

## Visão geral
Pessoas e equipes costumam perder prazos e prioridades quando as tarefas ficam espalhadas em
anotações e conversas. O TaskTracker centraliza o cadastro e o acompanhamento das tarefas em um
único programa de terminal, com validação das entradas e um resumo do progresso.

Na Fase 3, a aplicação foi **conteinerizada**: a imagem Docker carrega o Python e o código,
e o `docker-compose.yml` configura o terminal interativo. Assim o programa roda de forma idêntica
em qualquer computador que tenha o Docker, sem instalar o Python.

## Funcionalidades e regras de negócio
O menu funciona em laço contínuo, com as opções:

1. **Cadastrar nova tarefa:** pede título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas:** mostra todas as propriedades, ordenadas por prioridade
   (Alta, Média, Baixa), com um resumo de pendentes, concluídas e total.
3. **Concluir tarefa:** altera o status de uma tarefa cadastrada de `Pendente` para `Concluída`.
4. **Sair da aplicação.**

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e a pergunta se repete. |
| Descrição | Texto livre. |
| Prioridade | Aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas de minúsculas. Outros valores geram erro e a pergunta se repete. |
| Data limite | Opcional. Formato livre, `DD/MM/AAAA` ou `AAAA-MM-DD`. Se estiver em um formato de data, ela precisa existir de verdade (31/02/2026 é recusada). |
| Status | Definido automaticamente como `Pendente` no cadastro. |
| Concluir | Só é possível para uma tarefa já cadastrada. |
| Lista vazia | O programa informa que não há tarefas cadastradas no momento. |

Os dados ficam apenas em memória e são perdidos ao encerrar o programa.

## Tecnologias utilizadas
- Python 3 (somente a biblioteca padrão, sem dependências externas)
- Docker e Docker Compose (imagem base `python:3.11-slim`)
- Git e GitHub para versionamento

## Execução com Docker (recomendado)

### Pré-requisitos
- Docker instalado e **em execução**. No Windows, abra o Docker Desktop e espere aparecer
  "Engine running".
- Um terminal aberto na **pasta raiz do repositório** (a que contém o `Dockerfile`).

### 1. Como construir a imagem
```bash
docker build -t tasktracker-app .
```
O ponto final (`.`) é obrigatório: indica que o `Dockerfile` está na pasta atual. A primeira
construção demora um pouco, porque baixa a imagem base do Python.

### 2. Como rodar o container em modo isolado
```bash
docker run -it --rm tasktracker-app
```
O `-it` mantém o terminal interativo (o programa usa `input()`), e o `--rm` apaga o container
automaticamente ao sair.

### 3. Como rodar via orquestração (recomendado)
```bash
docker compose run --rm tasktracker-app
```
O Docker Compose lê o `docker-compose.yml`, constrói a imagem se for preciso e abre o terminal
interativo com as configurações corretas, sem precisar lembrar de nenhuma flag.

### Comandos úteis
| Objetivo | Comando |
|---|---|
| Ver as imagens criadas | `docker images` |
| Ver os containers (rodando ou parados) | `docker ps -a` |
| Remover a imagem | `docker rmi tasktracker-app` |

## Execução sem Docker
Requer Python 3.8 ou superior.
```bash
git clone https://github.com/thiagocb03/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```
Em alguns sistemas o comando é `python3 src/main.py` ou `py src/main.py`.

## Exemplo de uso
```text
===== TASKTRACKER =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Concluir tarefa
4. Sair da aplicação
Escolha uma opção: 1

=== Cadastrar nova tarefa ===
Título da tarefa (obrigatório):
Erro: o título é obrigatório e não pode ficar em branco. Tente novamente.
Título da tarefa (obrigatório): Estudar Docker
Descrição da tarefa (opcional): Praticar build e run
Prioridade (Alta, Média ou Baixa): urgente
Erro: prioridade inválida. Digite exatamente Alta, Média ou Baixa.
Prioridade (Alta, Média ou Baixa): Alta
Data limite (opcional, ex.: 15/10/2026): 25/10/2026
Tarefa cadastrada com sucesso!

=== Tarefas cadastradas ===
--------------------------------------------
Tarefa nº 1
  Título     : Estudar Docker
  Descrição  : Praticar build e run
  Prioridade : Alta
  Data limite: 25/10/2026
  Status     : Pendente
--------------------------------------------
Pendentes: 1 | Concluídas: 0 | Total: 1
```

## Decisões técnicas da conteinerização

### Dockerfile (a receita)
| Instrução | Para que serve |
|---|---|
| `FROM python:3.11-slim` | Base leve do sistema, só com o Python 3.11. Menor tamanho e inicialização mais rápida que a imagem completa. |
| `WORKDIR /app` | Define a pasta central de operações dentro do container. |
| `ENV PYTHONUNBUFFERED=1` | Faz o Python enviar a saída imediatamente ao terminal, sem guardar em buffer. |
| `COPY src/ /app/src/` | Injeta o código local no container. Só o necessário entra na imagem. |
| `CMD ["python", "src/main.py"]` | Gatilho que dispara a execução da aplicação. |

Não há `pip install`, porque o projeto não tem dependências externas (`requirements.txt` só
documenta isso). O `.dockerignore` mantém o contexto de build pequeno.

### docker-compose.yml (o maestro)
| Configuração | Para que serve |
|---|---|
| `build: .` | Constrói a imagem a partir do `Dockerfile` da pasta atual. |
| `image: tasktracker-app` | Dá à imagem o mesmo nome usado no `docker build`. |
| `stdin_open: true` | Mantém o canal de entrada de dados aberto, necessário para o `input()`. |
| `tty: true` | Aloca um terminal virtual, simulando o seu console. |

Um container isolado, por padrão, não recebe digitação do usuário. Por isso a CLI interativa
precisa dessas duas opções.

## Estrutura do repositório
```text
tasktracker-projeto/
├── README.md                        # Documentação principal
├── .gitignore                       # Ignora arquivos temporários do Python e ambientes virtuais
├── .dockerignore                    # Reduz o contexto de build do Docker
├── requirements.txt                 # Dependências (só biblioteca padrão)
├── Dockerfile                       # Receita da imagem Docker
├── docker-compose.yml               # Orquestra a execução interativa no terminal
├── docs/
│   ├── planejamento_logico.pdf      # Planejamento lógico da Fase 1
│   └── mapeamento_arquitetural.pdf  # Mapeamento arquitetural para Git e GitHub (Fase 1)
└── src/
    ├── main.py                      # Ponto de entrada e laço principal do menu
    ├── menu.py                      # Exibe o menu, lê a opção e chama a função correspondente
    ├── tarefas.py                   # cadastrar_tarefa, listar_tarefas e concluir_tarefa
    └── validacoes.py                # Regras de validação das entradas
```

## Solução de problemas
| Sintoma | Causa provável e solução |
|---|---|
| `docker build ... requires 1 argument` | Faltou o ponto final. Use `docker build -t tasktracker-app .` |
| `Cannot connect to the Docker daemon` ou erro de conexão | O Docker não está em execução. Abra o Docker Desktop e espere o "Engine running". |
| O menu aparece, mas não aceita digitação | Faltou `-it` no `docker run`. Use o comando com `-it` ou o `docker compose run`. |
| Acentos aparecem errados no terminal do Windows | Rode `chcp 65001` e execute de novo. Alternativa: digite `media` (sem acento). |
| `docker compose` não é reconhecido | Atualize o Docker Desktop. Em versões antigas o comando é `docker-compose`. |

## Versionamento e fases do projeto
- **Fase 1:** planejamento lógico, decomposição do problema e mapeamento arquitetural (`docs/`).
- **Fase 2:** implementação do menu e das regras de negócio em Python, com versionamento em Git.
- **Fase 3:** conteinerização com `Dockerfile` e orquestração com `docker-compose.yml`.

O desenvolvimento usou uma branch por funcionalidade (`feature/validacoes`, `feature/tarefas`,
`feature/menu`, `feature/docker` e `docs/fase1`), mescladas na `main`. O histórico de commits
registra a evolução do projeto.

## Observação
O desenvolvimento teve apoio de IA generativa (Claude, da Anthropic), e o código foi revisado pelo autor.
