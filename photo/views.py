from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from base64 import b64encode


def home_page(request):

    return render(request, template_name="upload.html")


@csrf_exempt
def response_page(request):
    inImg = request.FILES["pic"].read()

    encoded = b64encode(inImg)
    print(encoded)

    return render(request, "response.html", {'img': str(encoded)[2:-1]})
