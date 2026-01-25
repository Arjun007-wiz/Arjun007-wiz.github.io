from flask import Flask, render_template, request, jsonify, stream_with_context, Response
import ollama
import json

app = Flask(__name__)

# Configure Ollama settings
OLLAMA_MODEL = "llama2"  # You can change this to other models like "mistral", "codellama", etc.

@app.route('/')
def home():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages and get responses from Ollama"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get conversation history if provided
        conversation_history = data.get('history', [])
        
        # Prepare messages for Ollama
        messages = conversation_history + [{'role': 'user', 'content': user_message}]
        
        # Get response from Ollama
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=messages
        )
        
        bot_response = response['message']['content']
        
        return jsonify({
            'response': bot_response,
            'success': True
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    """Handle streaming chat responses from Ollama"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        conversation_history = data.get('history', [])
        messages = conversation_history + [{'role': 'user', 'content': user_message}]
        
        def generate():
            """Generator function for streaming responses"""
            try:
                stream = ollama.chat(
                    model=OLLAMA_MODEL,
                    messages=messages,
                    stream=True
                )
                
                for chunk in stream:
                    if 'message' in chunk and 'content' in chunk['message']:
                        content = chunk['message']['content']
                        yield f"data: {json.dumps({'content': content})}\n\n"
                
                yield f"data: {json.dumps({'done': True})}\n\n"
            
            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"
        
        return Response(
            stream_with_context(generate()),
            mimetype='text/event-stream',
            headers={
                'Cache-Control': 'no-cache',
                'X-Accel-Buffering': 'no'
            }
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/models', methods=['GET'])
def get_models():
    """Get list of available Ollama models"""
    try:
        models = ollama.list()
        return jsonify({
            'models': [model['name'] for model in models.get('models', [])],
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if Ollama is running and accessible"""
    try:
        ollama.list()
        return jsonify({
            'status': 'healthy',
            'ollama_running': True
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'ollama_running': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
