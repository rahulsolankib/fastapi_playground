from fastapi import FastAPI
from api.deps import DBSession
app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'Working!'}


# if __name__ == '__main__':
#     uvicorn.run('main:app', port=8000, reload=True)
