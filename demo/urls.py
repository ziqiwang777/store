from django.conf.urls import url
from . import test,index, quality, company_introduction, contact_US, news_information, product_introduction, production_process
from . import product_detail1, product_detail2, product_detail3, product_detail4
from django.contrib import admin


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
    url(r'product_detail4', product_detail4.product_detail4)
]
