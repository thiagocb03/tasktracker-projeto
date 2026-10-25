"""Interface com o usuário: exibe as opções, lê a escolha e chama a função certa.

O menu é montado a partir de uma lista de pares (rótulo, função). Assim, para
mudar ou acrescentar uma opção, basta alterar a função _montar_opcoes, sem mexer
no restante. A opção "Sair" não tem função associada (None).
"""
from tarefas import cadastrar_tarefa, listar_tarefas, concluir_tarefa

# Controla se o recurso "Concluir tarefa" aparece no menu.
# True  -> menu do planejamento da Fase 1: cadastrar, visualizar, concluir e sair.
# False -> menu mínimo do enunciado da Fase 2: cadastrar, visualizar e sair.
INCLUIR_CONCLUIR = True


def _montar_opcoes():
    """Monta o menu como um dicionário {número: (rótulo, função)}.

    Os números são gerados automaticamente a partir de 1, então a opção "Sair"
    é sempre a última, qualquer que seja a quantidade de opções.
    """
    opcoes = [("Cadastrar nova tarefa", cadastrar_tarefa),
              ("Visualizar tarefas cadastradas", listar_tarefas)]
    if INCLUIR_CONCLUIR:
        opcoes.append(("Concluir tarefa", concluir_tarefa))
    opcoes.append(("Sair da aplicação", None))
    return {str(i): op for i, op in enumerate(opcoes, start=1)}


def exibir_menu():
    """Mostra na tela as opções disponíveis, cada uma com o seu número."""
    print("\n===== TASKTRACKER =====")
    for numero, (rotulo, _) in _montar_opcoes().items():
        print(f"{numero}. {rotulo}")


def processar_opcao(opcao, tarefas):
    """Encaminha a opção digitada para a função correspondente.

    Devolve False quando o usuário escolhe sair (o laço do main.py então termina)
    e True em qualquer outro caso, inclusive quando a opção é inválida: nesse caso
    só avisa o usuário e o menu aparece de novo.
    """
    opcoes = _montar_opcoes()
    opcao = (opcao or "").strip()
    if opcao not in opcoes:
        print(f"Opção inválida. Por favor, escolha de 1 a {len(opcoes)}.")
        return True

    _, funcao = opcoes[opcao]
    if funcao is None:  # a opção "Sair" não tem função associada
        print("Encerrando a aplicação. Até logo!")
        return False
    funcao(tarefas)
    return True
