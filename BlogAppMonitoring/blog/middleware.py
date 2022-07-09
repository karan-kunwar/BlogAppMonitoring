import time
from . import metrics

class StatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = (time.time() - start_time)*20
        
        print("Latency : ", duration, 's\n')
        metrics.custom_network_lateny.observe(duration)
        # Add the header. Or do other things, my use case is to send a monitoring metric
        response["X-Page-Generation-Duration-ms"] = duration 
        return response