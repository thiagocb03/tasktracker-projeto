"""TaskTracker - gerenciador de tarefas em linha de comando (Bootcamp II, Fase 2)."""

import re
from datetime import datetime

STATUS_PENDENTE = "Pendente"
STATUS_CONCLUIDA = "Concluída"
SEPARADOR = "-" * 44

# Aceita Alta, Média (com ou sem acento) e Baixa, sem diferenciar maiúsculas.
PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}
PADRAO_DATA = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def titulo_valido(texto):
    """O título é obrigatório: vazio ou só espaços em branco é rejeitado."""
    return bool(texto and texto.strip())


def normalizar_prioridade(texto):
    """Devolve 'Alta', 'Média' ou 'Baixa'; devolve None se a entrada for inválida."""
    return PRIORIDADES.get(texto.strip().lower())


def validar_data_limite(texto):
    """Data limite é opcional e aceita formato livre ou DD/MM/AAAA.

    Retorna (ok, valor). Se o texto estiver no formato DD/MM/AAAA, a data precisa
    existir de verdade (31/02/2026 é rejeitada). Outro texto é aceito como livre.
    """
    valor = texto.strip()
    if PADRAO_DATA.match(valor):
        try:
            datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            return False, valor
    return True, valor


def cadastrar_tarefa(tarefas):
    """Lê os dados de uma tarefa e a grava na lista."""
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
        print("Erro: data inexistente. Use DD/MM/AAAA com uma data real ou deixe livre.")

    tarefas.append({
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_PENDENTE,
    })
    print("Tarefa cadastrada com sucesso!")


def exibir_tarefa(numero, tarefa):
    """Mostra todas as propriedades de uma tarefa de forma legível."""
    print(SEPARADOR)
    print(f"Tarefa nº {numero}")
    print(f"  Título     : {tarefa['titulo']}")
    print(f"  Descrição  : {tarefa['descricao'] or '(sem descrição)'}")
    print(f"  Prioridade : {tarefa['prioridade']}")
    print(f"  Data limite: {tarefa['data_limite'] or '(não definida)'}")
    print(f"  Status     : {tarefa['status']}")


def listar_tarefas(tarefas):
    """Lista as tarefas por prioridade (Alta, Média, Baixa) e mostra o resumo."""
    print("\n=== Tarefas cadastradas ===")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    # O número é a posição de cadastro; a ordenação é estável, então tarefas
    # de mesma prioridade mantêm a ordem em que foram cadastradas.
    numeradas = list(enumerate(tarefas, start=1))
    numeradas.sort(key=lambda par: ORDEM_PRIORIDADE[par[1]["prioridade"]])
    for numero, tarefa in numeradas:
        exibir_tarefa(numero, tarefa)
    print(SEPARADOR)

    pendentes = sum(1 for t in tarefas if t["status"] == STATUS_PENDENTE)
    concluidas = sum(1 for t in tarefas if t["status"] == STATUS_CONCLUIDA)
    print(f"Pendentes: {pendentes} | Concluídas: {concluidas} | Total: {len(tarefas)}")


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    tarefas = []  # lista que guarda as tarefas (dicionários) em memória
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando a aplicação. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada interrompida. Encerrando a aplicação. Até logo!")
