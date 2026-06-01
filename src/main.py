from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from collections import deque

import globals
import mem_manager as mm

model = OllamaLLM(model="llama3.2")

# Read in default personality:

personality = ""

with open(globals.default_personality_path) as file:
    personality += file.read()

# Prompt loop:
dialogue_record = deque([], maxlen = globals.dialogue_quota)

while(True):

    curr_input = input(">>> ")

    if (curr_input == "q"): break

    else:
        
        past_info = ""
        
        for user_input, agent_output in dialogue_record:
            past_info += "Me:\n" + user_input + "\n" + "You:\n" + agent_output + "\n"

        # template = "" + past_info + personality + "\n" + user_input

        template = """
            Here is your personality: {personality}
            Here is our past conversation: {past_info}
            Here is what I'm saying to you right now: {curr_input}
        """

        # print("\n",template,"\n")

        prompt = ChatPromptTemplate.from_template(template)

        chain = prompt | model 
        result = chain.invoke({"past_info": past_info, "personality": personality, "curr_input": curr_input})
        print(result)

        # Save last exchange:
        dialogue_record.append((curr_input, result))
        
        # print("\n", dialogue_record, "\n")
