from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
from .forms import LoginForm, CustomPasswordResetForm, CustomPasswordChangeForm
from .views import APP

app_name = 'coderunner'

# Authentication system URLs
urlpatterns = [
    path('accounts/login/',
         auth_views.LoginView.as_view(authentication_form=LoginForm,
                                      redirect_authenticated_user=True,
                                      extra_context={'app': APP,
                                                     'title': 'Sign in'}),
         name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/account_activation_sent/',
         views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/',
         views.activate, name='activate'),
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(extra_context={'app': APP})),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(extra_context={
                                                  'app': APP})),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             form_class=CustomPasswordResetForm, extra_context={
                 'app': APP})),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(extra_context={
                                                      'app': APP})),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(
             form_class=CustomPasswordChangeForm,
             extra_context={'app': APP})),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(extra_context={
                                                   'app': APP})),
]

urlpatterns = urlpatterns + [
    path('', views.index, name='index'),
]

# Enforce Login required on the below URLs
urlpatterns = urlpatterns + [
    path('home/', login_required(views.home), name='home'),
    path('details/<int:qid>/', login_required(views.details), name='details'),
    path('publish_question/', views.publish_question, name='publish_question'),
    path('publish_question/modify/<pk>/',
         views.ModifyQuestion.as_view(extra_context={'app': APP}),
         name='modify_question'),
    path('publish_question/delete/<pk>/',
         views.DeleteQuestion.as_view(extra_context={'app': APP}),
         name='delete_question'),
    path('program/<int:qid>/', login_required(views.program), name='program'),
    path('ajax/run_code/<int:qid>/',
         login_required(views.run_code), name='run_code'),
    path('ajax/validate_program/',
         login_required(views.validate_program), name='validate_program')
]
