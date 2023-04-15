from django.conf import settings

def tougblog(request):
    return {
        "tougblog": settings.TOUGBLOG
    }

