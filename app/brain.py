# Memória simples em RAM
memory = {}

def responder(user_id: str, message: str) -> str:
    msg = message.lower().strip()

    # Inicializa memória do usuário
    if user_id not in memory:
        memory[user_id] = {"stage": "inicio"}

    stage = memory[user_id]["stage"]

    if stage == "inicio":
        if msg in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]:
            memory[user_id]["stage"] = "menu"
            return (
                "Olá! 👋\n"
                "Como posso te ajudar?\n\n"
                "1️⃣ Orçamento\n"
                "2️⃣ Informações"
            )
        else:
            return "Oi! Digite *oi* para começar 🙂"

    if stage == "menu":
        if msg == "1":
            memory[user_id]["stage"] = "orcamento"
            return "Perfeito! Que tipo de móvel você quer orçar?"
        elif msg == "2":
            return "Somos uma marcenaria especializada em móveis sob medida 🪵"
        else:
            return "Escolha uma opção válida: 1️⃣ ou 2️⃣"

    if stage == "orcamento":
        return f"Legal! Vou anotar que você quer um orçamento de: {message}"

    return "Desculpa, ainda não entendi isso."
