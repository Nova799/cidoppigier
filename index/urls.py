from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/<user_idf>/', views.logout, name='logout'),
    path('firstLogin/<user_idf>/', views.firstConn, name='firstLogin'),
    path('Accueil/<user_idf>/', views.home, name='home'),
    path('A_propos/<user_idf>/', views.about, name='about'),
    path('Recommandations/<user_idf>/', views.recommandations, name='recommandations'),
    path('Preferences/<user_idf>/', views.preferences, name='preferences'),
    path('AllDocs/<user_idf>/', views.all_docs, name='all_docs'),
    path('DocInfo/<user_idf>/<doc_idfy>/', views.doc_info, name='doc_info'),
    path('ReadDoc/<user_idf>/<doc_idfy>', views.read_doc, name='read_doc'),
    path('Admin/<user_idf>/Utilisateurs/', views.adm_users, name='adm_users'),
    path('Admin/<user_idf>/Documents/', views.adm_docs, name='docs_index'),
    path('Admin/<user_idf>/Diagnostics/', views.diagnostics, name='diagnostics'),
    path('Admin/<user_idf>/Emprunts/', views.adm_emp, name='emp_index'),
    path('Emprunts/<user_idf>/Acte/<emp_idfy>/', views.acte_emp, name='acte_emp'),
    path('Emprunts/<user_idf>/Facture/<emp_idfy>/', views.facture, name='facture'),
    path('Admin/<user_idf>/Utilisateurs/Modifications/<idfy_user>/', views.adm_users_modify, name='adm_users_modify'),
    path('Admin/<user_idf>/Utilisateurs/Suppressions/<idfy_user>/', views.adm_users_del, name='adm_users_del'),
    path('Admin/<user_idf>/Rechercher/<searchGroup>/', views.search, name='search'),
    path('Accueil/<user_idf>/recents/', views.recents, name='recents'),
    path('Admin/<user_idf>/delete/<searchGroup>/<target>/', views.delete_target, name='delete_target'),
    path('Admin/<user_idf>/<searchGroup>/Modify/<target>/', views.modify_target, name='modify_target'),
    path('Admin/<user_idf>/Emprunts/renew/<emp_idfy>/', views.renew, name='renew'),
    path('Admin/<user_idf>/Emprunts/fresh/<emp_idfy>/', views.fresh, name='fresh'),
    path('mdpForgot/', views.mdpForgot, name="mdpForgot"),
    path('fake_page/<user_idf>/<target>', views.fake_page, name="fake_page"),
    path('MostEvaluated/<user_idf>/', views.most_noted, name="most_noted"),
    path('Admin/<user_idf>/ImportData/<import_group>/', views.import_data, name="import_data"),
    path('Admin/<user_idf>/ExportData/<export_group>/', views.export_data, name="export_data"),

    ## Les URLs API
    # 
    path('API/login/', views.api_login, name='api_login'),
    path('API/AllDocs/<user_idf>/', views.api_all_docs, name='api_all_docs'),
    path('API/RecentsDocs/<user_idf>/', views.api_recents_docs, name='api_recents_docs'),
    path('API/MostNoted/<user_idf>/', views.api_most_noted, name='api_most_noted'),
    path('API/Recom/<user_idf>/', views.api_recom, name='api_recom'),
    path('API/MdpForgot/', views.api_mdpForgot, name='api_mdpForgot'),
    path('API/AppDoc/<user_idf>/', views.api_appreciate_doc, name='api_appreciate_doc'),
    path('API/FirstConn/<user_idf>/', views.api_firstConn, name='api_firstConn'),
]
