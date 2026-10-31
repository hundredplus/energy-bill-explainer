def test_home_page_is_available(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Energy Bill Explainer" in response.content
    assert b"not an official energy comparison service" in response.content

