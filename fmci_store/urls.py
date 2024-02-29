from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import err400, err403, err404, err405,  err500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('space/', include('space.urls')),
    path('service/', include('service.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error views
handler400 = 'fmci_store.views.err400'
handler403 = 'fmci_store.views.err403'
handler404 = 'fmci_store.views.err404'
handler405 = 'fmci_store.views.err405'
handler500 = 'fmci_store.views.err500'