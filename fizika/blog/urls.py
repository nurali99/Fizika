from django.urls import path
from .views import KunYangiliklarDetailView, KunYangiliklarListView, MexanikaListView, MexanikaDetailView, MolekulyarListView, MolekulyarDetailView
from .views import ElektrostatikaListView, ElektrostatikaDetailView, OptikaListView, OptikaDetailView
from .views import AtomYadroListView, AtomYadroDetailView, MuallifListView, KitobListView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('Mexanika/<int:pk>/', MexanikaDetailView.as_view(), name='mex_detail'),
    path('Mexanika/', MexanikaListView.as_view(), name='mex'),
    path('Molekulyar/<int:pk>/', MolekulyarDetailView.as_view(), name='molekulyar_detail'),
    path("Molekulyar/", MolekulyarListView.as_view(), name="molekulyar"),
    path('Elektrostatika/<int:pk>/', ElektrostatikaDetailView.as_view(), name='elektrostatika_detail'),
    path('Elektrostatika/', ElektrostatikaListView.as_view(), name='elektrostatika'),
    path('Optika/<int:pk>/', OptikaDetailView.as_view(), name="optika_detail"),
    path('Optika/', OptikaListView.as_view(), name="optika"),
    path('AtomYadro/<int:pk>/', AtomYadroDetailView.as_view(), name='atomyadro_detail'),
    path('AtomYadro/', AtomYadroListView.as_view(), name="atomyadro"),
    path('Muallif/', MuallifListView.as_view(), name='muallif'),
    path('Kitoblar/', KitobListView.as_view(), name='kitob'),
    path('Kunyangiliklar/<int:pk>/', KunYangiliklarDetailView.as_view(), name='kunyangiliklar_detail'),
    path('Kunyangiliklar/', KunYangiliklarListView.as_view(), name='kunyangiliklar'),
    # path('Kunyangiliklar/new/', KunYangiliklarCreateView.as_view(), name='post_new')
]
