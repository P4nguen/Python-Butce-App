from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'transactions.json'

def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_transactions(transactions):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(transactions, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = load_transactions()
    return jsonify(transactions)

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transactions = load_transactions()
    
    new_transaction = {
        'id': max([t['id'] for t in transactions], default=0) + 1 if transactions else 1,
        'type': data['type'],
        'amount': float(data['amount']),
        'category': data['category'],
        'description': data['description'],
        'date': data['date'],
        'timestamp': datetime.now().isoformat()
    }
    
    transactions.insert(0, new_transaction)
    save_transactions(transactions)
    
    return jsonify(new_transaction), 201

@app.route('/api/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    transactions = load_transactions()
    transactions = [t for t in transactions if t['id'] != id]
    save_transactions(transactions)
    return jsonify({'success': True})

@app.route('/api/transactions/<int:id>', methods=['PUT'])
def update_transaction(id):
    data = request.json
    transactions = load_transactions()
    
    for i, t in enumerate(transactions):
        if t['id'] == id:
            transactions[i] = {
                'id': id,
                'type': data['type'],
                'amount': float(data['amount']),
                'category': data['category'],
                'description': data['description'],
                'date': data['date'],
                'timestamp': t.get('timestamp', datetime.now().isoformat())
            }
            break
    
    save_transactions(transactions)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)