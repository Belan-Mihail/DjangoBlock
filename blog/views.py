from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
#     now we can use more of the built-in methods  to quickly and easily render our list of posts.
# So we're going to supply the queryset here,  which will be the contents of our post table.  
# We're going to filter this by status. Remember  that our status field can be set to either 0  
# for draft, or one for published we want only  publish posts to be visible to the users,  
# so we'll filter our posts by status equals one.
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
#     Well list view provides a built-in  way to paginate the displayed list  
# and paginate just means separate into pages.  
# By setting paginate_by to six, we're limiting the  number of posts that can appear on the front page,  
# if there are more than six then Django  will automatically add page navigation.
    paginate_by = 6
