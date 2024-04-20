from django.http import JsonResponse
from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema
from .services import CurrencyConversionService

class CurrencyConversionSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = [
            {
                "name": "amount",
                "required": True,
                "location": "form",
                "schema": {"type": "number"}
            },
            {
                "name": "from_currency",
                "required": True,
                "location": "form",
                "schema": {"type": "string"}
            },
            {
                "name": "to_currency",
                "required": True,
                "location": "form",
                "schema": {"type": "string"}
            }
        ]
        manual_fields = super().get_manual_fields(path, method)
        manual_fields.extend(extra_fields)
        return manual_fields

@api_view(['POST'])
@schema(CurrencyConversionSchema())
def convert_currency(request):
    if request.method == 'POST':
        data = request.data
        amount = float(data.get('amount'))
        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')
        converted_amount, error = CurrencyConversionService.convert_currency(amount, from_currency, to_currency)
        if error:
            return JsonResponse({'error': error}, status=400)
        return JsonResponse({'converted_amount': converted_amount, 'error': None})
    else:
        return JsonResponse({'error': 'Метод не поддерживается'}, status=405)
