# Django Project Example

This represents my quick and easy Django project development template.  For those who are unfamiliar with Django, a good starting point is the [Official Django Tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/) and more specifically the section on [Creating A Project](https://docs.djangoproject.com/en/3.0/intro/tutorial01/#creating-a-project).

Making this code work requires some [Django web framework](https://www.djangoproject.com/) skills.

## Installation

This repository requires Python 3.6 (preferably Python 3.8) or newer and Django 3.0 or newer.


### Verify Installation

```powershell
PS C:\Users\human> python3.8 --version
Python 3.8.3
PS C:\Users\human>

PS C:\Users\human> python3.8
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'3.0.2'
>>> exit()
PS C:\Users\human>
```

## Setup Django Project

- Change directory to ```src/server```

- Edit ```server/settings.py``` to configure the database settings.

- Run ```python3.8 manage.py makemigrations```

- Run ```python3.8 manage.py migrate```

- Run ```python 3.8 manage.py migrate createsuperuser```



## Include Django Applications

- In ```settings.py```, Add Django applications (e.g. "django_file_system_searcher") at the end of the INSTALLED_APPS list:

  ```python
  INSTALLED_APPS = [
    ...
    ...
    "django_file_system_searcher",
  ]
  ```

- Include the application info to the project ```urls.py``` code.  For example,

  ```python
  path('file_system_searcher/', include('file_system_searcher.urls')),
  ```

- Run ```python3.8 manage.py makemigrations```

- Run ```python3.8 manage.py migrate```

- Start the development server ```python3.8 manage.py runserver``` and go to [http://127.0.0.1:8000/file_system_searcher].


  It works the same way with Linux and Mac.



