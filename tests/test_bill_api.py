import pytest
from rest_framework.test import APIClient
from decimal import Decimal

@pytest.mark.django_db
def test_bill_analysis_api_returns_estimate():
    client = APIClient()

    response = client.post("/api/bills/analyse/", 
                           {
                                "period_start": "2026-01-01",
                                "period_end": "2026-03-31",
                                "total_kwh": "900",
                                "daily_supply_charge": "1.20",
                                "usage_rate_per_kwh": "0.30",
                           }, 
                           format="json")

    assert response.status_code == 200

    data = response.json()
    
    assert Decimal(data["daily_usage_kwh"]) == Decimal("10")
    assert Decimal(data["annual_usage_kwh"]) == Decimal("3650")
    assert Decimal(data["estimated_annual_cost"]) == Decimal("1533")

@pytest.mark.django_db
def test_bill_analysis_api_rejects_invalid_dates():
    client = APIClient()

    response = client.post(
        "/api/bills/analyse/",
        {
            "period_start": "2026-03-31",
            "period_end": "2026-01-01",
            "total_kwh": "900",
            "daily_supply_charge": "1.20",
            "usage_rate_per_kwh": "0.30",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "period_end" in response.json()

@pytest.mark.django_db
def test_bill_analysis_api_rejects_negative_usage():
    client = APIClient()

    response = client.post(
        "/api/bills/analyse/",
        {
            "period_start": "2026-01-01",
            "period_end": "2026-03-31",
            "total_kwh": "-1",
            "daily_supply_charge": "1.20",
            "usage_rate_per_kwh": "0.30",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "total_kwh" in response.json()

