# Personal_Agent
Multimodal AI agent that will hopefully be used in embedded systems

# Helpful Sources:
- Tech With Tim: How to set up basic local agent:
    https://www.youtube.com/watch?v=E4l91XKQSgw

- Tech With TIme: Taking agent one step further and connecting it to external services (adding in tools, specifically with MCP):
    https://www.youtube.com/watch?v=GAyNvq6Ayps

    - Tiny Huang: Actually explaining what the heck MCP is
        https://www.youtube.com/watch?v=kOhLoixrJXo

    - NOTE: looking more into it, MCPs might be overkill;
            might just be able to get away with using basic API calls...
            (also, MCP servers don't work at for local devices, so...)

        - only problem: have to set up in such a way that LLM still understands it... (check out first video for that, I think)

# NOTES: 
    - will likely have to switch to a VLM so that this thing can process images...
        - check out what ollama has in terms of "thinking" models: https://docs.ollama.com/capabilities/thinking

    - look at these refs:

        - can this just be used to do the work for me???: https://docs.langchain.com/oss/javascript/langchain/agents

        - for passing messages (go back and read this, might be helpful): https://docs.langchain.com/oss/javascript/langchain/messages
        - for short-term memory (go back and re-implement using library): https://docs.langchain.com/oss/javascript/langchain/short-term-memory
        - for tools: https://docs.langchain.com/oss/javascript/langchain/tools