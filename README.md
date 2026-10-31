# Energy Bill Explainer

A Django application and REST API that helps Victorian households understand a
single-rate electricity bill. It combines a standalone Decimal calculation engine
with a usage-summary endpoint and a simple landing page.

It is an educational companion to official comparison services, not an official
comparison service or a guarantee of the cheapest plan.

## Run locally

Requires Python 3.12 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Alternatively, use `uv venv` and `uv pip install -e '.[dev]'`.
Open `http://127.0.0.1:8000/` for the landing page.

Settings read `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` from
the process environment. `.env.example` documents their names; `.env` files are
not loaded automatically. To use your own trusted local `.env` in a POSIX shell:

```bash
cp .env.example .env
set -a
. ./.env
set +a
```

The defaults are for local development. Configure an actual secret key, disable
debugging and configure allowed hosts before any production deployment.

## Bill analysis API

POST `/api/bills/analyse/` with bill dates, total usage, daily supply charge,
and a single usage rate:

```bash
curl -X POST http://127.0.0.1:8000/api/bills/analyse/ \
  -H 'Content-Type: application/json' \
  -d '{"period_start":"2025-01-01","period_end":"2025-01-30","total_kwh":"300.000","daily_supply_charge":"1.0500","usage_rate_per_kwh":"0.295000"}'
```

The response includes billing days, average daily and annualised usage, annual
supply and usage costs, and total estimated annual cost. Monetary calculations use
`Decimal`; dates and nonnegative inputs are validated. Usage is annualised over
365 days using the supplied single-rate tariff.

## Usage summary

GET `/bills/usage-summary/` with repeated `usage_kwh` parameters:

```bash
curl 'http://127.0.0.1:8000/bills/usage-summary/?usage_kwh=10&usage_kwh=20'
```

Response: `{"count": 2, "total": 30.0, "average": 15.0}`.
Readings must be finite and nonnegative; missing or invalid input returns HTTP 400.
This endpoint uses floating-point summaries, separate from Decimal bill costing.

## Development

```bash
pytest
python manage.py check
ruff check .
```

Both the GitHub bill-calculation tests and the iMac landing-page test are kept.
The usage-summary endpoint has additional validation tests.

## Layout

- `bills/`: Django views, serializers, usage service and URLs.
- `src/energy_bill_explainer/`: standalone bill-calculation engine.
- `config/`: project settings and root URLs.
- `tests/`: API, calculation, landing-page and usage-summary tests.
- `docs/`: learning checklist, interview notes and trade-offs from the iMac work.

The preserved iMac source originally used `apps/bills/`. Its usage service now
lives in `bills/` alongside the existing GitHub API to avoid duplicate Django apps.
The exact original source is retained on branch `preserve/imac-2026-10-31`.

## Scope and limitations

Manual bill entry, Victorian electricity, a single usage rate and a daily supply
charge are supported. OCR, bill uploads, AER data ingestion, plan recommendations,
time-of-use, demand tariffs, detailed solar modelling and gas are not implemented.
Learning notes describe future work, not a promise that these features exist.
Actual bills can differ because of discounts, concessions, tariff structures and
other charges. Verify decisions with official services and retailer information.
