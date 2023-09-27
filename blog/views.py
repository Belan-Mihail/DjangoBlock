from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class PostDetail(View):
#     I'm sure you realize that, because we  want to get our blog post and display it  
# then we'll be using a GET method.
# So, let’s create a class method called get. Into  our class method, we're going to pass in self,  
# then request then slug, and the standard other  arguments and keyword arguments as parameters.    
    def get(self, request, slug, *args, **kwargs):

#         So, in our method let's get the post.
# First, we'll filter all of our posts so that we  only have the active ones with status set to one.
        queryset = Post.objects.filter(status=1)

#         And then, we'll get our published  post with the correct slug.
# By passing in our queryset to get_object_or_404,  and then with the arguments "slug = slug".
        post = get_object_or_404(queryset, slug=slug)

#         Now the post object contains most of the  helpful things that we're looking for.  
# So using this we can get any comments  that are attached to the post.
# So we'll type "comments =", we're  
# able to get the comments from our post, we'll  filter them to view only those that are approved.
# And we're going to order them this time  in ascending order, so that we have the  
# oldest comment first and we can actually view  this as a conversation.
        comments = post.comments.filter(approved=True).order_by("-created_on")

#         I also want to set a  
# boolean value to say whether our logged-in  user had liked this post or not. If we did,  
# we'll set the boolean to true, otherwise it  will remain false. So we'll say "liked = false"  
# and then we'll check with an if statement here, 
# to see if our post  
# when we filter it out if the user id is actually  there to say that they've liked the post.
# If they are, we'll set it to true,  otherwise it will remain false.
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
# Finally then, for this view, we can send all  of this information to our render method.  
# So we'll return render, we're  going to send a request through,  
# we're then going to supply the template  that we require post_detail.html.
# Then we'll create a dictionary here to supply  our context. So our post will be simply post,  
# our comments key will be the  comments that we got back, 
# and liked will be our liked boolean.
# Now we are going to add more to this view  a bit later but that will do for now.
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
