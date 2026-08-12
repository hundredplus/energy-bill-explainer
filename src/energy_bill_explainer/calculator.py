from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

DAYS_PER_YEAR = Decimal("365")

class BillValidationError(ValueError):
    """Raised when a bill calculation input is invalid."""

@dataclass(frozen=True)
class BillCalculationInput:
    period_start: date
    period_end: date
    total_kwh: Decimal
    daily_supply_charge: Decimal
    usage_rate_per_kwh: Decimal

@dataclass(frozen=True)
class BillCalculationResult:
    billing_days: int
    daily_usage_kwh: Decimal
    annual_usage_kwh: Decimal
    annual_supply_cost: Decimal
    annual_usage_cost: Decimal
    estimated_annual_cost: Decimal

def calculate_bill(
        bill: BillCalculationInput,

) -> BillCalculationResult:
    billing_days = (bill.period_end - bill.period_start).days + 1

    if billing_days <= 0:
        raise BillValidationError(
            "period_end must be on or after period_start"
        )

    if bill.total_kwh < 0:
        raise BillValidationError(
            "total_kwh cannot be negative"
        )

    if bill.daily_supply_charge < 0:
        raise BillValidationError(
            "daily_supply_charge cannot be negative"
        )

    if bill.usage_rate_per_kwh < 0:
        raise BillValidationError(
            "usage_rate_per_kwh cannot be negative"
        )

    billing_days_decimal = Decimal(billing_days)

    daily_usage_kwh = (
        bill.total_kwh / billing_days_decimal
    )

    annual_usage_kwh = (
        daily_usage_kwh * DAYS_PER_YEAR
    )

    annual_supply_cost = (
        bill.daily_supply_charge * DAYS_PER_YEAR
    )

    annual_usage_cost = (
        annual_usage_kwh * bill.usage_rate_per_kwh
    )

    estimated_annual_cost = (
        annual_supply_cost + annual_usage_cost
    )

    return BillCalculationResult(
        billing_days=billing_days,
        daily_usage_kwh=daily_usage_kwh,
        annual_usage_kwh=annual_usage_kwh,
        annual_supply_cost=annual_supply_cost,
        annual_usage_cost=annual_usage_cost,
        estimated_annual_cost=estimated_annual_cost,
    )