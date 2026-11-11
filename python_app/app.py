from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('<h1>Hello from Flask! 🚀</h1>')

if __name__ == '__main__':
    # Use the PORT environment variable if provided (e.g., for Heroku/Railway)
    import os
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
