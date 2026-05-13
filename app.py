from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Приветствие</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        #greet { margin-top: 20px; font-size: 1.2em; color: #2a7; }
        button { padding: 10px 20px; font-size: 1em; cursor: pointer; }
    </style>
</head>
<body>
    <button onclick="showPrompt()">Ввести имя</button>
    <div id="greet"></div>
    <script>
        function showPrompt() {
            let name = prompt('Введите ваше имя:');
            if (name) {
                fetch('/greet', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: name })
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('greet').textContent = data.greeting;
                });
            }
        }
    </script>
</body>
</html>
''')

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', '').strip()
    if not name:
        greeting = 'Пожалуйста, введите имя.'
    else:
        greeting = f'Привет, {name}!'
    return jsonify({'greeting': greeting})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)