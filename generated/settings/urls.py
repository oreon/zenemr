
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'settingses', SettingsViewSet)
router.register(r'settingsesWritable', SettingsWritableViewSet)
router.register(r'settingsesComplete', SettingsCompleteViewSet)
router.register(r'settingsesLookup', SettingsLookupViewSet)
  
router.register(r'settings', SettingViewSet)
router.register(r'settingsWritable', SettingWritableViewSet)
router.register(r'settingsComplete', SettingCompleteViewSet)
router.register(r'settingsLookup', SettingLookupViewSet)
  
router.register(r'settingNames', SettingNameViewSet)
router.register(r'settingNamesWritable', SettingNameWritableViewSet)
router.register(r'settingNamesComplete', SettingNameCompleteViewSet)
router.register(r'settingNamesLookup', SettingNameLookupViewSet)
  
router.register(r'settingGroups', SettingGroupViewSet)
router.register(r'settingGroupsWritable', SettingGroupWritableViewSet)
router.register(r'settingGroupsComplete', SettingGroupCompleteViewSet)
router.register(r'settingGroupsLookup', SettingGroupLookupViewSet)

    
