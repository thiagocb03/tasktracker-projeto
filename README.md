# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), desenvolvido em Python 3 para a
disciplina **Bootcamp II** (CEUB EAD), Fase 2 (Entrega Intermediária).

**Autor:** Thiago Castro Barreto, Ciências de Dados.

## Descrição funcional
O TaskTracker centraliza as tarefas do dia a dia em um único programa de terminal.
O menu funciona em laço contínuo, com as opções:

1. **Cadastrar nova tarefa:** pede título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas:** mostra todas as propriedades de cada tarefa,
   ordenadas por prioridade (Alta, Média, Baixa), com um resumo de pendentes, concluídas e total.
3. **Concluir tarefa:** altera o status de uma tarefa cadastrada de `Pendente` para `Concluída`.
4. **Sair da aplicação.**

### Regras de negócio
- **Título:** obrigatório. Entradas vazias ou só com espaços são rejeitadas e o programa pergunta de novo.
- **Descrição:** texto livre.
- **Prioridade:** aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas de minúsculas. Outros valores geram erro e a pergunta é repetida.
- **Data limite:** opcional. Aceita formato livre, `DD/MM/AAAA` ou `AAAA-MM-DD`. Se estiver em um desses formatos de data, ela precisa existir de verdade.
- **Status:** definido automaticamente como `Pendente` no cadastro.
- **Concluir:** só é possível para uma tarefa já cadastrada.
- **Lista vazia:** o programa informa que não há tarefas cadastradas no momento.

## Tecnologias utilizadas
- Python 3.8 ou superior (somente biblioteca padrão, sem dependências externas)
- Git e GitHub para versionamento
- Docker (previsto para a Fase 3)

## Instalação e execução
1. Instale o Python 3 (https://www.python.org/downloads/).
2. Clone o repositório:
   ```bash
   git clone https://github.com/thiagocb03/tasktracker-projeto.git
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```bash
   python src/main.py
   ```
   Em alguns sistemas o comando é `python3 src/main.py` ou `py src/main.py`.

## Estrutura do repositório
```
tasktracker-projeto/
├── README.md                        # Documentação principal
├── .gitignore                       # Ignora arquivos temporários do Python e ambientes virtuais
├── requirements.txt                 # Dependências (só biblioteca padrão)
├── Dockerfile                       # Empacotamento em container, previsto para a Fase 3
├── docs/
│   ├── planejamento_logico.pdf      # Planejamento lógico da Fase 1
│   └── mapeamento_arquitetural.pdf  # Mapeamento arquitetural para Git e GitHub (Fase 1)
└── src/
    ├── main.py                      # Ponto de entrada e laço principal do menu
    ├── menu.py                      # Exibe o menu, lê a opção e chama a função correspondente
    ├── tarefas.py                   # cadastrar_tarefa, listar_tarefas e concluir_tarefa
    └── validacoes.py                # Regras de validação das entradas
```

## Fluxo de versionamento
O desenvolvimento usou uma branch por módulo (`feature/validacoes`, `feature/tarefas`,
`feature/menu` e `docs/fase1`), mescladas na `main`. O histórico de commits mostra a evolução do projeto.

## Observação
Os dados ficam apenas em memória e são perdidos ao encerrar o programa.
O desenvolvimento teve apoio de IA generativa (Claude, da Anthropic), e o código foi revisado pelo autor.
