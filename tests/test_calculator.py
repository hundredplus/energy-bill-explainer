from datetime import date
from decimal import Decimal

import pytest

from energy_bill_explainer.calculator import (
    BillCalculationInput,
    BillValidationError,
    calculate_bill,
)


def make_bill(
    *,
    period_start: date = date(2026, 1, 1),
    period_end: date = date(2026, 3, 31),
    total_kwh: Decimal = Decimal("900"),
    daily_supply_charge: Decimal = Decimal("1.20"),
    usage_rate_per_kwh: Decimal = Decimal("0.30"),
) -> BillCalculationInput:
    return BillCalculationInput(
        period_start=period_start,
        period_end=period_end,
        total_kwh=total_kwh,
        daily_supply_charge=daily_supply_charge,
        usage_rate_per_kwh=usage_rate_per_kwh,
    )


def test_calculates_90_day_bill() -> None:
    result = calculate_bill(make_bill())

    assert result.billing_days == 90
    assert result.daily_usage_kwh == Decimal("10")
    assert result.annual_usage_kwh == Decimal("3650")
    assert result.annual_supply_cost == Decimal("438.00")
    assert result.annual_usage_cost == Decimal("1095.00")
    assert result.estimated_annual_cost == Decimal("1533.00")


def test_one_day_billing_period() -> None:
    bill = make_bill(
        period_start=date(2026, 1, 1),
        period_end=date(2026, 1, 1),
        total_kwh=Decimal("5"),
    )

    result = calculate_bill(bill)

    assert result.billing_days == 1
    assert result.daily_usage_kwh == Decimal("5")
    assert result.annual_usage_kwh == Decimal("1825")


def test_zero_usage_is_allowed() -> None:
    bill = make_bill(
        total_kwh=Decimal("0")
    )

    result = calculate_bill(bill)

    assert result.daily_usage_kwh == Decimal("0")
    assert result.annual_usage_kwh == Decimal("0")


def test_zero_supply_charge_is_allowed() -> None:
    bill = make_bill(
        daily_supply_charge=Decimal("0")
    )

    result = calculate_bill(bill)

    assert result.annual_supply_cost == Decimal("0")


def test_zero_usage_rate_is_allowed() -> None:
    bill = make_bill(
        usage_rate_per_kwh=Decimal("0")
    )

    result = calculate_bill(bill)

    assert result.annual_usage_cost == Decimal("0")


def test_rejects_end_date_before_start_date() -> None:
    bill = make_bill(
        period_start=date(2026, 2, 1),
        period_end=date(2026, 1, 31),
    )

    with pytest.raises(
        BillValidationError,
        match="period_end",
    ):
        calculate_bill(bill)


def test_rejects_negative_usage() -> None:
    bill = make_bill(
        total_kwh=Decimal("-1")
    )

    with pytest.raises(
        BillValidationError,
        match="total_kwh",
    ):
        calculate_bill(bill)


def test_rejects_negative_supply_charge() -> None:
    bill = make_bill(
        daily_supply_charge=Decimal("-0.01")
    )

    with pytest.raises(
        BillValidationError,
        match="daily_supply_charge",
    ):
        calculate_bill(bill)


def test_rejects_negative_usage_rate() -> None:
    bill = make_bill(
        usage_rate_per_kwh=Decimal("-0.01")
    )

    with pytest.raises(
        BillValidationError,
        match="usage_rate_per_kwh",
    ):
        calculate_bill(bill)


def test_outputs_are_decimal_values() -> None:
    result = calculate_bill(make_bill())

    assert isinstance(result.daily_usage_kwh, Decimal)
    assert isinstance(result.annual_usage_kwh, Decimal)
    assert isinstance(result.annual_supply_cost, Decimal)
    assert isinstance(result.annual_usage_cost, Decimal)
    assert isinstance(result.estimated_annual_cost, Decimal)


def test_irregular_billing_period() -> None:
    bill = make_bill(
        period_start=date(2026, 1, 10),
        period_end=date(2026, 2, 3),
        total_kwh=Decimal("250"),
    )

    result = calculate_bill(bill)

    assert result.billing_days == 25
    assert result.daily_usage_kwh == Decimal("10")

def test_billing_period_can_span_leap_day() -> None:
    bill = make_bill(
        period_start=date(2024, 2, 28),
        period_end=date(2024, 3, 1),
        total_kwh=Decimal("30"),
    )

    result = calculate_bill(bill)

    assert result.billing_days == 3
    assert result.daily_usage_kwh == Decimal("10")