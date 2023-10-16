import os
from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
from fastapi.responses import FileResponse
import uuid 

app = FastAPI()

class TextToSpeechRequest(BaseModel):
    text: str

@app.post("/text-to-speech/")
def text_to_speech(request: TextToSpeechRequest):
    try:
        mytext = request.text
        language = 'en'
        unique_filename = f'output_{str(uuid.uuid4())}.wav'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(unique_filename)
        return FileResponse(unique_filename, headers={'Content-Disposition': 'attachment; filename="output.wav"'})
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
