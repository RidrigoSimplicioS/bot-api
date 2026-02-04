def extract_whatsapp_data(payload: dict):
    """
    Extrai número do usuário e mensagem
    em um formato padronizado para o cérebro
    """

    try:
        message = payload["message"]
        from_number = payload["from"]

        return from_number, message

    except KeyError:
        return None, None
