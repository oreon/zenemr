
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'appliedCharts', AppliedChartViewSet)
router.register(r'appliedChartsWritable', AppliedChartWritableViewSet)
router.register(r'appliedChartsComplete', AppliedChartCompleteViewSet)
router.register(r'appliedChartsLookup', AppliedChartLookupViewSet)
  
router.register(r'charts', ChartViewSet)
router.register(r'chartsWritable', ChartWritableViewSet)
router.register(r'chartsComplete', ChartCompleteViewSet)
router.register(r'chartsLookup', ChartLookupViewSet)
  
router.register(r'chartItems', ChartItemViewSet)
router.register(r'chartItemsWritable', ChartItemWritableViewSet)
router.register(r'chartItemsComplete', ChartItemCompleteViewSet)
router.register(r'chartItemsLookup', ChartItemLookupViewSet)
  
router.register(r'chartProcedures', ChartProcedureViewSet)
router.register(r'chartProceduresWritable', ChartProcedureWritableViewSet)
router.register(r'chartProceduresComplete', ChartProcedureCompleteViewSet)
router.register(r'chartProceduresLookup', ChartProcedureLookupViewSet)

    
