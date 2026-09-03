from models.productModel import Product
from fastapi import Response
from dbConnect import productCollection
from bson import ObjectId

products = []
id = 0

async def create_product_controller(product: Product, response: Response):
    global id
    try:
        # id += 1
        # product.id = id
        # products.append(product)
        # response.status_code = 201

        result = await productCollection.insert_one(product.dict())
        product.id = str(result.inserted_id)
        return {"isSuccess": True,"message": "Product created successfully!", "product": product}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{"message": str(e),"isSuccess": False}


async def get_product_controller(response: Response):
    try:
        productss = []
        async for product in productCollection.find():
            product["id"] = str(product["_id"])
            productss.append(Product(**product))
        # response.status_code = 200
        return {"products": productss, "isSuccess": True}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": "Error fetching products", "isSuccess": False}


async def get_product_by_id_controller(productid: str, response: Response):
    try:
        response.status_code = 200
        product = await productCollection.find_one({"_id": ObjectId(product)})
        product["_id"] = str(product["_id"])
        if product:
                return {"product": Product(**product), "isSuccess": True}
            
        response.status_code = 404
        return {"message": "Product not found", "isSuccess": False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": "Error fetching product", "isSuccess": False}

async def update_product_controller(productid: str, product: Product, response: Response):
    try:
        result = await productCollection.update_one(
            {'_id':ObjectId(productid)},
            {'$set': product.dict()}
        )
        if result.modified_count == 1:
            response.status_code = 200
            return {'isSuccess': True, 'message': 'Product Updated Successfully', 'product': product}

        response.status_code = 404
        return {'isSuccess': False, 'message': 'Product not found'}

    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e)}


async def delete_product_controller(productid: str, response: Response):
    try:
        result = await productCollection.delete_one({'_id' : ObjectId(productid)})
        if result.deleted_count == 1:
            response.status_code = 200
            return {'isSuccess': True, 'message': 'Product Deleted Successfully'}
        response.status_code = 404
        return {'isSuccess':False, 'message' : 'Product not found'}
    
    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e)}
