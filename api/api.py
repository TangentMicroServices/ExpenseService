from django.conf.urls import url, include
from .models import Expense
from rest_framework import routers, serializers, viewsets


## Some boilerplate code to get you started ...

# Serializers define the API representation.
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        
# ViewSets define the view behavior.
class ExpenseViewSet(viewsets.ModelViewSet):
    
    queryset = Expense.objects.all()
    model = Expense
    serializer_class = ExpenseSerializer

    def get_queryset(self):
    	
    	user = self.request.user
        if not user.is_authenticated():
            return Expense.objects.none()

        if user.is_superuser:
            return Expense.objects.all()
        else:
            return Expense.objects.filter(user=user.id)

router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
