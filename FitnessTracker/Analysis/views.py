from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
from Analysis.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    
    # generate data to be loaded to each graph

    # queryset of all readings that are vo2 max
    vo2readings = Readings.objects.filter(metric__title="vo2_max").order_by('date')

    date_points = [reading.date.strftime("%Y-%m-%d") for reading in vo2readings]  # Format dates as strings
    quantities = [reading.quantity for reading in vo2readings]

    return render(request, "Analysis/index.html", {"date_data_points": date_points, "qty_data_points": quantities})

def receive_data(request):
    print("view has been triggered")
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            # Access the data fields
            metric_data = data.get('data', {}).get('metrics', [])

            for metric in metric_data:
                metric_name = metric_data.get('name')
                metric_units = metric_data.get('units')
                
                # check if metric already exists, else create one
                imported_metric, created = Metric.objects.get_or_create(title=metric, units=metric_units)
            
            dataset = metric_data.get('data', [])

            for reading in dataset:
                new_reading = Readings.objects.create(
                    metric=imported_metric,
                    date=reading.get('date'),
                    quantity=reading.get('qty'),
                    source=reading.get('source')
                    )    
                
                new_reading.save()

            return JsonResponse({'status': 'success', 'received_data': data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

class ReceiveDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Process the data from the request
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            # Access the data fields
            metric_data = data.get('data', {}).get('metrics', [])   # this = [
                                                                    #{"name" : "vo2_max",
                                                                    #"units" : "ml\/(kg·min)",
                                                                    # "data" : [
                                                                        #{"date": ....
                                                                        #},
                                                                        #{ ...},
                                                                        #..... 

            for metric in metric_data:
                metric_name = metric.get('name')
                metric_units = metric.get('units')
        
                # check if metric already exists, else create one
                imported_metric, metric_created = Metric.objects.get_or_create(title=metric_name, units=metric_units)
    
                dataset = metric_data[0].get('data', [])   # this = [{date:...}, {}]

                for reading in dataset:
                    new_reading, reading_created = Readings.objects.get_or_create(
                        metric=imported_metric,
                        date=reading.get('date'),
                        quantity=reading.get('qty'),
                        source=reading.get('source')
                    )
                    if reading_created:    
                        new_reading.save()

            return JsonResponse({'status': 'success', 'received_data': data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
        #return Response({"message": "Data received successfully through Class"})