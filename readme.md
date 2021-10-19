Pour que ca marche en production :
1. il faut ajouter un STATIC_ROOT = str(BASE_DIR) + '/static/' et commenter "STATICFILES_DIR
2. Mettre les bonnes configuration pour le serveur mail dans Porfolio/settings.py
3. Ajouter un curriculum vitae depuis le admin dashboard in the section files admin.
4. Insert your profile image on index.html line 55
5. superuser username : test@test.com. Password: portfolio_test
6.