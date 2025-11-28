# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.PrductListCreateAPIView.as_view()),              # POST, GET (list)
#     path('<int:pk>/', views.ProductDetailAPIView.as_view()),        # GET single
#     path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()), # PUT/PATCH
#     path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()), # DELETE
# ]


from django.urls import path
from . import views


urlpatterns = [
    path('',views.PrductListCreateAPIView.as_view()),
    path('<int:pk>/',views.PrductDetailAPIView.as_view()),
    path('<int:pk>/', views.ProductRetrieveUpdateDeleteAPIView.as_view()),
]


