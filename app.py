from flask import Flask, render_template, request, jsonify, stream_with_context, Response
import ollama
import json

app = Flask(__name__)

# Configure Ollama settings
OLLAMA_MODEL = "llama2"  # You can change this to other models like "mistral", "codellama", etc.

# System prompt for concise responses
SYSTEM_PROMPT = """You are a helpful AI assistant. Keep your responses very brief and concise.
Answer in 2-3 lines maximum. Be direct and to the point. Avoid lengthy explanations and examples.
Focus on the core answer the user is looking for."""

# Quiz Configuration
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the main purpose of this website?",
        "options": ["To sell chainsaws", "To let people know about me", "To play games", "To learn Python"],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which page tells you about my background?",
        "options": ["Home", "Quiz", "About Me", "Contact"],
        "correct": 2
    },
    {
        "id": 3,
        "question": "What happens if you win the quiz?",
        "options": ["Nothing", "You get a prize", "You get banned", "You lose points"],
        "correct": 1
    }
]

@app.route('/')
def home():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/quiz')
def quiz():
    """Render the quiz page"""
    return render_template('quiz.html')

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    """Get quiz questions"""
    return jsonify({
        'questions': [{
            'id': q['id'],
            'question': q['question'],
            'options': q['options']
        } for q in QUIZ_QUESTIONS]
    })

@app.route('/api/quiz/check', methods=['POST'])
def check_quiz():
    """Check quiz answers"""
    try:
        data = request.json
        answers = data.get('answers', {})
        score = 0
        
        for q in QUIZ_QUESTIONS:
            qid = str(q['id'])
            if qid in answers and answers[qid] == q['correct']:
                score += 1
        
        return jsonify({
            'score': score,
            'total': len(QUIZ_QUESTIONS),
            'prize': "🎉 You won a prize! 🎉" if score == len(QUIZ_QUESTIONS) else None
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        
        # Add system prompt if this is the start of conversation
        if not conversation_history:
            messages = [{'role': 'system', 'content': SYSTEM_PROMPT}]
        else:
            messages = []
        
        # Prepare messages for Ollama
        messages = messages + conversation_history + [{'role': 'user', 'content': user_message}]
        
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
        
        # Add system prompt if this is the start of conversation
        if not conversation_history:
            messages = [{'role': 'system', 'content': SYSTEM_PROMPT}]
        else:
            messages = []
        
        messages = messages + conversation_history + [{'role': 'user', 'content': user_message}]
        
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
