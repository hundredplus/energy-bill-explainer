# Energy Bill Explainer

A small Django REST API backed by a standalone Python calculation engine. It turns a manually entered Victorian electricity bill into a transparent, simplified annual cost estimate.

**Project:** [GitHub repository](https://github.com/hundredplus/energy-bill-explainer)  
**Portfolio:** [erictran.dev](https://erictran.dev/#work)

## What it does

Submit the bill period, total usage, daily supply charge, and usage rate. The API returns the billing duration, average daily usage, annualised usage, and estimated annual supply, usage, and combined costs.

The calculation engine is kept separate from Django so the core logic can be reused independently. Calculations use Python's `Decimal` for monetary and rate values, and the API validates dates and non-negative numeric inputs.

## API

The endpoint accepts a JSON `POST` at `/api/bills/analyse/`.

```bash
curl -X POST http://127.0.0.1:8000/api/bills/analyse/ \
  -H "Content-Type: application/json" \
  -d '{
    "period_start": "2025-01-01",
    "period_end": "2025-01-30",
    "total_kwh": "300.000",
    "daily_supply_charge": "1.0500",
    "usage_rate_per_kwh": "0.295000"
  }'
```

A successful response contains:

```json
{
  "billing_days": 30,
  "daily_usage_kwh": "10",
  "annual_usage_kwh": "3650",
  "annual_supply_cost": "383.2500",
  "annual_usage_cost": "1076.750000",
  "estimated_annual_cost": "1460.000000"
}
```

The estimate annualises the bill's average daily usage over 365 days and applies the submitted single-rate tariff. It is a useful explanation of the supplied inputs, not a comparison with available retail plans.

## Run locally

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python manage.py runserver
```

The API is then available at `http://127.0.0.1:8000/api/bills/analyse/`.

## Scope and limitations

- Victorian residential electricity bills
- Manual bill data entry
- Single-rate usage tariff and daily supply charge
- Simplified 365-day annualisation

This version does not include OCR, gas, time-of-use or demand tariffs, detailed solar modelling, or official retailer-plan recommendations. It is an educational portfolio project, not financial advice or an official energy comparison service; actual bills can differ due to tariff structures, discounts, concessions, solar credits, and other charges.

## Development

Install the development dependencies with `python -m pip install -r requirements-dev.txt`. Run the test suite with:

```bash
PYTHONPATH=src pytest
```
