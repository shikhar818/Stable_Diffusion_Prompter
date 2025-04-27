# agents.py
import sys
from praisonaiagents import Agent, Task, PraisonAIAgents
import ollama
import shutil
import os

# Get user specification and image path from command-line arguments
specification = sys.argv[1]  # User specification
image_path = sys.argv[2] if len(sys.argv) > 2 else None  # Image path (if provided)

# Models
gemma3 = "ollama/gemma3"  # Ensure correct model name

# Environment Configuration (for Ollama with OpenAI compatibility)
os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"
os.environ["OPENAI_API_KEY"] = "fake-key"

# AI Config
config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "praison",
            "path": ".praison"
        }
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "gemma3",  # Adjust model name if necessary
            "temperature": 0.5,
            "max_tokens": 8000,
            "ollama_base_url": "http://localhost:11434",
        },
    },
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest",
            "ollama_base_url": "http://localhost:11434",
            "embedding_dims": 1536
        },
    },
}

#Delete Database before starting
praison_folder = ".praison"
if os.path.exists(praison_folder) and os.path.isdir(praison_folder):
    shutil.rmtree(praison_folder)

# Define output path
prompt_output_path = "./prompts/prompts.md"

# Agent: Instructor for Prompt Generation
instructor_agent = Agent(
    name="Instructor_Agent",
    role="User Context Understander for Stable Diffusion",
    goal=(f"Understand user specification: {specification}. "
          "Generate a variety of high-quality prompts for Stable Diffusion with a format that can be directly copy and pasted into stable diffusion based on your knowledge."
          "Make sure to include the following parameters required for Stable Diffusion: the prompt, negative prompt, sampling method, sampling steps, CFG scale, and the image dimensions (height and width)"
          "Label each generated prompt clearly (e.g., Prompt 1, Prompt 2, Prompt 3...) to help the user easily review and select their preferred option"),
    knowledge=["./knowledge/tips_for_prompt.pdf"],
    user_id="user1",
    knowledge_config=config,
    llm=gemma3
)

# Task: Generate Prompts
task1 = Task(
    name="Generate Stable Diffusion Prompts",
    description=f"Generate multiple prompt with the following parameters: the prompt, negative prompt, sampling method, sampling steps, CFG scale, and the image dimensions (height and width) options for the given user specification: {specification}.",
    expected_output=f"A variety of prompts based on: {specification}",
    output_file=prompt_output_path,
    agent=instructor_agent,
)

# Run the Task via PraisonAIAgents
print("Running agent task to generate prompts...")
agents = PraisonAIAgents(
    agents=[instructor_agent],
    tasks=[task1],
    process="sequential",
    verbose=1
)

# Run analysis
agents.start()

# Check if prompt output file exists
if not os.path.exists(prompt_output_path):
    print(f"❌ Prompt file not found at {prompt_output_path}")
    exit(1)

# Read prompt content
with open(prompt_output_path, "r", encoding="utf-8") as md_file:
    content = md_file.read()

# Prepare final prompt content
prompt_content = f"""
You are a Stable-Diffusion Prompter. Based on user specification:

>> {specification}

And the following generated prompts:

{content}

Select and refine the best prompts and negative prompts for image generation.
In the end, conclude your answer based on this format of well structured table for user convenience: 
the prompt, negative prompt, sampling method, sampling steps, CFG scale, and the image dimensions (height and width) options.
"""

# Image Path (optional)
if image_path:
    print(f"Image found: {image_path}. Analyzing with image + context...")
    res = ollama.chat(
        model="gemma3",  # Double-check model here
        messages=[{
            'role': 'user',
            'content': prompt_content,
            'images': [image_path]
        }]
    )
else:
    print("No image provided. Proceeding with context only...")
    res = ollama.chat(
        model="gemma3",  # Double-check model here
        messages=[{
            'role': 'user',
            'content': prompt_content
        }]
    )

# Output result
result = res['message']['content']
print("\n✅ Final Output:\n", result)

# Save final output
output_path = "./results/final_response.md"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result)
