from app.memory import get_state, set_state

def responder(user_id: str, message: str) -> str:
    message = message.lower().strip()
    state = get_state(user_id)

    # início da conversa
    if not state:
        set_state(user_id, {"step": "menu"})
        return "Olá! 😄 Você quer *orçamento* ou *informações*?"

    # menu principal
    if state["step"] == "menu":
        if "orçamento" in message:
            set_state(user_id, {"step": "orcamento_tipo"})
            return "Perfeito! Qual tipo de móvel você deseja?"
        elif "informação" in message:
            return "Posso te ajudar com prazos, materiais ou valores médios."
        else:
            return "Por favor, responda *orçamento* ou *informações*."

    # fluxo de orçamento
    if state["step"] == "orcamento_tipo":
        set_state(user_id, {"step": "final"})
        return f"Legal! Um(a) **{message}**. Em breve um especialista continua 😉"

    return "Não entendi muito bem. Pode repetir?"
