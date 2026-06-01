import os
import globals

# WORRY ABOUT PERSISTENT MEMORY AS ONE OF ITS TOOLS 

# def init_session() -> int:
#     session_file = os.open(globals.current_session_memory, "a")
#     return session_file

# def close_session(session_file: int):

#     if not session_file.closed:
#         os.close(session_file)
    
#     # Session memory is non-persistent unless explicitedly saved
#     os.remove(globals.current_session_memory)
#     return

# def save_session(dialogue_record: list[tuple[str, str]], quota: int):
#     '''
#     Saves last "quota" exchanges between the user and the agent.
#     NOTE: the number of exchanges saved is arbitrary, and may be changed based on context available
#     '''