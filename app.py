from fastapi import FastAPI
from pydantic import BaseModel
from utils.TransformaEmAudio import transforma_em_audio


class Texto(BaseModel):
    texto: str
    caminho_de_armazenamento: str


app = FastAPI(docs_url="/docs")


@app.post("/text-to-speech")
async def create_speech(dados: Texto):
    return transforma_em_audio(dados.texto, dados.caminho_de_armazenamento)
