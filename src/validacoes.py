"""Regras de validação das entradas do TaskTracker (Regras 2.3 do planejamento)."""
import re
from datetime import datetime

STATUS_PENDENTE = "Pendente"
STATUS_CONCLUIDA = "Concluída"

# Aceita Alta, Média (com ou sem acento) e Baixa, sem diferenciar maiúsculas.
_PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}

# Formatos de data reconhecidos: DD/MM/AAAA (enunciado) e AAAA-MM-DD (planejamento).
_FORMATOS_DATA = (
    (re.compile(r"^\d{2}/\d{2}/\d{4}$"), "%d/%m/%Y"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
)


def titulo_valido(texto):
    """Regra 2.3: o título não pode ficar em branco nem ter só espaços."""
    return bool(texto and texto.strip())


def normalizar_prioridade(texto):
    """Regra 2.3: só Alta, Média (ou Media) e Baixa. Devolve None se for inválida."""
    return _PRIORIDADES.get((texto or "").strip().lower())


def validar_data_limite(texto):
    """A data limite é opcional. Aceita formato livre, DD/MM/AAAA ou AAAA-MM-DD.

    Retorna (ok, valor). Se o texto estiver em um dos dois formatos de data, ela
    precisa existir de verdade (31/02/2026 é rejeitada). Outro texto é aceito.
    """
    valor = (texto or "").strip()
    for padrao, formato in _FORMATOS_DATA:
        if padrao.match(valor):
            try:
                datetime.strptime(valor, formato)
            except ValueError:
                return False, valor
    return True, valor


def tarefa_existe(texto, tarefas):
    """Regra 2.3: só se conclui uma tarefa já cadastrada. Devolve o índice ou None."""
    texto = (texto or "").strip()
    if texto.isdigit() and 1 <= int(texto) <= len(tarefas):
        return int(texto) - 1
    return None
