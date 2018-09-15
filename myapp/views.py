import os
import time


from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.template import Context, loader
from jinja2 import Environment, FileSystemLoader
from itertools import chain


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESS_TIME = 5


def index(request):

    return render(request, 'jinja2/index.html')

def simple_ad_add_official(request):

    return render(request, 'jinja2/ad-add-official.html')

def simple_ad_add_organisation(request):

    return render(request, 'jinja2/ad-add-organisation.html')

def simple_ad_ap_revise_user(request):

    return render(request, 'jinja2/ad-ap-revise-user.html')

def simple_ad_change_password(request):

    return render(request, 'jinja2/ad-change-password.html')

def simple_of1_change_password(request):

    return render(request, 'jinja2/of1-change-password.html')
    
def simple_of1_revise_luth_member(request):

    return render(request, 'jinja2/of1-revise-luth-member.html')

def simple_of2_add_drug(request):

    return render(request, 'jinja2/of2-add-drug.html')

def simple_of2_change_password(request):

    return render(request, 'jinja2/of2-change-password.html')

def simple_of2_revise_banner_drug(request):

    return render(request, 'jinja2/of2-revise-banner-drug.html')

def simple_of3_add_patient(request):

    return render(request, 'jinja2/of3-add-patient.html')

def simple_of3_change_password(request):

    return render(request, 'jinja2/of3-change-password.html')

def simple_ph_add_patient(request):

    return render(request, 'jinja2/ph-add-patient.html')

def simple_ph_change_password(request):

    return render(request, 'jinja2/ph-change-password.html')

def simple_phm_add_affiliate(request):

    return render(request, 'jinja2/phm-add-affiliate.html')

def simple_phm_administer_prescription(request):

    return render(request, 'jinja2/phm-administer-prescription.html')

def simple_hphm_affiliate_list(request):

    return render(request, 'jinja2/phm-affiliate-list.html')

def simple_ph_make_prescription(request):

    return render(request, 'jinja2/ph-make-prescription.html')

def simple_phm_change_password(request):

    return render(request, 'jinja2/phm-change-password.html')

def simple_phm_verify_prescription(request):

    return render(request, 'jinja2/phm-verify-prescription.html')

def simple_ph_request_permission(request):

    return render(request, 'jinja2/ph-request-permission.html')

def simple_ph_view_description(request):

    return render(request, 'jinja2/ph-view-description.html')

# def simple_httpresponse(request):

#     context = get_sample_context()

#     return render(request, 'jinja2/index.html', context)


# def get_sample_context():

#     long_response = simulate_long_response_with_delay()
#     mystring = 'I am a string stored in the context dict'
#     context = {'mylist': [1, 2, 3, 4, 5], 'mystring': mystring, 'mylongresponse': long_response}

#     return context

# def simple_streaminghttpresponse(request):

#     context = get_sample_context()
#     title = '<h1>2) StreamingHttResponse() without a template </h1>'
#     description = '<p>StreamingHttpResponse() is used to stream a response from Django to the browser.<br/>' \
#                   'The user will see the context elements as they are processed.<br/>' \
#                   'Unfortunately, you cannot use templates by default, which means that its use is limited ' \
#                   'to specific use cases, such as rendering big csv files.<br/>' \
#                   'If I pass the context to the stream chain, it will be processed without formatting,' \
#                   'and without taking into account variables and loops inside the template, like this: </p>'
#     navigation_menu = '''<ol type="1">
#         <li><a href="httpresponse">Problem: rendering delay with HttpResponse()</a></li>
#         <li><a href="streaminghttpresponse">render page with StreamingHttpresponse()</a></li>
#         <li><a href="naive">try to add templates to StreamingHttpresponse()</a></li>
#         <li><a href="jinja">Solution: render page with StreamingHttpresponse() combined with jinja.generate()</a></li>
#         </ol>'''
#     stream = chain(navigation_menu, title, description, context, simulate_long_response_with_delay())

#     return StreamingHttpResponse(stream)


# def naive_template_implementation_with_streaminghttpresponse(request):

#     template = loader.get_template('jinja2/naive.html')
#     context = Context(get_sample_context()).flatten()
#     stream = template.render(context)

#     return StreamingHttpResponse(stream)

# def streaminghttpresponse_with_jinja(request):

#     template = 'jinja2/streaming_with_jinja.html'
#     context = get_sample_context()
#     stream = jinja_generate_with_template(template, context)
#     return StreamingHttpResponse(stream)

# def jinja_generate_with_template(template, context):

#     template_dir = THIS_DIR + '/templates/'
#     j2_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)

#     return j2_env.get_template(template).generate(context)


# def simulate_long_response_with_delay():

#     for i in range(PROCESS_TIME):
#         time.sleep(1)
#         yield 'This request is taking a while... still {} seconds to go'.format(PROCESS_TIME - i)

