"""TaskTracker - ponto de entrada do programa (Bootcamp II, Fase 2)."""
from menu import exibir_menu, processar_opcao


def main():
    tarefas = []  # lista vazia que guarda as tarefas cadastradas (em memória)
    continuar = True
    while continuar:  # laço principal do menu de opções
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        continuar = processar_opcao(opcao, tarefas)  # False quando o usuário sai


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada interrompida. Encerrando a aplicação. Até logo!")
