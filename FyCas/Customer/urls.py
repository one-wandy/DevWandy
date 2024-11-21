from django.contrib import admin
from django.urls import path, include
from . import views, views_ajax

app_name = "customer"
urlpatterns = [
      path("", views.Dashboard.as_view(), name='dashboard'),
      path('add-customer/<int:pk>', views.AddCustomer.as_view(), name='add-customer'),
      path('detail-customer/<int:pk>', views.DetailCustomer.as_view(), name='detail-customer'),
      path('update-customer/<int:pk>', views.UpdateCustomer.as_view(), name='update-customer'),
      
      path('delete-customer/<int:pk>', views.DeleteCustomer.as_view(), name='delete-customer'),

      path('list-customer', views.ListCustomer.as_view(), name='list-customer'),
      path('card-customer/<int:pk>/<int:credit_id>', views.CardCustomer.as_view(), name='card-customer'),
      path('notary-customer/<int:pk>/<int:notary_id>', views.NotaryCustomer.as_view(), name='notary-customer'),
      
      path('create-credit/<int:pk>', views.CreateCredit.as_view(), name='create-credit'),
      path('update-credit/<int:pk>', views.UpdateCredit.as_view(), name='update-credit'),
      path('list-credit/<int:pk>', views.ListCredit.as_view(), name='list-credit'),

      path('create-credit-new/<int:pk>', views.CreateCreditNew.as_view(), name='create-credit-new'),

      path('calendario/', views.Calendario.as_view(), name='calendario'),

      path('configuraciones/', views.Configuraciones.as_view(), name='configuraciones'),

      path("detail-credit/customer/<int:pk>", views.DetailCreditCustomer.as_view(), name="detail-credit-cutomer"),

      path("no-approved/customer", views.NoApproved.as_view(), name='no-approved'),
      path("approved/customer/<int:pk>", views.Approved.as_view(), name='approved'),
      
      path("create/customer-debit", views.CreateCustomerDebit.as_view(), name='create-customer-debit'),
      path("mensaje/customer-debit", views.MensajeCustomerDebit.as_view(), name='mensaje-customer-debit'),

      path("select/customer", views.ListCustomerSelect.as_view(), name='select-customer'),
      
      path("customer-profile", views.CustomerProfile.as_view(), name='customer-profile'),
      path('mensajeria', views.Mensensajeria.as_view(), name='mensajeria'),

      path("prestamos", views.Prestamos.as_view(), name='prestamos'),
      
      path('ubicaciones', views.Ubicaciones.as_view(), name='ubicaciones'),
      path('agregar/<int:pk>', views.Agregar.as_view(), name='agregar'),

      path('listado-credit-redirect/<int:pk>', views.ListadoCredit_rederict.as_view(), name='listado-credit-redirect'),

      path('empresa', views.Empresa.as_view(), name='empresa'),
      path('calculadora', views.Calculadora.as_view(), name='calculadora'),

      # New Version
      path('crear-credito/<int:pk>', views.CrearCredito.as_view(), name='crear-credito'),
      path('list-all-credits', views.ListAllCredits.as_view(), name='list-all-credits'),

      path('search-company', views.SearchCompany.as_view(), name='search-company'),




      # Views Ajax``
      path('aplicar-pago', views_ajax.AplicarPago, name='aplicar-pago'),
      path("searching/customer", views_ajax.SearchCustomer, name="searching-customer"),
      path("verify/customer/", views_ajax.CustomerVerify, name="verify-true-customer"),
      path("verify-no/customer/", views_ajax.CustomerNoVerify, name="verify-false-customer"),
      path('calcular-mora', views_ajax.CalcularMora, name='calcular-mora'),
      path("turn-debit/customer/", views_ajax.TurnDebeit, name="turn-debit-customer"),
      path("turn-debit-follow/customer/", views_ajax.TurnDebeitFollow, name="turn-debit-customer-follow"),
      path("turn-debit-active/customer/", views_ajax.TurnDebeitActive, name="turn-debit-customer-active"),
      path("msg/customer/debit", views_ajax.MensajeCustomerDebit, name="msg-debit-customer"),
      path("create-credit-ajax/customer/", views_ajax.CreateCreditAjax, name="create-credit-ajax"),
      path("disable-customer/", views_ajax.DisableCustomer, name="disable-customer-ajax"),
      path("delete-credit", views_ajax.DeleteCreditAjax, name="delete-credit"),
      path('upload-image-url', views_ajax.UploadImageURL, name='upload-image-url'),
      

      path('chatgpt', views_ajax.ChatGPT, name='chatgpt'),
      
]
