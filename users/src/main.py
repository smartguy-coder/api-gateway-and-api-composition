from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check")
async def heath_check():
    return {"status": "Users service started."}

@app.get('/{user_id}')
async def get_user_data(user_id: int):
    return {"user": {"name": "Alex", "id": user_id}}