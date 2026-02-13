// Initialize on page load

document.addEventListener('DOMContentLoaded', () => {
    setupNavigation();
    setupSmoothScroll();
    setupButtonRipple();
});

// Navigation setup

function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            // Only animate for hash links
            if (link.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    // Animate scroll
                    targetSection.scrollIntoView({ behavior: 'smooth' });
                    // Animate nav link (ripple effect)
                    createRipple(link, e);
                }
            }
        });
    });
}

// Smooth scroll behavior

function setupSmoothScroll() {
    document.documentElement.style.scrollBehavior = 'smooth';
}

// Button ripple animation
function setupButtonRipple() {
    const buttons = document.querySelectorAll('.btn, .nav-link');
    buttons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            createRipple(this, e);
        });
    });
}

function createRipple(element, event) {
    // Remove any old ripple
    const oldRipple = element.querySelector('.ripple');
    if (oldRipple) oldRipple.remove();
    // Create new ripple
    const ripple = document.createElement('span');
    ripple.className = 'ripple';
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = (event.clientX - rect.left - size / 2) + 'px';
    ripple.style.top = (event.clientY - rect.top - size / 2) + 'px';
    element.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
}
}

// Update connection status
function updateStatus(status, text) {
    statusIndicator.className = `status-indicator ${status}`;
    statusText.textContent = text;
}

// Auto-resize textarea
function adjustTextareaHeight() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 120) + 'px';
}

// Send message
async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message) return;
    
    // Disable input while processing
    setInputState(false);
    
    // Add user message to chat
    addMessage(message, 'user');
    
    // Add to conversation history
    conversationHistory.push({
        role: 'user',
        content: message
    });
    
    // Clear input
    userInput.value = '';
    adjustTextareaHeight();
    
    // Show typing indicator
    const typingIndicator = addTypingIndicator();
    
    // Check if streaming is enabled
    if (streamToggle.checked) {
        await sendStreamingMessage(message, typingIndicator);
    } else {
        await sendNormalMessage(message, typingIndicator);
    }
    
    // Re-enable input
    setInputState(true);
    userInput.focus();
}

// Send normal (non-streaming) message
async function sendNormalMessage(message, typingIndicator) {
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                history: conversationHistory.slice(0, -1) // Exclude the current message
            })
        });
        
        const data = await response.json();
        
        // Remove typing indicator
        typingIndicator.remove();
        
        if (data.success) {
            addMessage(data.response, 'bot');
            conversationHistory.push({
                role: 'assistant',
                content: data.response
            });
        } else {
            addMessage('Sorry, I encountered an error: ' + data.error, 'bot');
        }
    } catch (error) {
        typingIndicator.remove();
        addMessage('Sorry, I encountered an error connecting to the server.', 'bot');
        console.error('Error:', error);
    }
}

// Send streaming message
async function sendStreamingMessage(message, typingIndicator) {
    try {
        const response = await fetch('/api/chat/stream', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                history: conversationHistory.slice(0, -1)
            })
        });
        
        // Remove typing indicator
        typingIndicator.remove();
        
        // Create message element for streaming response
        const messageElement = addMessage('', 'bot');
        const contentElement = messageElement.querySelector('.message-content p');
        
        let fullResponse = '';
        
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        
        while (true) {
            const { done, value } = await reader.read();
            
            if (done) break;
            
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');
            
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    try {
                        const data = JSON.parse(line.slice(6));
                        
                        if (data.content) {
                            fullResponse += data.content;
                            contentElement.textContent = fullResponse;
                            scrollToBottom();
                        }
                        
                        if (data.error) {
                            contentElement.textContent = 'Error: ' + data.error;
                        }
                    } catch (e) {
                        console.error('Error parsing stream data:', e);
                    }
                }
            }
        }
        
        // Add to conversation history
        conversationHistory.push({
            role: 'assistant',
            content: fullResponse
        });
        
    } catch (error) {
        typingIndicator.remove();
        addMessage('Sorry, I encountered an error with streaming.', 'bot');
        console.error('Streaming error:', error);
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const avatar = document.createElement('div');
    avatar.className = `message-avatar ${sender}-avatar`;
    avatar.textContent = sender === 'bot' ? '🐵' : '👤';
    
    const content = document.createElement('div');
    content.className = 'message-content';
    
    const paragraph = document.createElement('p');
    paragraph.textContent = text;
    
    content.appendChild(paragraph);
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
    
    return messageDiv;
}

// Add typing indicator
function addTypingIndicator() {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    messageDiv.id = 'typing-indicator';
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar bot-avatar';
    avatar.textContent = '🤖';
    
    const content = document.createElement('div');
    content.className = 'message-content';
    
    const typingDiv = document.createElement('div');
    typingDiv.className = 'typing-indicator';
    typingDiv.innerHTML = '<span></span><span></span><span></span>';
    
    content.appendChild(typingDiv);
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
    
    return messageDiv;
}

// Clear chat
function clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
        // Keep only the first welcome message
        const messages = chatMessages.querySelectorAll('.message');
        messages.forEach((msg, index) => {
            if (index > 0) {
                msg.remove();
            }
        });
        
        // Clear conversation history
        conversationHistory = [];
    }
}

// Enable/disable input
function setInputState(enabled) {
    userInput.disabled = !enabled;
    sendButton.disabled = !enabled;
}

// Scroll to bottom of chat
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
