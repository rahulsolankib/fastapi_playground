from fastapi import FastAPI, BackgroundTasks
import asyncio
import time
import uvicorn

app = FastAPI()
count = 0


@app.get("/")
async def root():
    return {"message": "Hello World"}

async def write_to_file(name):
    with open("log.txt", "a") as f:
        f.write(f"{name} - {time.time()}\n")
        await asyncio.sleep(5)
        return "Completed"


@app.get("/send/{email}")
async def send(email: str, background_tasks: BackgroundTasks):
    global count
    count += 1
    print(str(count) + "\n")
    background_tasks.add_task(write_to_file, 'Rahul')

    return {"msg": "email sent!"}


# if __name__ == "__main__":
#     uvicorn.run(app="main:app", host="127.0.0.1", port=9393, reload=True)
