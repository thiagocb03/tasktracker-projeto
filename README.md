# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), desenvolvido em Python 3 para a
disciplina **Bootcamp II** (CEUB EAD), Fase 2 (Entrega Intermediária).

**Autor:** Thiago Castro Barreto, Ciências de Dados.

## Descrição funcional
O TaskTracker centraliza as tarefas do dia a dia em um único programa de terminal.
O menu funciona em laço contínuo, com três opções:

1. **Cadastrar nova tarefa:** pede título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas:** mostra todas as propriedades de cada tarefa,
   ordenadas por prioridade (Alta, Média, Baixa), com um resumo ao final.
3. **Sair da aplicação.**

### Regras de negócio
- **Título:** obrigatório. Entradas vazias ou só com espaços são rejeitadas e o programa pergunta de novo.
- **Descrição:** texto livre.
- **Prioridade:** aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas de minúsculas. Outros valores geram erro e a pergunta é repetida.
- **Data limite:** formato livre ou `DD/MM/AAAA`. Se estiver nesse formato, precisa ser uma data real.
- **Status:** definido automaticamente como `Pendente` no cadastro.
- **Lista vazia:** o programa informa que não há tarefas cadastradas no momento.

## Tecnologias utilizadas
- Python 3.8 ou superior (somente biblioteca padrão, sem dependências externas)
- Git e GitHub para versionamento

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
   Em alguns sistemas o comando é `python3 src/main.py`.

## Estrutura do repositório
```
tasktracker-projeto/
├── README.md                    # Documentação principal
├── .gitignore                   # Ignora arquivos temporários do Python e ambientes virtuais
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural da Fase 1
└── src/
    └── main.py                  # Código-fonte da aplicação
```

## Observação
Os dados ficam apenas em memória e são perdidos ao encerrar o programa.
O desenvolvimento teve apoio de IA generativa (Claude, da Anthropic), e o código foi revisado pelo autor.
