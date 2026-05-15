from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_KEYS = ["OMNI-77B", "OMNI-X22"] # Add your keys here

@app.route('/process', methods=['POST'])
def process_command():
    data = request.json
    cmd = data.get('command', '').lower()
    user_key = data.get('key', '')

    if user_key not in VALID_KEYS:
        return jsonify({"reply": "Access Denied. Invalid License.", "action": "none"})

    if any(x in cmd for x in ["cap", "money", "chip", "currency", "cola"]):
        return jsonify({
            "reply": "Bypassing account verification and injecting currency. Transaction complete.",
            "action": "inject_money"
        })
    elif "launch" in cmd:
        return jsonify({
            "reply": "Initializing game launch sequence.",
            "action": "launch_game"
        })
    
    return jsonify({"reply": "Command received.", "action": "custom"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
