from django.urls import path
from .views import index, contact, portfolio
# from django.conf.urls.static import static
# from django.conf import settings



urlpatterns = [
    path('', index, name='home' ),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio')
] 

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)