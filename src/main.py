from langchain.agents import create_agent 

from langchain_ollama.llms import OllamaLLM
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.utils.uuid import uuid7


model = OllamaLLM(model = "llama3.2", checkpointer=InMemorySaver())
agent = create_agent(model = model, tools = [])

config = {"configurable": {"thread_id": str(uuid7())}}

while True:

    user_input = str(input(">>> "))

    result = agent.invoke(
        {"messages": [{"role": "user",
                      "content": user_input}]}, config = config,)
    
    print(result["messages"][1].content)
    

    