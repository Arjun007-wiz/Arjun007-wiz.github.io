# 🐵 Arjun's Chatbot

A modern, professional AI-powered chatbot web application built with **Ollama**, **Flask**, and **Python**. Features a sleek dark-themed interface with real-time streaming responses and an adorable monkey assistant.

## ✨ Features

- 🤖 **AI-Powered Conversations** - Powered by Ollama's local LLM models
- 💬 **Real-Time Streaming** - Watch responses stream in real-time as they're generated
- 🎨 **Professional Dark Theme** - Modern UI with blue gradient background and glassmorphism effects
- 📝 **Conversation Memory** - Maintains conversation history for context-aware responses
- ⚡ **Fast & Lightweight** - Runs locally on your machine
- 🦆 **Animated Background** - Fun walking ducks animation
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🔄 **Dual Mode** - Toggle between streaming and standard response modes

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Ollama** ([Download here](https://ollama.ai))
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/redesigned-chainsaw.git
   cd redesigned-chainsaw
   ```

2. **Install Ollama and pull a model**
   ```bash
   ollama pull llama2
   # Or try other models: mistral, neural-chat, codellama
   ```

3. **Create a Python environment (optional but recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the Flask server**
   ```bash
   python app.py
   ```

6. **Open in your browser**
   ```
   http://localhost:5000
   ```

## 📖 Usage

1. **Type a message** in the input box at the bottom
2. **Press Enter** or click the send button
3. **Toggle "Stream responses"** to enable/disable real-time streaming
4. **Click "Clear Chat"** to start a new conversation

### Example Queries
- "What is machine learning?"
- "How do I learn Python?"
- "Tell me a joke"
- "Explain quantum computing briefly"

## 🏗️ Project Structure

```
redesigned-chainsaw/
├── app.py                    # Flask backend & Ollama integration
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── templates/
│   └── index.html           # Main chat interface (HTML)
└── static/
    ├── style.css            # Professional styling (CSS)
    ├── script.js            # Frontend logic (JavaScript)
    └── ...
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main chat interface |
| POST | `/api/chat` | Get non-streaming response |
| POST | `/api/chat/stream` | Get streaming response |
| GET | `/api/models` | List available Ollama models |
| GET | `/api/health` | Check Ollama connection status |

## ⚙️ Configuration

### Change the AI Model

Edit `app.py`:
```python
OLLAMA_MODEL = "mistral"  # Change from "llama2" to any available model
```

Available models: https://ollama.ai/library

### Customize the System Prompt

Modify the `SYSTEM_PROMPT` in `app.py` to change AI behavior:
```python
SYSTEM_PROMPT = "Your custom instructions here..."
```

### Change Server Port

In `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Changed from 5000
```

## 🌐 Deployment Options

### Local Network Access
Access from any device on your network:
```
http://<YOUR_COMPUTER_IP>:5000
```

Get your IP: `ipconfig` (Windows) or `ifconfig` (macOS/Linux)

### Deploy Online

**Option 1: Replit** (Easiest - Free)
- Go to [replit.com](https://replit.com)
- Import your GitHub repository
- Click "Run" to get a live URL

**Option 2: Railway.app** (Free with credits)
- Connect your GitHub repo
- Auto-deploys on every push

**Option 3: PythonAnywhere** (Free tier)
- Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
- Upload files and configure

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Ollama connection error** | Make sure Ollama is running: `ollama serve` |
| **Model not found** | Install model: `ollama pull llama2` |
| **Port already in use** | Change port in `app.py` to 5001, 8000, etc. |
| **Slow responses** | Check CPU/RAM usage; try a smaller model |
| **Import errors** | Reinstall dependencies: `pip install -r requirements.txt --force-reinstall` |

## 🎨 Customization

### Change Color Theme
Edit `:root` variables in `static/style.css`:
```css
--primary-color: #3b82f6;      /* Main blue */
--primary-hover: #2563eb;      /* Darker blue */
--background: #0a0e1a;         /* Dark background */
```

### Modify AI Avatar
Change emoji in `templates/index.html` and `static/script.js`:
```javascript
avatar.textContent = sender === 'bot' ? '🐵' : '👤';  // 🐵 = monkey
```

### Disable Duck Animation
Comment out the ducks-container in `templates/index.html` or set `z-index: -1` in CSS.

## 📊 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Backend | Flask (Python) | Web server & API |
| AI Model | Ollama | Local LLM inference |
| Frontend | HTML/CSS/JavaScript | User interface |
| Font | Inter (Google Fonts) | Professional typography |

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙋 Support

Having issues? Try:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review Ollama documentation: https://ollama.ai
3. Check Flask documentation: https://flask.palletsprojects.com

## 🎯 Future Enhancements

- [ ] Model selection dropdown in UI
- [ ] Chat history export (JSON/PDF)
- [ ] User preferences/settings panel
- [ ] Multiple conversation threads
- [ ] Voice input/output support
- [ ] Conversation sharing feature
- [ ] Custom system prompts in UI

## 👨‍💻 Author

**Arjun** - [@Arjun007-wiz](https://github.com/Arjun007-wiz)

---

**⭐ If you find this project helpful, please give it a star!**

Made with ❤️ and 🐵
