"""Regras de validação do TaskTracker.

Este módulo reúne as regras que decidem se uma entrada do usuário é aceita ou
rejeitada (item 2.3 do planejamento lógico da Fase 1). Aqui nenhuma função lê o
teclado nem imprime mensagens: cada uma só recebe um texto e devolve um
resultado. Quem conversa com o usuário é o módulo tarefas.py. Essa separação
deixa as regras fáceis de testar e de reaproveitar.
"""
import re
from datetime import datetime

# Valores possíveis do campo "status" de uma tarefa.
STATUS_PENDENTE = "Pendente"      # status inicial, definido no cadastro
STATUS_CONCLUIDA = "Concluída"    # status depois de concluir a tarefa

# Prioridades aceitas. A chave é o texto digitado em minúsculas; o valor é a forma
# padronizada que será guardada. "media" (sem acento) também é aceita, como o
# enunciado pede. Qualquer outra entrada fica de fora e será rejeitada.
_PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}

# Ordem de exibição na listagem: número menor aparece primeiro.
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}

# Formatos de data que o programa reconhece: DD/MM/AAAA (pedido no enunciado) e
# AAAA-MM-DD (usado no planejamento da Fase 1). Cada item guarda o padrão que
# identifica o formato e o formato que o datetime usa para conferir a data.
_FORMATOS_DATA = (
    (re.compile(r"^\d{2}/\d{2}/\d{4}$"), "%d/%m/%Y"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
)


def titulo_valido(texto):
    """Diz se o título é aceito.

    Regra: o título é obrigatório. Texto vazio ou só com espaços é rejeitado.
    Exemplos: "" -> False; "   " -> False; "Estudar" -> True.
    """
    # strip() remove os espaços das pontas; se não sobrar nada, o título é inválido.
    return bool(texto and texto.strip())


def normalizar_prioridade(texto):
    """Converte o texto digitado na prioridade padronizada.

    Devolve "Alta", "Média" ou "Baixa". Se a entrada não for válida, devolve None.
    Ignora maiúsculas, minúsculas e espaços nas pontas.
    Exemplos: "ALTA" -> "Alta"; "media" -> "Média"; "urgente" -> None.
    """
    # (texto or "") evita erro caso chegue None; .get devolve None se não existir.
    return _PRIORIDADES.get((texto or "").strip().lower())


def validar_data_limite(texto):
    """Valida a data limite, que é opcional.

    Aceita formato livre, DD/MM/AAAA ou AAAA-MM-DD. Se o texto estiver em um dos
    dois formatos de data, ela precisa existir de verdade: 31/02/2026 é rejeitada.
    Qualquer outro texto (como "sem prazo") é aceito como formato livre.

    Devolve uma tupla (ok, valor): ok diz se a entrada é aceita, e valor é o texto
    já sem os espaços das pontas.
    """
    valor = (texto or "").strip()
    for padrao, formato in _FORMATOS_DATA:
        if padrao.match(valor):
            # O texto tem cara de data. Confere se o dia e o mês existem de verdade.
            try:
                datetime.strptime(valor, formato)
            except ValueError:
                return False, valor
    return True, valor


def tarefa_existe(texto, tarefas):
    """Confere se o número digitado corresponde a uma tarefa cadastrada.

    Regra 2.3: só se conclui uma tarefa que já está na lista. O número é a posição
    de cadastro, começando em 1. Devolve o índice na lista (começando em 0) ou
    None se o texto não for um número válido.
    Exemplo com 2 tarefas: "1" -> 0; "2" -> 1; "3" -> None; "abc" -> None.
    """
    texto = (texto or "").strip()
    if texto.isdigit() and 1 <= int(texto) <= len(tarefas):
        return int(texto) - 1
    return None
