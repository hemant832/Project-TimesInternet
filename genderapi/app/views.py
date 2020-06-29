from django.http import HttpResponse,JsonResponse
from returngender import returngender
from returnprobability import returnprobability
import pandas as pd
def home(request):
	return "Hello"
def genderapi(request):
	c=request.GET["name"]
	gender=returngender(c)
	probability=returnprobability(c)
	data = [{'Gender': gender},	{'Probability': probability}]
	return JsonResponse(data,safe=False)





