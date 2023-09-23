from django.contrib import admin
from .models import Post, Comment


#  Now all we need to do  
# is tell our admin panel which field  we want to use Summernote for.
# So basically we're going to  say that our content field  
# which is stored as a text field in the  database is going to be a Summernote field. 
# And this little piece of code in  our admin.py file will add it.
from django_summernote.admin import SummernoteModelAdmin

# And instead we're going to add  a decorator above our class. 
# Which is "@admin.register(Post)" 
# And this will register both our post model  and the post admin class with our admin site.
@admin.register(Post)
# And then we'll create a new class  we're going to call this PostAdmin.  
# That's going to inherit from  SummernoteModelAdmin that we've just imported.
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
#     When we enter the post title, we want the  slug field to be generated automatically.  
# To do that, we'll use the  prepopulated_fields property.  
# Which was specifically designed  for generating slug fields.
# It calls a bit of JavaScript that formats  and populates the slug field for us,   
# so that we don't have to worry about it. To  use it, we pass in a dictionary that maps  
# the field names to the fields that we want to  populate from. In our case, we want to populate  
# the slug field from the title field.
# This  will form part of our URL  
# so an individual blog posts URL will be  our project's base URL, plus this slug.
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
#     And then we're just going to say: "summernote_fields = ('content',)".
# So that's saying that our  content field, our blog content,  
# which we know is a Django text field,  we want to use summer note for this.


# admin.site.register(Post)
# We then need to register  post admin to our admin site. 
# Now instead of adding it to  this admin.site.register method,  
# I'm going to delete that line entirely.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')

#     So the last thing that I want to add here is an  action that allows us to approve the comment. 
# Now remember, that in our model the  approved field is set to false by default. 
# This ensures that all comments  need to be manually approved by an  
# admin before they appear on the site. 
# So now we want to add the  approval action to the admin site.
# To do this, we use another handy  built-in feature of the admin classes,  
# which is actions. The actions method allows you  
# to specify different actions that can be  performed from the action drop-down box.
# Now the default action is just  to delete the selected items  
# but we want to add an approved comment section  too
    actions = ['approve_comments']

#     Now as you remember, the approved field is a  boolean field that's set to false by default,  
# to approve the comment we just need to  set that field to true. So we'll add our  
# method called approve_comments which accept  self, request, and queryset as parameters.
# Don't worry about those too much, queryset is  the one that we'll use to update our record.  
# Our function then, is a one-liner we just  call the update method on the query set and  
# change our approved field to true and that's it! Our post admin and comments admin is now complete. 
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)