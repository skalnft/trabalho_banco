from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
# from database.dbconnection import connec

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": "Not found"})

@app.get('/')
def hello_world():
    return {'message': 'Helo World'}

@app.get("/pessoa/{id}")
def listar_pessoas(id: int):
    return id

@app.delete("/pessoa/{nome}")
def deletar_pessoa(nome: str):
    return "User deletado com sucesso!"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)