"""As três funcionalidades do sistema: cadastrar, listar e concluir tarefas."""
from validacoes import (
    STATUS_PENDENTE, STATUS_CONCLUIDA, ORDEM_PRIORIDADE,
    titulo_valido, normalizar_prioridade, validar_data_limite, tarefa_existe,
)

SEPARADOR = "-" * 44


def criar_tarefa(titulo, descricao, prioridade, data_limite):
    """Monta o dicionário que representa uma tarefa. Status inicial: Pendente."""
    return {
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_PENDENTE,
    }


def cadastrar_tarefa(tarefas):
    """Item 3.1 do planejamento: lê, valida e grava a nova tarefa na lista."""
    print("\n=== Cadastrar nova tarefa ===")

    while True:
        titulo = input("Título da tarefa (obrigatório): ")
        if titulo_valido(titulo):
            break
        print("Erro: o título é obrigatório e não pode ficar em branco. Tente novamente.")

    descricao = input("Descrição da tarefa (opcional): ")

    while True:
        prioridade = normalizar_prioridade(input("Prioridade (Alta, Média ou Baixa): "))
        if prioridade:
            break
        print("Erro: prioridade inválida. Digite exatamente Alta, Média ou Baixa.")

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
    print(SEPARADOR)
    print(f"Tarefa nº {numero}")
    print(f"  Título     : {tarefa['titulo']}")
    print(f"  Descrição  : {tarefa['descricao'] or '(sem descrição)'}")
    print(f"  Prioridade : {tarefa['prioridade']}")
    print(f"  Data limite: {tarefa['data_limite'] or '(não definida)'}")
    print(f"  Status     : {tarefa['status']}")


def listar_tarefas(tarefas):
    """Item 3.2 do planejamento: lista por prioridade e mostra o resumo estatístico."""
    print("\n=== Tarefas cadastradas ===")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    # O número é a posição de cadastro; a ordenação é estável, então tarefas
    # de mesma prioridade mantêm a ordem em que foram cadastradas.
    numeradas = list(enumerate(tarefas, start=1))
    numeradas.sort(key=lambda par: ORDEM_PRIORIDADE[par[1]["prioridade"]])
    for numero, tarefa in numeradas:
        _exibir_tarefa(numero, tarefa)
    print(SEPARADOR)

    pendentes = sum(1 for t in tarefas if t["status"] == STATUS_PENDENTE)
    concluidas = sum(1 for t in tarefas if t["status"] == STATUS_CONCLUIDA)
    print(f"Pendentes: {pendentes} | Concluídas: {concluidas} | Total: {len(tarefas)}")


def concluir_tarefa(tarefas):
    """Altera o status de 'Pendente' para 'Concluída' (só se a tarefa existir)."""
    print("\n=== Concluir tarefa ===")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

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
