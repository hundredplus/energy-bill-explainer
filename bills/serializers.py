from decimal import Decimal
from rest_framework import serializers

class BillAnalysisSerializer(serializers.Serializer):
    period_start = serializers.DateField()
    period_end = serializers.DateField()
    total_kwh = serializers.DecimalField(max_digits=12, decimal_places=3, min_value=Decimal("0"))
    daily_supply_charge = serializers.DecimalField(max_digits=10, decimal_places=4, min_value=Decimal("0"))
    usage_rate_per_kwh = serializers.DecimalField(max_digits=10, decimal_places=6, min_value=Decimal("0"))

    def validate(self, attrs):
        if attrs["period_end"] < attrs["period_start"]:
            raise serializers.ValidationError(
                {
                    "period_end": (
                        "period_end must be on or after period_start"
                    )
                }
            )

        return attrs