
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'codes', CodeViewSet)
router.register(r'codesWritable', CodeWritableViewSet)
router.register(r'codesComplete', CodeCompleteViewSet)
router.register(r'codesLookup', CodeLookupViewSet)
  
router.register(r'chapters', ChapterViewSet)
router.register(r'chaptersWritable', ChapterWritableViewSet)
router.register(r'chaptersComplete', ChapterCompleteViewSet)
router.register(r'chaptersLookup', ChapterLookupViewSet)
  
router.register(r'sections', SectionViewSet)
router.register(r'sectionsWritable', SectionWritableViewSet)
router.register(r'sectionsComplete', SectionCompleteViewSet)
router.register(r'sectionsLookup', SectionLookupViewSet)
  
router.register(r'simpleCodes', SimpleCodeViewSet)
router.register(r'simpleCodesWritable', SimpleCodeWritableViewSet)
router.register(r'simpleCodesComplete', SimpleCodeCompleteViewSet)
router.register(r'simpleCodesLookup', SimpleCodeLookupViewSet)

    
