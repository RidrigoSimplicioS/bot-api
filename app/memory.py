# app/memory.py

# memória simples em RAM
conversation_state = {}

def get_state(user_id: str):
    return conversation_state.get(user_id, {})

def set_state(user_id: str, state: dict):
    conversation_state[user_id] = state
