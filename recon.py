# app.py
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import io
import base64

app = FastAPI()

# Configurar los archivos estáticos y las plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recognize")
async def recognize_face(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    # Convertir la imagen a un array numpy
    image_np = np.array(image)
    
    # Encontrar todas las caras en la imagen
    face_locations = face_recognition.face_locations(image_np)
    
    # Dibujar rectángulos alrededor de las caras
    draw = ImageDraw.Draw(image)
    for (top, right, bottom, left) in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255), width=2)
    
    # Convertir la imagen procesada de vuelta a base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return {
        "num_faces": len(face_locations),
        "processed_image": f"data:image/png;base64,{img_str}"
    }

# Contenido del archivo HTML (guárdalo en la carpeta 'templates' como 'index.html')
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reconocimiento Facial</title>
    <script src="https://unpkg.com/htmx.org@1.9.6"></script>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        img { max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>Reconocimiento Facial</h1>
    <input type="file" name="file" hx-post="/recognize" hx-target="#result" hx-encoding="multipart/form-data">
    <div id="result"></div>

    <script>
        document.body.addEventListener('htmx:afterSwap', function(event) {
            var result = JSON.parse(event.detail.xhr.response);
            var resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `
                <h2>Imagen Procesada</h2>
                <img src="${result.processed_image}" alt="Processed Image">
                <p>Número de caras detectadas: ${result.num_faces}</p>
            `;
        });
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
