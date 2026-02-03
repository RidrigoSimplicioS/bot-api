def responder(mensagem: str) -> str:
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Olá! Como posso te ajudar hoje?"

    if "preço" in mensagem:
        return "Ainda estou aprendendo, mas em breve terei preços 😉"

    return "Desculpa, ainda não entendi isso."
