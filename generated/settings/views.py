
from rest_framework import viewsets
from .serializers import *
    
class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    
class SettingsLookupViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsLookupSerializer
    
class SettingsCompleteViewSet(SettingsViewSet):
    serializer_class = FullSettingsSerializer
    
class SettingsWritableViewSet(SettingsViewSet):
    serializer_class = SettingsWritableSerializer    

class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    
class SettingLookupViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingLookupSerializer
    
class SettingCompleteViewSet(SettingViewSet):
    serializer_class = FullSettingSerializer
    
class SettingWritableViewSet(SettingViewSet):
    serializer_class = SettingWritableSerializer    

class SettingNameViewSet(viewsets.ModelViewSet):
    queryset = SettingName.objects.all()
    serializer_class = SettingNameSerializer
    
class SettingNameLookupViewSet(viewsets.ModelViewSet):
    queryset = SettingName.objects.all()
    serializer_class = SettingNameLookupSerializer
    
class SettingNameCompleteViewSet(SettingNameViewSet):
    serializer_class = FullSettingNameSerializer
    
class SettingNameWritableViewSet(SettingNameViewSet):
    serializer_class = SettingNameWritableSerializer    

class SettingGroupViewSet(viewsets.ModelViewSet):
    queryset = SettingGroup.objects.all()
    serializer_class = SettingGroupSerializer
    
class SettingGroupLookupViewSet(viewsets.ModelViewSet):
    queryset = SettingGroup.objects.all()
    serializer_class = SettingGroupLookupSerializer
    
class SettingGroupCompleteViewSet(SettingGroupViewSet):
    serializer_class = FullSettingGroupSerializer
    
class SettingGroupWritableViewSet(SettingGroupViewSet):
    serializer_class = SettingGroupWritableSerializer    

  