from flask import Flask, request
app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    prompt = data.get('prompt', 'No Payload from C Sharp')
    # prmpot will contain what user says
      # EXAMPLE: prompt = "bring me to world war 2"
    
    enhanced_prompt = f"{prompt} but in more detail"

    return f'Hello People, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
