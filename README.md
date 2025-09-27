# 🤖 AI Voice Chatbot (Offline & Private)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)

A privacy-centric, voice-enabled AI chatbot built with Python. It uses a local LLM (Ollama), local voice recognition (Vosk), and a local database (MySQL) to function 100% offline, ensuring no user data ever leaves the machine.

![Screenshot of Chatbot GUI]()
<img width="935" height="753" alt="image" src="https://github.com/user-attachments/assets/a6e65c6a-e7fe-4feb-bc6f-aa2e316fb3cf" />


---

### ✨ Key Features

-   **🗣️ Voice Recognition:** Speak your queries directly to the chatbot using real-time, offline voice-to-text conversion.
-   **🧠 Local AI Model:** Powered by Ollama and the `phi3:latest` model, allowing it to generate intelligent responses without an internet connection.
-   **💾 Persistent Memory:** Conversations are saved to a local MySQL database, so you can load and revisit your chat history at any time.
-   ** intuitive GUI:** A clean and user-friendly graphical interface built with Python's native Tkinter library.

---

### 🛠️ Tech Stack

-   **Backend:** Python
-   **GUI:** Tkinter
-   **AI Model:** Ollama (`phi3:latest`)
-   **Voice Recognition:** Vosk & PyAudio
-   **Database:** MySQL

---

### ⚙️ Setup & Installation

To run this project locally, follow these steps:

1.  **Clone the Repository:**
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install Dependencies:**
    Make sure you have Python 3 installed. Then, open your terminal in the project folder and run:
    ```sh
    pip install -r requirements.txt
    ```

3.  **Set up the Database:**
    -   Ensure you have a local MySQL server (like XAMPP or WAMP) running.
    -   The Python script will automatically create the `project_db` database and the `history` table on its first run.

4.  **Download Required Models:**
    -   **Ollama:** Install Ollama from the [official website](https://ollama.com/) and then pull the required model by running this command in your terminal: `ollama pull phi3`
    -   **Vosk:** Download the small English model (`vosk-model-small-en-us-0.15`) from the [Vosk Models Page](https://alphacephei.com/vosk/models). Unzip the folder and place it in your project directory or update the `MODEL_PATH` in the script to its location.

5.  **Run the Application:**
    Execute the main Python script from your terminal:
    ```sh
    python your_script_name.py
    ```

---

### 🤝 Our Team & Contributions

This project was a collaborative effort. As the project lead, I managed the integration of all modules and developed the core AI logic.

-   **Bappi Singh (Project Lead & AI Developer):**
    -   Integrated the Ollama `phi3:latest` model for core response generation.
    -   Architected the overall application logic and workflow.
    -   Managed team coordination and final module integration.

-   **Omraj Singh (GUI & Integration Specialist):**
    -   Designed and built the complete user interface using Tkinter.
    -   Connected the GUI with the backend, voice, and database modules.

-   **Ayush Singh (Voice Recognition & Audio Stream Engineer):**
    -   Implemented the voice input functionality using Vosk and PyAudio.
    -   Configured the real-time microphone stream for accurate speech-to-text.

-   **Satyam Yadav (Database & Memory Manager):**
    -   Set up the MySQL database schema for storing chat history.
    -   Wrote the functions for saving and retrieving conversations.
