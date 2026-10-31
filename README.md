# Energy Bill Explainer

Energy Bill Explainer is a Django web application and API that helps Victorian households understand a single-rate electricity bill, estimate annual usage and cost, and prepare accurate inputs for official comparison services.

The application is a companion to Victorian Energy Compare and Energy Made Easy. It is not an official comparison service, does not guarantee the cheapest plan, and does not provide financial advice.

## Day 1 status

- Fresh Django project and `bills` app
- Environment-based development settings
- Minimal landing response with the product caveat
- Pytest smoke test
- Product scope, trade-off log, and interview notebook

Calculation logic, database models, REST endpoints, AER ingestion, PostgreSQL, Docker and CI intentionally come later in the four-week plan.

## Version 1 scope

- Victoria-only electricity bill explanation
- Manual entry of bill figures
- Single-rate tariffs
- Decimal-based annualised calculations
- Deterministic warnings and explanations
- AER Product Reference Data ingestion with limited normalisation
- Simple Django templates and REST endpoints

## Non-goals

- Replacing an official comparison service
- Guaranteeing a future bill or cheapest plan
- Bill PDF upload or OCR
- Complete time-of-use, controlled-load, demand, gas or solar modelling
- A separate frontend framework
- AI-generated recommendations

## Local setup

Python 3.12 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Run quality checks:

```bash
pytest
python manage.py check
ruff check .
```

## Repository layout

```text
apps/bills/           Django bill domain app
config/               Project settings and root URL configuration
docs/interview_notes.md
docs/tradeoffs.md
tests/                Cross-layer tests
```

## Product caveat

This educational demonstration produces simplified estimates that may not match actual bills. Users should verify results with Victorian Energy Compare, Energy Made Easy, retailer documents and official government guidance.

