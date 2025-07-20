import time

def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()  # process_request
        response = get_response(request, *args, **kwargs)
        end_time = time.time()  # process_response

        print(f"Request to {request.path} took {end_time - start_time:.4f} seconds.")

        return response

    return middleware