from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


def cars_filter(query_params: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for k, v in query_params.items():
        match k:
            case 'price__gt':
                qs = qs.filter(price__gt=v)
            case 'price__lt':
                qs = qs.filter(price__lt=v)
            case 'brand':
                qs = qs.filter(brand__exact=v)
            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{f}' for f in fields]]
                print(fields)
                if v not in fields:
                    raise ValidationError({'details': f'{v} is not a valid order value'})

                qs = qs.order_by(v)
            case _:
                raise ValidationError({'details': 'Invalid filter parameter'})
    return qs