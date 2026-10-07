"""TaskTracker - gerenciador de tarefas em linha de comando (Bootcamp II, Fase 2)."""

STATUS_PENDENTE = "Pendente"

# Aceita Alta, Média (com ou sem acento) e Baixa, sem diferenciar maiúsculas.
PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}


def titulo_valido(texto):
    """O título é obrigatório: vazio ou só espaços em branco é rejeitado."""
    return bool(texto and texto.strip())


def normalizar_prioridade(texto):
    """Devolve 'Alta', 'Média' ou 'Baixa'; devolve None se a entrada for inválida."""
    return PRIORIDADES.get(texto.strip().lower())


def cadastrar_tarefa(tarefas):
    """Lê os dados de uma tarefa e a grava na lista."""
    print("\n=== Cadastrar nova tarefa ===")
    while True:
        titulo = input("Título da tarefa (obrigatório): ")
        if titulo_valido(titulo):
            break
        print("Erro: o título é obrigatório e não pode ficar em branco. Tente novamente.")

    descricao = input("Descrição da tarefa: ")

    while True:
        prioridade = normalizar_prioridade(input("Prioridade (Alta, Média ou Baixa): "))
        if prioridade:
            break
        print("Erro: prioridade inválida. Digite exatamente Alta, Média ou Baixa.")

    data_limite = input("Data limite (opcional): ")
    tarefas.append({
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_PENDENTE,
    })
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas."""
    print("\n=== Tarefas cadastradas ===")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"Tarefa {numero}: {tarefa['titulo']} | {tarefa['prioridade']} | {tarefa['status']}")


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    tarefas = []
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
    main()
