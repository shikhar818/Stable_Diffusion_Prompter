### Libraries Used, You can use this as requirements.txt if the requirements.txt gets outdated.

streamlit
ollama
langchain_ollama
praisonai
praisonaiagents[llm]
praisonaiagents[knowledge]
streamlit-option-menu 
streamlit-extras
### There's Pydantic issue where it says dict() has depreceated, go to streamhandler.py and change .dict() to .model_dump() that should resolve the issue, else you can leave it too. 