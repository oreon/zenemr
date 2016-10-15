
from rest_framework import viewsets
from .serializers import *
    
class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    
class CodeLookupViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeLookupSerializer
    
class CodeCompleteViewSet(CodeViewSet):
    serializer_class = FullCodeSerializer
    
class CodeWritableViewSet(CodeViewSet):
    serializer_class = CodeWritableSerializer    

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    
class ChapterLookupViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterLookupSerializer
    
class ChapterCompleteViewSet(ChapterViewSet):
    serializer_class = FullChapterSerializer
    
class ChapterWritableViewSet(ChapterViewSet):
    serializer_class = ChapterWritableSerializer    

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    
class SectionLookupViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionLookupSerializer
    
class SectionCompleteViewSet(SectionViewSet):
    serializer_class = FullSectionSerializer
    
class SectionWritableViewSet(SectionViewSet):
    serializer_class = SectionWritableSerializer    

class SimpleCodeViewSet(viewsets.ModelViewSet):
    queryset = SimpleCode.objects.all()
    serializer_class = SimpleCodeSerializer
    
class SimpleCodeLookupViewSet(viewsets.ModelViewSet):
    queryset = SimpleCode.objects.all()
    serializer_class = SimpleCodeLookupSerializer
    
class SimpleCodeCompleteViewSet(SimpleCodeViewSet):
    serializer_class = FullSimpleCodeSerializer
    
class SimpleCodeWritableViewSet(SimpleCodeViewSet):
    serializer_class = SimpleCodeWritableSerializer    

  