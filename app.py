from flask import Flask, request, send_file
from rembg import remove
import io
import os

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    # Verificamos que se haya enviado una imagen
    if 'image' not in request.files:
        print("[ERROR] No se recibió ninguna imagen.")
        return 'No image uploaded', 400

    file = request.files['image']
    input_bytes = file.read()

    try:
        # Intentar remover el fondo con rembg
        output_bytes = remove(input_bytes)
    except Exception as e:
        # Si hay error, mostrar en logs y devolver mensaje
        print(f"[ERROR] Fallo al procesar la imagen: {e}")
        return f"❌ Error interno al procesar la imagen: {str(e)}", 500

    # Si todo salió bien, devolver la imagen sin fondo
    return send_file(
        io.BytesIO(output_bytes),
        mimetype='image/png',
        download_name='sin_fondo.png'
    )

# Esta línea es clave para que funcione en Railway:
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

