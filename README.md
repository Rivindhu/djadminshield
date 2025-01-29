# djadminshield

**djadminshield** is a Django library designed to secure your admin panel by creating fake login page and tracking unauthorized access attempts. Enhance your website's security and stay ahead of potential hackers!


---

## Features
* Fake admin login page that mimic the real admin login.
* Logs unauthorized login attempts with detailed information:
    * IP address, browser, OS, device type, and preferred languages.
    * A description of attempts, including warnings for guessed credentials.
* Protect your real admin panel with customizable login URLs. 

---


## Installation

Install the library by using pip:

```bash
pip install djadminshield
```


## Setup

1. **Add to Installed Apps**
    
    Add ```djadminshield``` to your ```INSTALLED_APPS``` in ```settings.py```: 

    ```python
    INSTALLED_APPS = [
        ...,
        'djadminshield',
    ]
    ```

2. **Apply Database Migrations**

    Run the following command to apply the necessary migrations:

    ```bash
    python manage.py migrate
    ```

3. **Create a Superuser**

    If you haven't already created a superuser, do so now:

    ```bash
    python manage.py createsuperuser
    ```

---

## Configuration

Update your project's ```urls.py``` file:

```python
from django.contrib import admin
from django.urls import include, path
from djadminshield import views

urlpatterns = [
    path('admin/', views.fake_admin_login, name='fake_admin_login'),
    path('real-admin-url/', admin.site.urls),
]
```

* Replace ```'real-admin-url/'``` with a unique and unguessable route for your actual admin login (e.g., ```'secure-admin-login/'```).

---


## How to test

1. Navigate to the ```/admin``` URL of your project.
    * You'll see a **fake admin login page** identical to the real one.
2. Attempt to login with invalid credentials.
    * These attempts will be logged and visible in the Django admin dashboard under the "**Unauthorized Access Attempts**" table in the "DJADMINSHIELD" section.
3. Check the logs for information such as:
    * IP address, attempt time, browser, OS, and description.
4. If someone successfully guess the credentials, the fake login page will still prevent access while login the activity.

---

## Example Use Case

* Use this library to monitor and analyze unauthorized login attempts.

* Identify potential threats based on logged data and take immediate actions, such as updating the passwords.

---

## GitHub Repository

Here is the [djadminshield GitHub Repository](https://github.com/Rivindhu/djadminshield). Feel free to check it out! 😊😊😊

If you find this library helpful, please consider giving the repository a ⭐ to show your support. Contribution and suggestions are always welcome--feel to raise issues or submit pull requests!

---

## Updates Log

* **v0.1.0** - Initial release with full functionality to secure Django admin dashboard.

* **v0.1.1** - Updated the README.md file with more accurate and easy to follow instructions.