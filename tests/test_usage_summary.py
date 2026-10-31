import pytest

from bills.services import summarize_usage


def test_usage_summary_returns_count_total_and_average(client):
    response = client.get("/bills/usage-summary/?usage_kwh=10&usage_kwh=20&usage_kwh=0")
    assert response.status_code == 200
    assert response.json() == {"count": 3, "total": 30.0, "average": 10.0}


@pytest.mark.parametrize(
    "query",
    [
        "",
        "usage_kwh=",
        "usage_kwh=text",
        "usage_kwh=-1",
        "usage_kwh=nan",
        "usage_kwh=inf",
        "usage_kwh=-inf",
        "usage_kwh=1e308&usage_kwh=1e308",
    ],
)
def test_usage_summary_rejects_invalid_readings(client, query):
    response = client.get(f"/bills/usage-summary/?{query}")
    assert response.status_code == 400
    assert "error" in response.json()


def test_usage_summary_requires_get(client):
    assert client.post("/bills/usage-summary/").status_code == 405


def test_usage_summary_allows_zero():
    assert summarize_usage([0.0]) == {"count": 1, "total": 0.0, "average": 0.0}
