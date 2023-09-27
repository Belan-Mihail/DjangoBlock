# Create the view code, create the view  template, connect up our URLs file.
# So we've done the first two, but  now we need to wire up our URLs.  

from . import views
from django.urls import path

# This is similar to what you've done  before so "urlpatterns =", this is a list.
# So we'll supply our path, we're  then going to just supply a blank  
# path because that indicates that  it's our default, our home page.
# ("", views.PostList.as_view(), name="home"),
# Now this is similar to what you've done before,  but because we're using class-based views we need  
# to add the as_view method on the end of post list.  So it's going to render this class as a view.
# Now we just need to import these  URLs in our main Codestar URLs file.

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]