from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from bills.views import usage_summary


def home(_request):
    return HttpResponse(
        "Energy Bill Explainer — development scaffold. "
        "This is not an official energy comparison service."
    )


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/bills/", include("bills.urls")),
    path("bills/usage-summary/", usage_summary, name="usage-summary"),
]
