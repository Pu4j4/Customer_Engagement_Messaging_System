from django.http import JsonResponse

def login_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.user:
            return JsonResponse({"error": "Authentication required"}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper