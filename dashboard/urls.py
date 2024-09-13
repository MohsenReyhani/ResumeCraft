from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    # Index
    path('', views.dashboard, name="dashboard"),
    # color pallete
    path('color-palette/', views.colorPalette, name="color_palette"),
    # sign up fill names
    path('fill-names/', views.fillNames, name="fill_names"),
    # Pages
    # path('dashboard/', views.dashboard, name="dashboard"),
    # Accounts
    path('accounts/', include('accounts.urls')),
    # Resume App
    path('resume/', include('resume.urls')),
   
    # update lists sorts order
    path('api/update-sort-order/', views.update_sorting_preferences, name="update_sort_order"),
    path('api/get-sort-order/', views.get_sorting_preferences, name="get_sort_order"),

    # # Tables
    # path('tables/bs-tables/', views.bs_tables, name="bs_tables"),

    # # Components
    # path('components/buttons/', views.buttons, name="buttons"),
    # path('components/notifications/', views.notifications, name="notifications"),
    # path('components/forms/', views.forms, name="forms"),
    # path('components/modals/', views.modals, name="modals"),
    # path('components/typography/', views.typography, name="typography"),

    # Errors
    path('error/404/', views.error_404, name="error_404"),
    path('error/500/', views.error_500, name="error_500"),

    # Extra
    path('pages/upgrade-to-pro/', views.upgrade_to_pro, name="upgrade_to_pro"),
]
