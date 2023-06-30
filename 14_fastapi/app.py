from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()
app.conter = 0

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    code: str
    tax: float | None = None

    def price_brutto(self):
        price_brutto = self.price * self.tax / 100 + self.price
        return price_brutto

class HelloResp(BaseModel):
    msg: str

@app.get("/helo/{item_id}")
async def read_item(item_id):
    return {"message": "Hello " + item_id}

@app.get("/counter")
async def counter():
    app.conter += 1
    return f"Counter - {app.conter}"

@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name}")


@app.post("/items/")
async def create_item(item: Item):
    return f'Name: {item.name}', f'Gross: {item.price_brutto()}'