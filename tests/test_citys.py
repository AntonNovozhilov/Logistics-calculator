def test_all_city(test_client):
    response = test_client.get("/city")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["city_name"] == "Самара"
    assert data[1]["city_name"] == "Москва"


def test_first_city(test_client, city_sam):
    response = test_client.get(f"/city/{city_sam.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["city_name"] == "Самара"
