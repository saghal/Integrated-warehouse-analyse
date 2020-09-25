from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from accounts.views import ContractListView, ContractUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newcontract/',accounts_views.newcontract, name='newcontract'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('contracts/<int:pk>/update', ContractUpdateView.as_view(), name='contract-update'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    path('', include('store.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
