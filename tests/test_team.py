def test_create_teams_and_conflict(client):
    # 1. POST team mới (Bổ sung headquarters/description nếu model team bắt buộc)
    payload = {"name": "Avengers", "headquarters": "New York"}
    res1 = client.post("/api/v1/teams", json=payload)
    assert res1.status_code in [200, 201]

    # 2. Tạo trùng tên team -> Báo 409
    res2 = client.post("/api/v1/teams", json=payload)
    assert res2.status_code == 409


def test_team_heroes_nested(client):
    # Tạo team
    res_team = client.post("/api/v1/teams", json={"name": "X-Men", "headquarters": "X-Mansion"})
    assert res_team.status_code in [200, 201]
    team_id = res_team.json()["id"]

    # Thêm hero vào team
    res_hero = client.post(
        "/api/v1/heroes",
        json={"name": "Wolverine", "secret_name": "Logan", "team_id": team_id}
    )
    assert res_hero.status_code in [200, 201]

    # Lấy danh sách hero của team
    res_nested = client.get(f"/api/v1/teams/{team_id}/heroes")
    assert res_nested.status_code == 200
    assert len(res_nested.json()) >= 1

    # Kiểm tra team 404
    res_404 = client.get("/api/v1/teams/99999/heroes")
    assert res_404.status_code == 404