from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

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
                "liked": liked,
                "comment_form": CommentForm(),
#                 So with the form imported, we now  need to render it as part of our view.
# To do this, we can simply add it to our context.
# So just under liked in our render method,  we're going to supply a new key comment_form.  
# And the value will just be the comment  form that we imported just now.
            },
        )



# So what we're going to do is add a post method to  our PostDetail class back in our views.py file.
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
# When that's done, we need to get the  data from our form and assign it to a variable.
# So I'm going to create a  new variable here called comment_form.
# And that's the value is going to be set to:
# comment_form = CommentForm(data=request.POST)
# So this will get all of the data  that we posted from our form.

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
# Now our form has a method called is  valid that returns a Boolean value  
# regarding whether the form is valid, as in  all the fields have been completed or not. 
# If it is valid, a comment has been  left and we want to process it. 
# So let's get that: if comment_form.is_valid():
# And what we're going to do is  set our email and our username  
# automatically from the logged in user.
# This is conveniently passed in as part  
# of the request so that we can  get those details from there.
# So we'll set the email to the request.user email.
# We'll set the instance name  to the request username.
# And then, we're going to call  the save method on our form  
# but we're not actually going to  commit it to the database yet.
# The reason is that we want to first assign a  post to it. So comment.post equals our post instance,  
# so that we know which post a comment has  been left on and then we can save it.
# We'll add an else clause here as  well, because if the form is not valid  
# then we just want to return an  empty comment form instance. So:
# else: comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,

                "commented": True,
#                 Okay, so now we just need  to adjust our render method.
# And what we're going to do is  set a commented value to True.

                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    def post(self, request, slug):
        # So first, let's get the relevant  post using our get_object_or_404 method.
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
#         Then, we'll toggle the state.
# We'll use an if statement to check if our post is  already liked and if it is we'll remove the like.
# So remember how we checked if a  post was already liked before?
# We used an if statement, we filtered  our post.likes on the user ID  
# and if the user ID exists, then  it's been liked, so we can remove it.


        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
#         Now we need to reload our post_detail  template so that we can see the results.
# To do this, we'll use a new response  type called HttpResponseRedirect.  
# So let's go up to the top of our views.py  file and import this from django.http.
# So: from django.http import HttpResponseRedirect