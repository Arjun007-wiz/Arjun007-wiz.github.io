# AI Chatbot with Ollama, Flask, and Python

A modern AI chatbot web application powered by Ollama, Flask, and a sleek web interface.

## Features

- 🤖 AI-powered conversationsin using Ollama
- 💬 Real-time streaming responses
- 🎨 Modern, responsive UI with dark theme
- 📝 Conversation history management
- ⚡ Fast and lightweight
- 🔄 Toggle between streaming and normal mode

## Prerequisites

Before running this application, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running
   - Download from: https://ollama.ai
   - After installation, pull a model: `ollama pull llama2`

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd redesigned-chainsaw
   ```

2. **Install Python dependencies:**
   ```bash
   
   ```

3. **Verify Ollama is running:**
   ```bash
   ollama list
   ```
   You should see at least one model listed (e.g., llama2)

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

- Type your message in the input box at the bottom
- Press Enter or click the send button to send your message
- Toggle "Stream responses" to enable/disable streaming mode
- Click "Clear Chat" to start a new conversation

## Project Structure

```
redesigned-chainsaw/
├── app.py                 # Flask application and API endpoints
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # HTML template for the chat interface
└── static/
    ├── style.css         # Styling for the chat interface
    └── script.js         # Frontend JavaScript logic
```

## API Endpoints

- `GET /` - Main chat interface
- `POST /api/chat` - Send message and get response (non-streaming)
- `POST /api/chat/stream` - Send message and get streaming response
- `GET /api/models` - List available Ollama models
- `GET /api/health` - Check if Ollama is running

## Configuration

You can change the AI model in `app.py`:

```python
OLLAMA_MODEL = "llama2"  # Change to "mistral", "codellama", etc.
```

Available models can be found at: https://ollama.ai/library

## Troubleshooting

**Ollama not connecting:**
- Ensure Ollama is running: `ollama serve`
- Check if models are installed: `ollama list`

**Port already in use:**
- Change the port in `app.py`: `app.run(debug=True, port=5001)`

**Dependencies issues:**
- Upgrade pip: `pip install --upgrade pip`
- Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## License

MIT License - feel free to use this project for your own purposes.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
