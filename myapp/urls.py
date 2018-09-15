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
	url(r'^of1-change-password$', views.simple_of1_change_password, name='of1-change-password'),
	url(r'^of1-revise-luth-member$', views.simple_of1_revise_luth_member, name='of1-revise-luth-member'),
	url(r'^of2-add-drug$', views.simple_of2_add_drug, name='of2-add-drug'),
	url(r'^of2-change-password$', views.simple_of2_change_password, name='of2-change-password'),
	url(r'^of2-revise-banner-drug$', views.simple_of2_revise_banner_drug, name='of2-revise-banner-drug'),
	url(r'^of3-add-patient$', views.simple_of3_add_patient, name='of3-add-patient'),
	url(r'^of3-change-password$', views.simple_of3_change_password, name='of3-change-password'),
	url(r'^ph-add-patient$', views.simple_ph_add_patient, name='ph-add-patient'),
	url(r'^ph-change-password$', views.simple_ph_change_password, name='ph-change-password'),
	url(r'^phm-add-affiliate$', views.simple_phm_add_affiliate, name='phm-add-affiliate'),
	url(r'^phm-administer-prescription$', views.simple_phm_administer_prescription, name='phm-administer-prescription'),
	url(r'^phm-affiliate-list$', views.simple_hphm_affiliate_list, name='phm-affiliate-list'),
	url(r'^ph-make-prescription$', views.simple_ph_make_prescription, name='ph-make-prescription'),
	url(r'^phm-change-password$', views.simple_phm_change_password, name='phm-change-password'),
	url(r'^phm-verify-prescription$', views.simple_phm_verify_prescription, name='phm-verify-prescription'),
	url(r'^ph-request-permission$', views.simple_ph_request_permission, name='ph-request-permission'),
	url(r'^ph-view-description$', views.simple_ph_view_description, name='ph-view-description'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)