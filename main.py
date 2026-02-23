from fastapi import FastAPI, UploadFile, File
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Spleeter ready"}

@app.post("/separate")
async def separate(file: UploadFile = File(...)):
    filename = file.filename
    with open(filename, "wb") as f:
        f.write(await file.read())

    subprocess.run([
        "spleeter",
        "separate",
        "-p", "spleeter:2stems",
        "-o", "output",
        filename
    ])

    return {"status": "done"}
