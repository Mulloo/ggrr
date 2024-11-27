from .models import Equipment

def equipment_list(request):
    return {
        'equipment_list': Equipment.objects.all()
    }
