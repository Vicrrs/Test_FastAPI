from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import UploadFile
from pathlib import Path
from aiofile import async_open
from uuid import uuid4


app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/secao02/static', StaticFiles(directory='static'), name='static')
app.mount('/secao02/media', StaticFiles(directory='media'), name='media')
media = Path('media')


@app.get('/')
async def index(request: Request, usuario: str = 'Victor Roza'):
    context = {
        "request": request,
        "usuario": usuario
    }

    return templates.TemplateResponse('index.html', context=context)

# Nome do template com o mesmo nome da funcao


@app.get('/servicos')
async def servicos(request: Request):
    context = {
        "request": request,
    }

    return templates.TemplateResponse('servicos.html', context=context)


@app.post('/servicos')
async def card_servicos(request: Request):
    form = await request.form()

    servico: str = form.get('servico')
    print(f"Servico: {servico}")

    arquivo: UploadFile = form.get('arquivo')
    print(f"Nome: {arquivo.filename}")
    print(f"Tipo: {arquivo.content_type}")

    # Nome aleatorio para os arquivos
    arquivo_ext: str = arquivo.filename.split('.')[1]
    novo_nome: str = f"{str(uuid4())}.{arquivo_ext}"

    context = {
        "request": request,
        "imagem": novo_nome
    }

    async with async_open(f"{media}/{novo_nome}", "wb") as afile:
        await afile.write(arquivo.file.read())

    return templates.TemplateResponse('servicos.html', context=context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1",
                port=8000, log_level='info', reload=True)
