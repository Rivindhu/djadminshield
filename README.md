# djadminshield

A Django library to secure the admin panel by faking login pages and logging attempts.

## Installation

```bash
pip install djadminshield
```

## Usage
Migrate the database by executing the django migrate command.

```bash
python manage.py migrate
```

If you didn't create your superuser please create the superuser.

```bash
python manage.py createsuperuser
```

Installed the library in the settings.py file

```python
INSTALLED_APPS = [
    .....,
    'djadminshield',
]
```

Now go to the project directory urls.py file and add the below code.

```python
from django.contrib import admin
from django.urls import include, path
from djadminshield import views

urlpatterns = [
    path('admin/', views.fake_admin_login, name='fake_admin_login'),
    path('real-admin-url/', admin.site.urls),
]
```

In above code we import the views from the djadminshield library so we can use the 
djadminshield view functions. 

Then we added the fake admin login page to the 'admin/' url route. You can see we using the 
djadminshield fake_admin_login function to render the fake admin login pages.

second url route is for the actual admin user login page, for demonstration purposes we named 
it as 'real-admin-url/' but you can give what ever you want. Please make sure to the given url route is not guessable by hackers.


## How to try

Then you can this by directing to the admin URL like www.example.com/admin  then this will directed to the fake admin dashboard login page. This login page is exactly same as the real django admin login page.

If someone trying to login as admin those attempt will be recorded and website real admin user can see them by simply going to the admin dashboard. In the Django admin dashboard, under the “DJADMINSHIELD” there’s a table called “Unauthorized Access Attempts”. In there by using that table you can get information such as ip address, attempt time, browser, operating system, device type, prefer languages by unauthorized hacker, and a description. This description might be helpful because let’s say a hacker successfully find the username and password and trying to login to the dashboard via the fake login page that action is captured and this description is showing to the real admin user someone is somehow get the real username and password. Then the real admin can update the password immediately. Even if hacker guess or get the real username and password the fake login page might not be log them in instead it showing the same error that password and username is not correct. 