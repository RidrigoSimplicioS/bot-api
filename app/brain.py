from app.memory import get_state, set_state
from app.utils import normalize

def responder(user_id: str, message: str) -> str:
    msg = normalize(message)
    state = get_state(user_id)

    # INÍCIO
    if not state:
        set_state(user_id, {"step": "menu"})
        return (
            "Olá! 👋\n"
            "Sou o assistente virtual.\n\n"
            "Como posso te ajudar?\n"
            "1️⃣ Orçamento\n"
            "2️⃣ Informações"
        )

    # MENU PRINCIPAL
    if state["step"] == "menu":
        if msg in ["1", "orçamento", "orcamento"]:
            set_state(user_id, {"step": "orcamento_tipo"})
            return "Perfeito! 😊 Qual tipo de móvel você deseja?"
        elif msg in ["2", "informações", "informacao", "info"]:
            return (
                "📌 Posso te ajudar com:\n"
                "- prazos\n"
                "- materiais\n"
                "- valores médios\n\n"
                "O que você gostaria de saber?"
            )
        else:
            return "Escolha uma opção válida:\n1️⃣ Orçamento\n2️⃣ Informações"

    # FLUXO ORÇAMENTO
    if state["step"] == "orcamento_tipo":
        set_state(user_id, {"step": "final"})
        return (
            f"Ótima escolha! 🛠️\n"
            f"Um(a) *{message}*.\n\n"
            "Em breve um especialista continuará o atendimento 👌"
        )

    return "Não entendi muito bem. Pode repetir, por favor?"

