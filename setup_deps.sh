#!/bin/bash

# 1. Create python virtual environment
# 2. Activate it
# 3. Install/upgrade pip in new environment
# 4. Install deps in new environment

# To actually enter new environment from powershell:
#               >>> ./agent_env/Scripts/activate

python -m venv agent_env && \
source agent_env/Scripts/activate && \
python -m pip install --upgrade pip && \
pip install langchain langchain-ollama langchain-chroma pandas