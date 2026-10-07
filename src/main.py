"""TaskTracker - gerenciador de tarefas em linha de comando (Bootcamp II, Fase 2)."""


def cadastrar_tarefa(tarefas):
    """Lê os dados de uma tarefa e a grava na lista."""
    print("\n=== Cadastrar nova tarefa ===")
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade (Alta, Média ou Baixa): ")
    data_limite = input("Data limite (opcional): ")
    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
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
