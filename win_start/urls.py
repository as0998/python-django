from django.urls import path
# from .views import RenderHTMLPlayer
from . import views
app_name="win_start"
urlpatterns = [
#    '20/dy/plc_red_01/<int:item_id1>/<int:item_id2><int:item_id3>/<str:id_str>'
    path("a/",views.main_a, name="main_a"),
    # path('plc/plc_red_01/<int:item_id1>/<int:item_id2>/<int:item_id3>/<str:id_str>', views.plc_red_01, name='plc_red_01'),
    # path("re/<str:maridb_ip>",views.re_updata, name="re_updata"),
    # path("li/<str:maridb_ip>",views.re_live, name="re_live"),
    # path("cctv/<int:cctv_name>/<str:net_name>",views.cctv, name="cctv"),
    # path('20/dy/plc_red_02/<int:item_id1>/<str:id_str1>/<str:id_str2>/<str:id_str3>', views.plc_red_02, name='plc_red_02')
]
