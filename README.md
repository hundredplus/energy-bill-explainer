# Energy Bill Explainer

Energy Bill Explainer is a Django portfolio project for helping
Victorian households understand electricity bills and estimate
simplified annual electricity costs.

## Current milestone

The project currently contains a pure Python calculation engine
for single-rate electricity bills.

It calculates:

- billing days
- daily usage
- annualised usage
- annual supply cost
- annual usage cost
- estimated annual cost

Money and rate calculations use Python `Decimal`.

## MVP scope

Initial scope:

- Victoria
- electricity only
- manual bill entry
- single-rate tariff
- simplified estimates

Not included initially:

- OCR
- gas
- time-of-use tariffs
- demand tariffs
- full solar modelling
- official energy plan recommendations

## Run tests

Install dependencies:

    python -m pip install -r requirements-dev.txt

Run tests:

    PYTHONPATH=src pytest

## Disclaimer

This is an educational and portfolio project, not an official
energy comparison service. Estimates are simplified and may not
match actual electricity bills.