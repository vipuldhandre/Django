from django.urls import path
from testapp.views import login,dict,list,dict2dict,list2dict,list2list,tupleintuple,setinset,date


urlpatterns = [
    path('login/',login),
    path('dict/',dict),
    path('list/',list),
    path('dict2dict/',dict2dict),
    path('list2dict/',list2dict),
    path('list2list/',list2list),
    path('tupleintuple/',tupleintuple),
    path('setinset/',setinset),
    path('datetime/',date),


]
