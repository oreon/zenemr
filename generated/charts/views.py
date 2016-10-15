
from rest_framework import viewsets
from .serializers import *
    
class AppliedChartViewSet(viewsets.ModelViewSet):
    queryset = AppliedChart.objects.all()
    serializer_class = AppliedChartSerializer
    
class AppliedChartLookupViewSet(viewsets.ModelViewSet):
    queryset = AppliedChart.objects.all()
    serializer_class = AppliedChartLookupSerializer
    
class AppliedChartCompleteViewSet(AppliedChartViewSet):
    serializer_class = FullAppliedChartSerializer
    
class AppliedChartWritableViewSet(AppliedChartViewSet):
    serializer_class = AppliedChartWritableSerializer    

class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    
class ChartLookupViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartLookupSerializer
    
class ChartCompleteViewSet(ChartViewSet):
    serializer_class = FullChartSerializer
    
class ChartWritableViewSet(ChartViewSet):
    serializer_class = ChartWritableSerializer    

class ChartItemViewSet(viewsets.ModelViewSet):
    queryset = ChartItem.objects.all()
    serializer_class = ChartItemSerializer
    
class ChartItemLookupViewSet(viewsets.ModelViewSet):
    queryset = ChartItem.objects.all()
    serializer_class = ChartItemLookupSerializer
    
class ChartItemCompleteViewSet(ChartItemViewSet):
    serializer_class = FullChartItemSerializer
    
class ChartItemWritableViewSet(ChartItemViewSet):
    serializer_class = ChartItemWritableSerializer    

class ChartProcedureViewSet(viewsets.ModelViewSet):
    queryset = ChartProcedure.objects.all()
    serializer_class = ChartProcedureSerializer
    
class ChartProcedureLookupViewSet(viewsets.ModelViewSet):
    queryset = ChartProcedure.objects.all()
    serializer_class = ChartProcedureLookupSerializer
    
class ChartProcedureCompleteViewSet(ChartProcedureViewSet):
    serializer_class = FullChartProcedureSerializer
    
class ChartProcedureWritableViewSet(ChartProcedureViewSet):
    serializer_class = ChartProcedureWritableSerializer    

  