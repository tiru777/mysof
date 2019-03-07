from django.db import models
from pygments.lexers import get_all_lexers,get_lexer_by_name
from pygments.styles import get_all_styles
#from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Sofmodel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TimeField()
    mobile_no = models.CharField(max_length=12)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    dob = models.DateField(max_length=12)
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)  # for creating user for authentication
    highlighted = models.TextField()


    #class Meta():
        #ordering = ('created_date',)



'''
def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.First_name)
    self.highlighted = highlight(self.dob, lexer)
    super(Sofmodel, self).save(*args, **kwargs)
'''

