from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pixel_id = request.form.get('pixel_id')
        access_token = request.form.get('access_token')
        
        # Your logic here...
        return jsonify({"status": "success", "pixel_id": pixel_id, "access_token": access_token})

    return "Welcome to Flask API on Vercel"

# Vercel requires this handler for serverless function
def handler(request):
    return app(request)
