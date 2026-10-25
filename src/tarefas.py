"""As funcionalidades do TaskTracker: cadastrar, listar e concluir tarefas.

Cada tarefa é um dicionário com cinco campos:
    titulo      - texto obrigatório
    descricao   - texto livre (pode ficar vazio)
    prioridade  - "Alta", "Média" ou "Baixa"
    data_limite - texto livre ou data (pode ficar vazio)
    status      - "Pendente" ou "Concluída"

As tarefas ficam em uma lista na memória, criada no main.py e passada para estas
funções. Aqui acontece a conversa com o usuário (input e print); as regras de
validação vêm do módulo validacoes.py.
"""
from validacoes import (
    STATUS_PENDENTE, STATUS_CONCLUIDA, ORDEM_PRIORIDADE,
    titulo_valido, normalizar_prioridade, validar_data_limite, tarefa_existe,
)

# Linha usada para separar visualmente uma tarefa da outra na listagem.
SEPARADOR = "-" * 44


def criar_tarefa(titulo, descricao, prioridade, data_limite):
    """Monta o dicionário que representa uma tarefa nova.

    O status inicial é sempre "Pendente", como manda o enunciado. Os textos livres
    (título e descrição) são guardados sem espaços sobrando nas pontas.
    """
    return {
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_PENDENTE,
    }


def cadastrar_tarefa(tarefas):
    """Item 3.1 do planejamento: lê os dados, valida e grava a tarefa na lista.

    Título, prioridade e data limite são perguntados em laços que só terminam
    quando a resposta for válida. A descrição aceita qualquer texto.
    """
    print("\n=== Cadastrar nova tarefa ===")

    # Título: repete a pergunta até receber um texto que não seja vazio.
    while True:
        titulo = input("Título da tarefa (obrigatório): ")
        if titulo_valido(titulo):
            break
        print("Erro: o título é obrigatório e não pode ficar em branco. Tente novamente.")

    descricao = input("Descrição da tarefa (opcional): ")

    # Prioridade: normalizar_prioridade devolve None quando a entrada é inválida.
    while True:
        prioridade = normalizar_prioridade(input("Prioridade (Alta, Média ou Baixa): "))
        if prioridade:
            break
        print("Erro: prioridade inválida. Digite exatamente Alta, Média ou Baixa.")

    # Data limite: opcional. Só é recusada se parecer uma data, mas não existir.
    while True:
        ok, data_limite = validar_data_limite(
            input("Data limite (opcional, ex.: 15/10/2026): ")
        )
        if ok:
            break
        print("Erro: data inexistente. Use uma data real ou deixe livre.")

    tarefas.append(criar_tarefa(titulo, descricao, prioridade, data_limite))
    print("Tarefa cadastrada com sucesso!")


def _exibir_tarefa(numero, tarefa):
    """Mostra todas as propriedades de uma tarefa, uma por linha.

    O prefixo "_" indica que esta função é de uso interno do módulo.
    """
    print(SEPARADOR)
    print(f"Tarefa nº {numero}")
    print(f"  Título     : {tarefa['titulo']}")
    # "or" mostra um texto de apoio quando o campo opcional está vazio.
    print(f"  Descrição  : {tarefa['descricao'] or '(sem descrição)'}")
    print(f"  Prioridade : {tarefa['prioridade']}")
    print(f"  Data limite: {tarefa['data_limite'] or '(não definida)'}")
    print(f"  Status     : {tarefa['status']}")


def listar_tarefas(tarefas):
    """Item 3.2 do planejamento: lista as tarefas por prioridade e mostra o resumo.

    Se a lista estiver vazia, avisa o usuário. Caso contrário, mostra cada tarefa
    (Alta primeiro, depois Média e Baixa) e, no fim, o total de pendentes,
    concluídas e o total geral.
    """
    print("\n=== Tarefas cadastradas ===")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    # Cada tarefa recebe o número da sua posição de cadastro (1, 2, 3...). Esse é o
    # número que o usuário digita para concluir a tarefa. A ordenação é estável:
    # tarefas de mesma prioridade mantêm a ordem em que foram cadastradas.
    numeradas = list(enumerate(tarefas, start=1))
    numeradas.sort(key=lambda par: ORDEM_PRIORIDADE[par[1]["prioridade"]])
    for numero, tarefa in numeradas:
        _exibir_tarefa(numero, tarefa)
    print(SEPARADOR)

    # Resumo estatístico: conta quantas tarefas existem em cada status.
    pendentes = sum(1 for t in tarefas if t["status"] == STATUS_PENDENTE)
    concluidas = sum(1 for t in tarefas if t["status"] == STATUS_CONCLUIDA)
    print(f"Pendentes: {pendentes} | Concluídas: {concluidas} | Total: {len(tarefas)}")


def concluir_tarefa(tarefas):
    """Muda o status de uma tarefa de "Pendente" para "Concluída".

    O usuário informa o número mostrado na listagem. Só conclui se a tarefa
    existir; avisa quando a lista está vazia, o número é inválido ou a tarefa já
    estava concluída.
    """
    print("\n=== Concluir tarefa ===")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    # tarefa_existe devolve a posição na lista, ou None se o número não servir.
    indice = tarefa_existe(input("Digite o número da tarefa a concluir: "), tarefas)
    if indice is None:
        print("Erro: tarefa não encontrada. Confira o número na listagem.")
        return

    tarefa = tarefas[indice]
    if tarefa["status"] == STATUS_CONCLUIDA:
        print("Essa tarefa já está concluída.")
        return
    tarefa["status"] = STATUS_CONCLUIDA
    print("Status alterado para concluída.")
