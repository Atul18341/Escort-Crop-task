from rest_framework.response import Response
from rest_framework.views import APIView
from googletrans import Translator
# Create your views here.
class Translation(APIView):
    def get(self,request):
        intext = request.data['text']
        s_lan_code=request.data['source_language_code']
        d_lan_code=request.data['destination_language_code']
        translator = Translator()
        translated = translator.translate(intext, src=s_lan_code, dest=d_lan_code)
        return Response(translated.text)