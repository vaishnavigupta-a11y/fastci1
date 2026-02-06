# def test_dummy():
#     assert 1 == 1

# def test_dummy():
#     assert 1 == 1
from fastapi.testclient import TestClient
# bina browser ke ham t4etskr skte hai testclinet ki help se  api automatic ke liey ebst hai
# from main eski helps e asa hota hai ki
#  hm broser ko req bejhete hai api se joki ekdma lhti hai liek ki user ne bejha hoaimport app, items   #

from main import app, items   # import your FastAPI app and items dict
#app server se apn fastapi ko check krte hai,or rqeus kbhi khi titak ietm update utem typ bhi rheti hai to us situa ke liye item dictonary ko bhiim,port kiya
client = TestClient(app)
#testcilemt ki hep se hm fak client user crrate krte hai joki fake req bejhat hai jisse hm autimatically check rk skte
# What is TestClient?

# TestClient is a tool provided by FastAPI (actually from Starlette) that allows you to:

# ✔ Test your API without starting the server
# ✔ Call your API endpoints like a normal client (browser, postman)
# ✔ Send GET, POST, PUT, DELETE requests in tests
# ✅ What does this line do?
# client = TestClient(app)

# ✔ It creates a fake client

# → Like Postman
# → But inside Python

# ✔ It uses your FastAPI app

# → Your app has routes like / or /items/1

# ✔ This client can now call your API

# Example:

# client.get("/items/1")
# client.post("/items/1", json=data)
# client.delete("/items/1")


# 1️⃣ Test: Create an item (POST)
def test_create_item():
    data = {
        "name": "Book",
        "description": "A good book",
        "price": 150.0
    }
    response = client.post("/items/1", json=data)

    assert response.status_code == 200
    body = response.json() 
    # respsne.json() baiscalky data jo ata hai api se usse dictanry form me cinvert krne ke liye hota hai
    # kyuki basically data send ya reviev json fom me hota hai itslike list jiss ehme index se acces knr aoreaga 
    # usse better hi ki dicetrny form me convert jkrede jisse ham key ki helps e check kr paye assert se or infuture caccess bhi kr oaye
    assert body["message"] == "Item created"
    assert body["item"]["name"] == "Book"


# 2️⃣ Test: Get item (GET)
def test_get_item():
    response = client.get("/items/1")

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Book"


# 3️⃣ Test: Full Update (PUT)
def test_update_item():
    data = {
        "name": "Updated Book",
        "description": "New desc",
        "price": 200.0
    }
    response = client.put("/items/1", json=data)
# assets mtlb check rknan
    assert response.status_code == 200
    body = response.json()
    assert body["item"]["name"] == "Updated Book"


# 4️⃣ Test: Partial Update (PATCH)
# assert checks equality
# If not equal → test FAIL.
def test_patch_item():
    data = {
        "name": "Laptop",

        "price": 250.0  # Only updating price
    }
    response = client.patch("/items/1", json=data)

    assert response.status_code == 200
    body = response.json()
    assert body["item"]["price"] == 250.0


# 5️⃣ Test: Delete item (DELETE)
def test_delete_item():
    response = client.delete("/items/1")

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Item deleted"


# 6️⃣ Test: Get item after delete (should not exist)
def test_get_after_delete():
    response = client.get("/items/1")

    assert response.status_code == 200
    assert response.json() == "Item not found"
