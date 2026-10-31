from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home(_request):
    return HttpResponse(
        "Energy Bill Explainer — development scaffold. "
        "This is not an official energy comparison service."
    )


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("bills/", include("apps.bills.urls")),
]

