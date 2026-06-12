from langchain.agents import create_agent, AgentState

from langchain_ollama.llms import OllamaLLM
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.utils.uuid import uuid7

from langchain.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langchain.agents.middleware import before_model
from langgraph.runtime import Runtime
from langchain_core.runnables import RunnableConfig
from typing import Any

# Middleware for trimming memory

MAX_MESSAGES = 3

@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:

    messages = state["messages"]

    if len(messages) <= MAX_MESSAGES:
        return None
    
    first_message = messages[0]
    recent_messages = messages[-1 * MAX_MESSAGES:] \
                      if len(messages) % 2 == 0 else messages[-1 * MAX_MESSAGES - 1:]
    new_messages = [first_message] + recent_messages

    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            *new_messages
        ]
    }


model = OllamaLLM(model = "qwen2.5vl:7b")
personality = "You are a helpful AI assistant"

agent = create_agent(model = model, 
                     tools = [], 
                     middleware = [trim_messages],
                     checkpointer=InMemorySaver(),
                     system_prompt = personality)

config = {"configurable": {"thread_id": str(uuid7())}}

while True:

    user_input = str(input(">>> "))

    result = agent.invoke(
        {"messages": [{"role": "user",
                      "content": user_input}]}, config = config,)
    
    print(result["messages"][-1].content)
    

  