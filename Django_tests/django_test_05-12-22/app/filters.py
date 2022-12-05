import django_filters
from .models import DataRecords


class SensorDataFilter(django_filters.FilterSet):

    class Meta:
        model = DataRecords

        fields = {
            "sensor": ["iexact"],
            "date": ["date__gt", "date__lt"],
            "value": ["lt", "gt"]
        }
