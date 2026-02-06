# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# import models
# import schemas

# from fastapi import FastAPI
# #fast api framwork lirbry hai jisse ham fastapi class ko import kr rhe hai aage chalkr 
# # eska instance mtlb ovject banayega
# #fastapi se jo api banta hai wo satly banaskte ai or ye atomatic datavalidtaion,iteractive
# #  api docmentaion(swagger se /docs kkre broser me hi api check kr skte hai),(token)deendcy
# #  injection bhi privide 
# from pydantic import BaseModel
# # ye sb pydantic me presnt hoga hai validation provid ekrta hai mtln agr data validta
# #  ekrte time "20" ksi ne imput diya hhona 20 cahahiye to automatif covert kr deta hai 
# # yw ,agr no possibel cobertsion ke bad equl to error de dete h             
# # json ko obev obje ko json me coebtr kta hai as per need data req sne dlrte time
# # pr ye sb use kr kse esliye basemodel class use krte hai jisse apn model banate hai or ye jitni priperti suni wo sb use kr skte hai

# from typing import Optional
# # //kisi value ko jb optinal krna ho tln maindatory ni wo value ho ay ti hogfi str likha
# #  hai to strung wrn anone mtln ni hoga value optinal hai
# # app namka vairble ya object bol skte hai banate hi fatsapi clas ska use krke jisse 
# # aaage chalkr ham essi object app se isnatnce se routes ke acc resptice route ke acc 
# # endpoint (spefic roite pr clck ya sne krne pr spefic func us func ko endpoint bolte hai) 
# # ye handle kr skte mtlb route ,endpoint g=hadle krne ke liye app nstance banta ahi
# # basmeodle json body dataa ko obkect me cinvetr krta hai
# app = FastAPI()
# # asa bolskte hai basemodel class ko dyn me d=rkhte hue suse hamne ek class me inehrit kr 
# # liya hai calss ka nam item hai
# # ya to bol skte hai basemodle class se hamne schem,a banaya hai ek model datastructue 
# # data kais estor ehoag uska fo,rya schema
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None 
#     # //optional value ni bhi dnege to cahlega ni dne epr a a none trette hogi pr agr bje
#     #  rh hi 
#     # valaue sue rto wo string hi honi cahahiye wrn ana bejha wo none trat hogo
#     price: float


#     # datatrsire krne ke intenson se as a temp database use kr rhe hai ham dictinary o
# # This dictionary stores items using unique IDs as the key, and the value is a dictionary
# #  or an instance of Item. For example:

# # items = {
# #     1: {"name": "Laptop", "price": 999.99},
# #     2: {"name": "Mouse", "price": 29.99}
# # }
#     # badme ye dtabas es echange hojyegi

# items = {}

# # {
# #     1: { "name": "...", "price": ... }
# # }
# @app.post("/items/{item_id}")
# #
# #  //fastapi url se itemid letahi or int me covet kr deta hai or func me pas kr dte hai
# # jo bhi data sne dr rhe hai json mem wo atomatic validated bjec data me jaise hamne schem
# #  dfeine kiya hoag typ usme covert hojyega
# # requnet j arhi hai usmes e hi idem id item ajise paramete rmilha joki aage func me use 
# # hoga
# #actual me json data receive hota hai url aya route me jb requ posts ne dhoti hai r wo 
# # ht
# #  baseodle sb convert kr leta hai
# # //fastapi khudse hi ane wale data ko validat ekrke schem aitem ka jo banaya hai su 
# # format me covert kr det ahai
# def create_item(item_id: int, item: Item): 
#     items[item_id] = item
#     # item to respsn eke trh sne dhora jo actail me dictrny ohiat ahi pr fastapi suse
#     #  jsn me coevrt krke user ko dikahta ahi bidy me as a succefsul reus ke trj
#     return {"message": "Item created", "item": item}


# # How FastAPI works:

# # FastAPI automatically extracts the item_id from the URL (e.g., 1, 42, etc.), converts it to the appropriate type (in this case, int), and passes it to the function (get_item).
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     # if item id hai dicetry e=me to rpestive  items return kr dega 
#     # agr ni ahi ri sceond argyment print hoga item notdind waka
#     return items.get(item_id, "Item not found") 

# @app.put("/items/{item_id}")
# # item: Item:

# # This parameter receives the data sent in the request body. FastAPI will parse the incoming 
# # JSON body and validate it using the Item Pydantic model.

# def update_item(item_id: int, item: Item):
#     items[item_id] = item
#     return {"message": "Item updated", "item": item}
# # Pydantic Model (Item):  tye conversuon ka try krti ahi like "20" to 20 p agr ek dma s ematch ni hora type ya numbe rof argyem tn ke cas eme 400 ba dreq

# # In the Item model, you would define attributes such as name, description, and price. FastAPI automatically validates that the incoming data matches the structure of the Item model.

# # If the incoming data doesn't match the model (e.g., missing required fields or invalid types), FastAPI will return a 400 Bad Request error to the clien
# @app.patch("/items/{item_id}")
# # item: Item: This parameter will receive the data sent in the request body. The Item class is a Pydantic model, and FastAPI will automatically 
# # convert the incoming JSON into an Item instance.
# def patch_item(item_id: int, item: Item):
#     if item_id in items:
#         stored_item = items[item_id].dict()
#         update_data = item.dict(exclude_unset=True)
#         stored_item.update(update_data)
#         items[item_id] = stored_item
#         return {"message": "Item partially updated", "item": stored_item}
#     return {"error": "Item not found"}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     if item_id in items:
#         del items[item_id]
#         return {"message": "Item deleted"}
#     return {"error": "Item not found"}





# # make a api having get put post patch delete ethod using fastapi framwork in python give me code of it explaining each and eberylinr and words 
# # 


# # make a api having get put post patch delete ethod using fastapi framwork in python give me code of it explaining each and eberylinr and words  similar code and then connect it to sqlite used modue methof meaning you have to make different file for model schemas or whatever required and then connect hat trhings and how we get to know rhat it is cinnecyed 


# # make a api having get put post patch delete ethod using fastapi framwork in python give me code of it explaining each and eberylinr and words  similar code and then connect it to postgrel used modue methof meaning you have to make different file for model schemas or whatever required and then connect hat trhings and how we get to know rhat it is cinnecyed 
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal

# Create tables in PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency → Every API call will get a DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE ITEM (POST)
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    new_item = models.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# READ ITEM (GET)
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        return {"error": "Item not found"}
    return item


# UPDATE ITEM (PUT)
@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, updated: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        return {"error": "Item not found"}

    item.name = updated.name
    item.description = updated.description
    item.price = updated.price

    db.commit()
    db.refresh(item)
    return item


# PARTIAL UPDATE (PATCH)
@app.patch("/items/{item_id}", response_model=schemas.ItemResponse)
def patch_item(item_id: int, updated: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        return {"error": "Item not found"}

    update_data = updated.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


# DELETE ITEM
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        return {"error": "Item not found"}

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}
