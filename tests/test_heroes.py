def test_create_hero(client):
    response = client.post(
        "/api/v1/heroes",
        json={"name": "Spider-Man", "secret_name": "Peter Parker", "age": 18}
    )
    data = response.json()
    assert response.status_code in [200, 201]
    assert data["name"] == "Spider-Man"
    assert "id" in data