__author__ = 'shahjalal'
from django.conf.urls import url, include
from home_app.views import HomePageView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home')

]
