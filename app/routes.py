from flask import Blueprint, render_template, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib

crypto_bp = Blueprint('crypto', __name__)

def process_key(key):
    """Convert any length key to 32 bytes using SHA-256"""
    return hashlib.sha256(key.encode()).digest()

@crypto_bp.route('/')
def index():
    return render_template('index.html')

@crypto_bp.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        plaintext = data['plaintext']
        key = data['key']
        
        if not plaintext or not key:
            return jsonify({'status': 'error', 'message': 'Plaintext and key are required'})
        
        processed_key = process_key(key)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(processed_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        encrypted_data = iv + ciphertext
        
        return jsonify({
            'status': 'success',
            'ciphertext': base64.b64encode(encrypted_data).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@crypto_bp.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        ciphertext = data['ciphertext']
        key = data['key']
        
        if not ciphertext or not key:
            return jsonify({'status': 'error', 'message': 'Ciphertext and key are required'})
        
        processed_key = process_key(key)
        encrypted_data = base64.b64decode(ciphertext)
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        cipher = AES.new(processed_key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        return jsonify({
            'status': 'success',
            'plaintext': decrypted.decode('utf-8')
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})