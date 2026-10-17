"""Interface com o usuário: exibe as opções, lê a escolha e chama a função certa."""
from tarefas import cadastrar_tarefa, listar_tarefas, concluir_tarefa

# True  -> menu do planejamento da Fase 1: cadastrar, visualizar, concluir e sair.
# False -> menu mínimo do enunciado da Fase 2: cadastrar, visualizar e sair.
INCLUIR_CONCLUIR = True


def _montar_opcoes():
    opcoes = [("Cadastrar nova tarefa", cadastrar_tarefa),
              ("Visualizar tarefas cadastradas", listar_tarefas)]
    if INCLUIR_CONCLUIR:
        opcoes.append(("Concluir tarefa", concluir_tarefa))
    opcoes.append(("Sair da aplicação", None))
    return {str(i): op for i, op in enumerate(opcoes, start=1)}


def exibir_menu():
    """Exibe as opções disponíveis."""
    print("\n===== TASKTRACKER =====")
    for numero, (rotulo, _) in _montar_opcoes().items():
        print(f"{numero}. {rotulo}")


def processar_opcao(opcao, tarefas):
    """Encaminha a opção digitada para a função correspondente.

    Devolve False quando o usuário escolhe sair; caso contrário, devolve True.
    Avisa o usuário quando a opção digitada é inválida.
    """
    opcoes = _montar_opcoes()
    opcao = (opcao or "").strip()
    if opcao not in opcoes:
        print(f"Opção inválida. Por favor, escolha de 1 a {len(opcoes)}.")
        return True

    _, funcao = opcoes[opcao]
    if funcao is None:
        print("Encerrando a aplicação. Até logo!")
        return False
    funcao(tarefas)
    return True
