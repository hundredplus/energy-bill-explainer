from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from energy_bill_explainer.calculator import (
    BillCalculationInput,
    calculate_bill,
)

from .serializers import BillAnalysisSerializer

class BillAnalysisView(APIView):
    def post(self, request):
        serializer = BillAnalysisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        bill = BillCalculationInput(**data)

        result = calculate_bill(bill)

        return Response(
            {
                "billing_days": result.billing_days,
                "daily_usage_kwh": str(result.daily_usage_kwh),
                "annual_usage_kwh": str(result.annual_usage_kwh),
                "annual_supply_cost": str(result.annual_supply_cost),
                "annual_usage_cost": str(result.annual_usage_cost),
                "estimated_annual_cost": str(result.estimated_annual_cost),
            },
            status=status.HTTP_200_OK,
        )
# Create your views here.
