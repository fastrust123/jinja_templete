from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from myapp import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^httpresponse$', views.simple_httpresponse, name='httpresponse'),
#     url(r'^streaminghttpresponse$', views.simple_streaminghttpresponse, name='streaminghttpresponse$'),
#     url(r'^jinja$', views.streaminghttpresponse_with_jinja, name='streaming_with_jinja$'),
#     url(r'^naive$', views.naive_template_implementation_with_streaminghttpresponse, name='test$'),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ad-add-official$', views.simple_ad_add_official, name='ad-add-official'),
	url(r'^ad-add-organisation$', views.simple_ad_add_organisation, name='ad-add-organisation'),
	url(r'^ad-ap-revise-user$', views.simple_ad_ap_revise_user, name='ad-ap-revise-user'),
	url(r'^ad-change-password$', views.simple_ad_change_password, name='ad-change-password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)