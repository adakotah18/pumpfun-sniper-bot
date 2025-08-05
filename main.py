from flask import Flask, jsonify, request
from flask_cors import CORS  # This allows your frontend to communicate with the backend

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for communication with the React frontend

# Example portfolio data
portfolio = {
    "balance": 117,
    "value": 10000,
    "pnL": 500
}

# Example trade logs
trade_logs = [
    {"time": "2023-08-01", "type": "BUY", "price": 50, "status": "Completed"},
    {"time": "2023-08-02", "type": "SELL", "price": 60, "status": "Completed"}
]

# Route to get portfolio data
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify(portfolio)

# Route to get trade logs
@app.route('/api/trade-logs', methods=['GET'])
def get_trade_logs():
    return jsonify(trade_logs)

# Route to toggle bot control (if needed)
@app.route('/api/bot-control', methods=['POST'])
def control_bot():
    data = request.get_json()
    if data.get('running') is not None:
        # You can integrate logic to start/stop the bot here
        return jsonify({"status": "Bot toggled", "running": data['running']})
    return jsonify({"status": "Invalid request"}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # This will start the server on http://localhost:5000
