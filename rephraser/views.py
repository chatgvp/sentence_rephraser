from django.http import JsonResponse
from django.shortcuts import render
import requests

from .serializer import ValueSerializer
from .models import Value, Dog

from rest_framework.decorators import api_view
from rest_framework.response import Response


# name = "cheetah"
# api_url = "https://api.api-ninjas.com/v1/animals?name={}".format(name)
# response = requests.get(
#     api_url, headers={"X-Api-Key": "fpv5vkEs8QSu3Axo0jj0rw==yrrXESw1tDzvXgtF"}
# )


# @api_view(["GET"])
# def display_api(request):
#     name = request.input
#     api_url = "https://api.api-ninjas.com/v1/animals?name={}".format(name)
#     response = requests.get(
#         api_url, headers={"X-Api-Key": "fpv5vkEs8QSu3Axo0jj0rw==yrrXESw1tDzvXgtF"}
#     )
#     return Response(response)


def home(request):
    return render(request, "homepage.html")


@api_view(["GET"])
def display_data(request):
    name = request.GET.get("inputValue")
    api_url = "https://api.api-ninjas.com/v1/logo?name={}".format(name)
    response = requests.get(
        api_url, headers={"X-Api-Key": "fpv5vkEs8QSu3Axo0jj0rw==yrrXESw1tDzvXgtF"}
    )
    if response.status_code == 200:
        data = response.json()
        return Response(data)
    else:
        return Response(
            {"error": "Failed to fetch data from the API"}, status=response.status_code
        )


@api_view(["GET"])
def display_values(request):
    values = Value.objects.all()
    serializer = ValueSerializer(values, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def rephrase(request):
    if request.method == "POST":
        sentence = request.data.get("value")
        # if sentence:
        #     url = (
        #         "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
        #     )
        #     payload = {"q": sentence}
        #     headers = {
        #         "content-type": "application/x-www-form-urlencoded",
        #         "Accept-Encoding": "application/gzip",
        #         "X-RapidAPI-Key": "ce13dcc549mshf02e78d7f36bc06p187f84jsn450a62612842",
        #         "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        #     }
        #     response = requests.post(url, data=payload, headers=headers)
        #     if response.status_code == 200:
        #         return Response(response.json())
        #     return Response(
        #         {"error": "Failed to fetch rephrased sentence"},
        #         status=response.status_code,
        #     )
        return Response({"error": "No sentence provided in the request"}, status=400)
    return Response({"error": "Invalid request method"}, status=405)
