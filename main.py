import uvicorn
from fastapi import FastAPI

from api.routers import orders

app = FastAPI(
    title='Dog walkers service',
    description='Сервис заказа выгула собак',
    version='1.0.0',
    docs_url='/',
    root_path='/api',
)

app.include_router(orders.router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8462)
