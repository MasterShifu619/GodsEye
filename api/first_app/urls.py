from django.conf.urls import url
from first_app import views

urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^upload_video/',views.showvideo,name='upload_video'),
    url(r'^preview_video/',views.VList,name='preview_video'),
    url(r'^generate_output/',views.Vout,name='gen_out'),
    url(r'^photogrid/',views.PhotoGrid,name='photo_grid'),
    url(r'^about/',views.about,name='about_us'),


]