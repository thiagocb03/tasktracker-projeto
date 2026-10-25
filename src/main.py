"""TaskTracker - ponto de entrada do programa (Bootcamp II).

Para executar:  python src/main.py
No Docker, este arquivo é o comando de partida definido no Dockerfile (CMD).
"""
from menu import exibir_menu, processar_opcao


def main():
    """Cria a lista de tarefas e mantém o menu em funcionamento até o usuário sair."""
    tarefas = []  # lista vazia que guarda as tarefas cadastradas (em memória)
    continuar = True
    while continuar:  # laço principal: mostra o menu, lê a opção e executa
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        continuar = processar_opcao(opcao, tarefas)  # False quando o usuário sai


# Este bloco só roda quando o arquivo é executado diretamente (e não quando é
# importado por outro módulo). O try/except evita uma mensagem de erro feia caso
# o usuário aperte Ctrl+C ou a entrada de dados seja encerrada de repente.
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada interrompida. Encerrando a aplicação. Até logo!")
