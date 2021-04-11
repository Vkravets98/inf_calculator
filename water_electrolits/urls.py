from django.urls import path
from water_electrolits.views import page, names, home_page, \
    do_logout, log, register, show_registration, enter_page, error, login_user, zadachi, obmen, uniq, test, currency, \
    photo, server, get_csv, onco_main

urlpatterns = [
    path('main_page', page),
    path('name_page', names),
    path('', home_page),
    path('onco_one', onco_main),
    path('enter_page', enter_page),
    path('error', error),
    path('enter', login_user),
    path('out', log),
    path('logout_btn', do_logout),
    path('show_form', register),
    path('reg', show_registration),
    path('zadan', zadachi),
    path('obmen', obmen),
    path('uniq', uniq),
    path('main_onc_page', test),
    path('exchange', currency),
    path('onco', photo),
    path('human', server),
    path('get_csv', get_csv),

]