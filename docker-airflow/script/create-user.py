import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

# Create Airflow User
user = PasswordUser(models.User())
user.username = 'airflowadmin'
user.email = 'rupesh.chaudhari@investors.com1'
user.password = 'airflowadmin'.encode('utf8')
user.superuser = True
session = settings.Session()
session.add(user)
session.commit()
session.close()
print('New User Created')