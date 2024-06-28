from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

def modinv(a, m):
    gcd, x, _ = egcd(a, m)
    if gcd == 1:
        return x % m
    return None  # No modular inverse if a and m are not coprime

def affine_encrypt(text, a, b):
    if modinv(a, 26) is None:
        raise ValueError("Error: 'a' must be coprime with 26.")
    encrypted_text = ''
    for char in text.upper():
        if char.isalpha():  # Only process alphabetic characters
            encrypted_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
    return encrypted_text


def affine_decrypt(ciphertext, a, b):
    a_inv = modinv(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse does not exist because 'a' and 26 are not coprime.")
    decrypted_text = ''
    for char in ciphertext.upper():
        if char.isalpha():  # Only process alphabetic characters
            decrypted_text += chr(((a_inv * ((ord(char) - ord('A')) - b)) % 26) + ord('A'))
    return decrypted_text


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        text = request.form['text']
        a = int(request.form['a'])
        b = int(request.form['b'])
        action = request.form['action']

        try:
            if action == 'Encrypt':
                message = affine_encrypt(text, a, b)
            elif action == 'Decrypt':
                message = affine_decrypt(text, a, b)
        except Exception as e:
            message = str(e)

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)





