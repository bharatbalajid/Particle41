import json
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get_visitor_info():
    visitor_info = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr
    }
    return json.dumps(visitor_info), 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)