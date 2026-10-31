
from math import isfinite

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .services import summarize_usage

@require_GET
def usage_summary(request):
    """Return summary for a list of usages"""
    try:
        usages = request.GET.getlist("usage_kwh")
        usages_number = [float(value) for value in usages]
        
        if any(value < 0 or not isfinite(value) for value in usages_number):
            raise ValueError("Readings must be finite and nonnegative.")
        
        summary = summarize_usage(usages_number)
    except ValueError as error:
        return JsonResponse({"error": str(error)}, status=400)
    
    return JsonResponse(summary)