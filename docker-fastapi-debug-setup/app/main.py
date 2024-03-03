from fastapi import FastAPI
app = FastAPI()
print("Waiting for debugger attach")


@app.get("/")
async def root(
    abc: str = "abc",
    xyza: str = "xyz",
    aaa: str = "aaa",
    bbb: str = "bbb",
    ccc: str = "cc",
):
    return {"message": "Hello This"}
