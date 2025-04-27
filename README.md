# Stable Diffusion Prompter

> AI-enhanced prompt generator for beautiful Stable Diffusion images.  
> Powered by Streamlit • Ollama (Gemma3) • PraisonAI Agents

---

## 📸 Video




---

## ✨ What It Does

- Enter a **simple idea**( with image for more clear reference) (e.g., "dragon flying over mountains").
- Let **local AI agents** understand and **enhance** your idea into a **perfect Stable Diffusion prompt**.
- Copy and paste the result into **Stable Diffusion** or any AI image generator to get better art.
- Optionally, **upload an image** to inspire future models (feature ready for expansion).

---

## 🦰 How It Works

1. **Input Prompt** ➞  
   The user provides an initial idea through a text box and can also upload images to give a better visual reference of what they are imagining

2. **AI Agents (PraisonAI + Gemma3)** ➞  
   Local agents analyze, expand, and beautify the idea into a detailed prompt.

3. **Stable Diffusion Focused Output** ➞  
   Returns a ready-to-use enhanced prompt optimized for AI image generation.

4. **Technologies Involved**:
   - `Streamlit` (App Frontend)
   - `Ollama` (Running Gemma 3 model locally)
   - `PraisonAI` (Handling AI agent flows)
   - `Stable Diffusion prompt design` (Creative writing)

---

## 🛠️ Tech Stack

| Technology         | Role                       |
|--------------------|-----------------------------|
| Streamlit          | Web App Frontend            |
| Ollama + Gemma3    | Local LLM Inference         |
| PraisonAI          | Agent System for Prompting  |
| Python             | Core Development            |

---

## 🏗️ Project Structure

```
/stable-diffusion-prompter
🔝
├── app.py                 # Streamlit app frontend
├── agents.py              # AI agents setup using PraisonAI (backend)
├── interface.py           # Frontend
├── install.sh             # Install Packages
├── launch.sh              # Launch
├── requirements.txt       # Python dependencies
```

---

## 🚀 General Installation

1. **Clone the Repository**  
```bash
git clone https://github.com/your-username/stable-diffusion-prompter.git
cd stable-diffusion-prompter
```

2. **Install Python Packages**  
```bash
pip install -r requirements.txt
```

3. **Make Sure Ollama is Running Locally**  
- Download [Ollama](https://ollama.ai/) and run the **Gemma 3** model locally.
```bash
ollama pull gemma3
```

4. **Run the Streamlit App**  
```bash
streamlit run interface.py
```
---
## 🚀 Linux Installation

1. **Clone the Repository**  
```bash
git clone https://github.com/your-username/stable-diffusion-prompter.git
cd stable-diffusion-prompter
```

2. **Install Python Packages**  
```bash
bash install.sh ; bash launch.sh
```

3. **Make Sure Ollama is Running Locally**  
- Download [Ollama](https://ollama.ai/) and run the **Gemma 3** model locally.
```bash
ollama pull gemma3
```
---

## 📜 Requirements

- Python 3.11
- Streamlit
- PraisonAI
- Ollama (with Gemma 3 model installed)
- (Optional) Stable Diffusion installed locally to test outputs

---

## 🎯 Future Improvements

- Integrate direct **Stable Diffusion image generation**.
- Add **style presets** (e.g., "anime", "cyberpunk", "realistic").
- Enhance **image upload** influence over generated prompts.
- Mobile responsiveness.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify!

---

# 🚀 Quick Preview

Here’s how simple it is:
1. Enter an idea 💡
2. Get a creative Stable Diffusion prompt ✨
3. Make amazing AI art 🎨

---

# 🎬 Screenshot 
![Screenshot 2025-04-27 173711](https://github.com/user-attachments/assets/579734dc-0b57-4b38-9ffe-f576f4c27b22)

![Screenshot 2025-04-27 173725](https://github.com/user-attachments/assets/23b2c5c7-9f16-4041-9a95-7af6d1f8762b)

![Screenshot 2025-04-27 173740](https://github.com/user-attachments/assets/19523f70-9196-464c-979d-af94ed37da46)




---

# 🛠️ Made With ❤️ By [Shikhar]

