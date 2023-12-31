"""
URL configuration for aravena_edinson_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seminario import views

urlpatterns = [
    path('',views.index, name='index'),
    path('datosAutor/',views.datosAutor),
    path('formInst/', views.agregar_institucion),
    path('formInsc/',views.agregar_participante),
    path('inscrito_class/', views.InscritosList.as_view()),
    path('inscrito_class_deta/<int:id>',views.InscritosDetalle.as_view()),
    path('institucion_function/', views.instituciones_list),
    path('institucion_function_deta/<int:id>', views.instituciones_detalle),
    path('admin/', admin.site.urls),
]
