# def test_dummy():
#     assert 1 == 1
from fastapi.testclient import TestClient
from main import app, items   # import your FastAPI app and items dict

client = TestClient(app)


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

    assert response.status_code == 200
    body = response.json()
    assert body["item"]["name"] == "Updated Book"


# 4️⃣ Test: Partial Update (PATCH)
def test_patch_item():
    data = {
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
