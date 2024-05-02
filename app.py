from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

class PasswordGenerator:
    def generate_password(self, length, include_uppercase, include_lowercase, include_numbers, include_symbols):
        if not (8 <= length <= 50):
            return None, "Password length should be between 8 and 50 characters."

        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            return None, "Please select at least one character type."

        password = ''.join(random.choice(characters) for _ in range(length))
        return password, None

password_generator = PasswordGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['POST'])
def generate_password():
    data = request.get_json()
    length = int(data['length'])
    include_uppercase = data['uppercase']
    include_lowercase = data['lowercase']
    include_numbers = data['numbers']
    include_symbols = data['symbols']

    password, error = password_generator.generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
