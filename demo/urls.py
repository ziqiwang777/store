from django.conf.urls import url
from . import table,test,index,index_eng, quality, company_introduction, contact_US, news_information, product_introduction, production_process
from . import product_detail1, product_detail2, product_detail3, product_detail4
from django.contrib import admin
from django.views import static
from django.conf import settings

urlpatterns = [
    url(r'admin_honghui/', admin.site.urls),
    url(r'test', test.test),

    url(r'index', index.index),
    url(r'^$', index.index),
    url(r'quality', quality.quality),
    url(r'submitsuccess', contact_US.submitsuccess),

    url(r'company_introduction', company_introduction.company_introduction),
    url(r'contact_US', contact_US.contact_US),
    url(r'news_information', news_information.news_information),
    url(r'product_introduction', product_introduction.product_introduction),
    url(r'production_process', production_process.production_process),
    url(r'product_detail1', product_detail1.product_detail1),
    url(r'product_detail2', product_detail2.product_detail2),
    url(r'product_detail3', product_detail3.product_detail3),
    url(r'product_detail4', product_detail4.product_detail4),

    url(r'cap_standards', table.cap_standards),

# ENGLISH
    url(r'eng_page', index_eng.index_eng),
    url(r'eng_qlti', quality.quality_eng),
    url(r'eng_ss', contact_US.submitsuccess_eng),
    #
    url(r'eng_aboutus', company_introduction.company_introduction_eng),
    url(r'eng_cs', contact_US.contact_US_eng),
    url(r'eng_pi', product_introduction.product_introduction_eng),
    url(r'eng_pp', production_process.production_process_eng),
    url(r'eng_pd1', product_detail1.eng_product_detail1),
    url(r'eng_pd2', product_detail2.eng_product_detail2),
    url(r'eng_pd3', product_detail3.eng_product_detail3),
    url(r'eng_pd4', product_detail4.eng_product_detail4),
    url(r'eng_capstandards', table.eng_cap_standards),

    # url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static'),


]
