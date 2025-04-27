import streamlit as st
import subprocess
import os
import tempfile

# --- Page Config ---
st.set_page_config(page_title="Stable Diffusion Prompter", page_icon="🤖", layout="wide")

# --- Sidebar Config ---
st.sidebar.title("⚙️ Settings")
uploaded_image = st.sidebar.file_uploader("🖼️ Upload Image (optional)", type=["jpg", "png", "jpeg"])

# --- Manual Clear Trigger ---
if "clear_trigger" not in st.session_state:
    st.session_state.clear_trigger = False

# --- Reset Everything on Clear ---
if st.sidebar.button("🧹 Clear Chat"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.clear_trigger = True
    st.rerun()

# --- Session Setup ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Title ---
st.title("🎨 Stable Diffusion Prompter")

# --- Chat Input ---
prompt = st.chat_input("Ask anything about your creative idea or image...")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Handle image
    if uploaded_image:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_image.read())
            image_path = tmp.name
    else:
        image_path = None

    # Prepare arguments for the backend script
    args = ["python3", "agents.py", prompt]
    if image_path:
        args.append(image_path)

    # Run the agent script with real-time output in the terminal
    with st.spinner("🤖 Thinking..."):
        try:
            process = subprocess.Popen(
                args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            # Capture and display the output in the terminal (stdout)
            for line in process.stdout:
                print(line.strip())  # Print to terminal for real-time tracking

            # Capture and display errors in the terminal (stderr)
            for line in process.stderr:
                print(f"ERROR: {line.strip()}")  # Print errors to terminal

            # Wait for the process to complete
            process.wait()

            # Read final_response.md
            final_reply = "⚠️ No final output found."
            if os.path.exists("./results/final_response.md"):
                with open("./results/final_response.md", "r", encoding="utf-8") as f:
                    final_reply = f.read()

            # Read prompts.md
            prompts_reply = ""
            if os.path.exists("./prompts/prompts.md"):
                with open("./prompts/prompts.md", "r", encoding="utf-8") as f:
                    prompts_reply = f.read()

        except Exception as e:
            final_reply = f"❌ Error occurred: {e}"
            prompts_reply = ""

        # Append both to chat history
        st.session_state["messages"].append({"role": "assistant", "content": final_reply})
        if prompts_reply:
            st.session_state["messages"].append({"role": "assistant", "content": f"### 📄 Generated Prompts:\n{prompts_reply}"})

        # Save for download button context
        st.session_state["final_reply_data"] = final_reply
        st.session_state["prompts_data"] = prompts_reply

# --- Display Chat History with download buttons right after content ---
for i, msg in enumerate(st.session_state["messages"]):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        # Show download buttons right after their respective messages
        if msg["content"] == st.session_state.get("final_reply_data"):
            st.download_button(
                "📥 Download Final Response",
                st.session_state["final_reply_data"],
                file_name="final_response.md",
                mime="text/markdown",
                key=f"download_final_{i}"  # Unique key
            )

        if msg["content"].startswith("### 📄 Generated Prompts:"):
            st.download_button(
                "📥 Download Prompts",
                st.session_state["prompts_data"],
                file_name="prompts.md",
                mime="text/markdown",
                key=f"download_prompts_{i}"  # Unique key
            )
