from fastapi import APIRouter, Response
from controller.productController import create_product_controller, get_product_controller, get_product_by_id_controller, delete_product_controller, update_product_controller 
from models.productModel import Product

productRouter = APIRouter(
    prefix = "/products",
    tags = ["products"]
)

#Status code:

@productRouter.post("/postProduct")
async def create_product(product: Product, response: Response):
    return await create_product_controller(product, response)


@productRouter.get("/getProducts")
async def get_products(response: Response):
    return await get_product_controller(response)


@productRouter.get("/getProducts/{productid}")
async def get_products(productid: str, response: Response):
    return await get_product_by_id_controller(productid, response)


@productRouter.put('/updateproduct/{productid}')
async def update_product(productid: str, product: Product, response: Response):
    return await update_product_controller(productid,product,response)


@productRouter.delete('/deleteproduct/{productid}')
async def delete_product(productid: str, response: Response):
    return await delete_product_controller(productid,response)

