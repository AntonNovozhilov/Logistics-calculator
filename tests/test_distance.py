def test_all_dist(test_client):
    response = test_client.get("/distance")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["city_from"] == "Самара"
    assert data[0]["city_to"] == "Москва"
    assert data[0]["distance"] == 1075


def test_first_city(test_client, dist_sam_mos):
    response = test_client.get(f"/distance/{dist_sam_mos.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["city_from"] == "Самара"
    assert data["id"] == 1
