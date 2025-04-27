# Libraries Used
### You can use the following list as a reference for requirements.txt in case it becomes outdated:

streamlit

ollama

langchain_ollama

praisonai

praisonaiagents[llm]

praisonaiagents[knowledge]

streamlit-option-menu

streamlit-extras

# Pydantic Deprecation Issue
***There is a known issue with Pydantic where it throws a deprecation warning when calling .dict(). To resolve this, navigate to streamhandler.py and replace .dict() with .model_dump(). Alternatively, you can choose to leave it as is if the warning is not critical for your use case.***
