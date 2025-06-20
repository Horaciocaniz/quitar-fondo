from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    file = request.files['image']
    input_bytes = file.read()
    output_bytes = remove(input_bytes)

    return send_file(
        io.BytesIO(output_bytes),
        mimetype='image/png',
        download_name='sin_fondo.png'
    )

if __name__ == '__main__':
    app.run()
