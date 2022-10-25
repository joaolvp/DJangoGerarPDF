from django.urls import path
from .views import *

urlpatterns = [
    path('', ListarFuncionariosListView.as_view(),
         name='Listar_func'),
    path('listafuncpdf/', ListaFuncPdfView.as_view(),
         name='Listar_func_pdf'),
    path('listadeptpdf/', ListaDepartPdfView.as_view(),
         name='Listar_dept_pdf'),
]