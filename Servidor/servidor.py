from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
fps_atual = 0  # Armazena o FPS mais recente

# Página HTML com atualização automática
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Monitor de FPS</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #121212; color: #00ffcc; }
        h1 { font-size: 4em; }
    </style>
</head>
<body>
    <h1>FPS Atual: <span id="fps">--</span></h1>
    <script>
        function atualizarFPS() {
            fetch('/fps').then(res => res.json()).then(data => {
                document.getElementById('fps').innerText = data.fps;
            });
        }
        setInterval(atualizarFPS, 1000); // Atualiza a cada 1 segundo
        atualizarFPS(); // Primeira chamada
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/fps', methods=['POST'])
def receber_fps():
    global fps_atual
    dados = request.get_json()
    if 'fps' in dados:
        fps_atual = dados['fps']
        print(f"[✔] FPS recebido: {fps_atual}")
        return jsonify({"status": "FPS recebido"}), 200
    return jsonify({"erro": "FPS não enviado"}), 400

@app.route('/fps', methods=['GET'])
def enviar_fps():
    return jsonify({"fps": fps_atual})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
