from fastapi import FastAPI
from api.deps import DBSession
from db.session import engine
from crud.crud_user import User, Base
from sqlalchemy.schema import CreateTable


print(CreateTable(User.__table__).compile())
app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'Working!'}


# if __name__ == '__main__':
#     uvicorn.run('main:app', port=8000, reload=True)
