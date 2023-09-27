"""codestar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    # add path to the blog urls
    path("", include("blog.urls"), name="blog-urls"),

    path("accounts/", include("allauth.urls")),
#     when that's installed update your  requirements.txt file before we forget
# now we need to add our all auth urls to our main  urls.py file so under the codestar directory
# open our urls.py file and then we'll add a line  inside our url patterns list and this is very
# similar to what we've already done before  we're going to provide the path to accounts
# so this will be our url and then we're  going to include the all auth urls
]
