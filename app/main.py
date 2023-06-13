from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from database.dbconnection import cursor

app = FastAPI()

@app.get("/paises")
def listar_paises():
    paises = _buscar_paises()
    return JSONResponse({"Países": paises})

@app.get("/pais/{id}")
def deletar_pais(id: int):
    _excluir_pais_por_id(id)
    return JSONResponse('DELETED')

def _buscar_paises():
    cursor.execute("SELECT * FROM BUSCAR_PAISES();")
    results = cursor.fetchall()
    return results

def _excluir_pais_por_id(id):
    cursor.execute(f'EXEC DELETAR_PAIS_POR_NOME @id = {id};')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3333)