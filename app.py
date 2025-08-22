from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Hola Mundo</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center;
      background: linear-gradient(-45deg, #667eea, #764ba2, #f6d365, #fda085);
      background-size: 400% 400%;
      animation: gradientBG 15s ease infinite;
      font-family: 'Segoe UI', sans-serif;
      color: white;
      text-align: center;
    }
    @keyframes gradientBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    h1 { font-size: 70px; text-shadow: 0 0 20px #fff, 0 0 30px #fff; animation: bounce 2s infinite; }
    @keyframes bounce {
      0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
      40% { transform: translateY(-30px); }
      60% { transform: translateY(-15px); }
    }
  </style>
</head>
<body>
  <h1>🌍 ¡Hola Mundo!</h1>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
