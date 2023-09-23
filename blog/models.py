from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
#  first of all we want to import the user model. So underneath the first import, we'll add 
# "from Django.contrib.auth.models import User". Then we want to import our Cloudinary field  
# for the featured image, so we'll  do that from Cloudinary models.

STATUS = ((0, "Draft"), (1, "Published"))
# Then we'll create a tuple for  our status which is going to  
# be a zero or a one for whether  the post is draft or published. 
# So "STATUS = " zero as draft and  then we'll have one as published.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
#     One is the "slug" field. Django is  betraying its roots in the publishing  
# industry here, because a slug in type  setting is an incidental line of type. 
# In Django, a slug is a label that  can be used as a part of a URL. 
# So we'll auto-generate a slug from the  title to use as our URL for each post,  
# and again this needs to be unique.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
#     Next, we'll do our author and remember that  we said that this needed to be a foreign key  
# relationship, it's a one-to-many  relationship from our user model.
# So that will be based on our user model,  we'll have on delete "models.cascade"  
# and we'll set a related name  which is going to be blog post.
# Now you might be wondering here what on earth is this "on_delete=models.CASCADE" that we have in our foreign key?
# Well it simply means that if the one record  
# in our one-to-many relationship is deleted,  then the related records will be deleted too.
# In other words, if we delete our user  we'll also delete their blog posts.
    featured_image = CloudinaryField('image', default='placeholder')
#     We give it a type, which is image. And we'll  also set a placeholder here which is just  
# going to be set to placeholder, we'll come  to that when we get into doing our templates.
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
#     The choices are going to be our  status that we created above  
# and the default is going to be  zero so the default will be draft.
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
#     And then finally we have our likes. Which as we  said is a many-to-many field, this is also going  
# to pull from our user. Related name is going  to be blog likes and it can also be blank.


    class Meta:
        ordering = ["-created_on"]
# Now we'll just add a couple of extra methods  to our model which can be viewed as helpers.  
# We're going to add the meta class, you can check  the Django documentation for all of these options  
# but the ones that I've used most often are to  do here with ordering, indexing and constraints.
# In this instance, we're going to order  our posts on the created_on field,  
# now the minus sign means to use descending order.

    def __str__(self):
        return self.title
#     Then we're going to use this string method  here, it's good practice to put that into your projects.
# The Django documentation says it's a  magic method that returns a string representation  
# of an object and it says you should define  it because the default isn't helpful at all.

    def number_of_likes(self):
        return self.likes.count()
# Finally, we have a helper method to return  the total number of likes on a post.


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
