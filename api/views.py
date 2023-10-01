from django.shortcuts import render

# from transformers import AutoTokenizer, pipeline
# import torch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from generator import generate_response

# Define a Django view to handle POST requests
@csrf_exempt
def handle_query(request):
    if request.method == 'POST':
        try:
            # Decode the request body as JSON
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            # Extract the "query" value from the JSON data
            query = data.get('query', '')
            # print(query)
            # Process the query and generate a response (you can replace this logic)
            
            response = generate_response(query)
            
            # response = "please try again"

            # Return the response as JSON
            return JsonResponse({'reply': response})
        except Exception as e:
            return JsonResponse({'error': 'Invalid request'}, status=400)
    else:
        return HttpResponse(status=405)  # Method not allowed



