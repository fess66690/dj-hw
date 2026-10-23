from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter(field_name="created_at")
    status = filters.MultipleChoiceFilter(
        choices=AdvertisementStatusChoices.choices
    )

    class Meta:
        model = Advertisement
        fields = ('status', 'creator', 'created_at')
