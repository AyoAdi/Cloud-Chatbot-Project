from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

# Ensure the tokenizer has a pad token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query_input = data.get('query')

    if query_input:
        solution = get_ai_response(query_input)
        return jsonify({"response": solution})
    else:
        return jsonify({"response": "Please provide the issue description."})

def get_ai_response(query):
    # Prompt setup
    prompt = f"Provide a troubleshooting step for the following Wi-Fi issue: {query}"
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

    try:
        # Generate response with controlled parameters
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_length=150,
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.pad_token_id,
            top_k=50,
            top_p=0.95,
            no_repeat_ngram_size=2,
            num_return_sequences=1
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Remove the prompt part from the response
        if response.startswith(prompt):
            response = response[len(prompt):].strip()
        
        # Format for HTML output
        response = response.replace("\n", "<br>")
        return response.strip()

    except Exception as e:
        print(f"Error in generating AI response: {e}")
        return "Sorry, something went wrong."

if __name__ == '__main__':
    app.run(debug=True)
