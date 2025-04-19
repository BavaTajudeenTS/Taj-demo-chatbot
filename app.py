from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'your_openai_api_key'

@app.route('/generate_policy', methods=['POST'])
def generate_policy():
    data = request.json
    user_input = data.get('input')
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate an Azure Firewall policy for {user_input}",
        max_tokens=150
    )
    
    policy = response.choices[0].text.strip()
    return jsonify({"policy": policy})

if __name__ == '__main__':
    app.run(debug=True)



