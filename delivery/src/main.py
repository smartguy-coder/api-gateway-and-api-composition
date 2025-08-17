from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check/")
async def heath_check():
    return {"status": "Delivery service started."}

@app.get('/{user_id}')
async def get_user_deliveries(user_id: int):
    return {"deliveries": [{'address': 'Odesa'}]}