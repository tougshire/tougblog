from django.db import models
from datetime import date
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse

class Image(models.Model):
    title = models.CharField(
        'Title',
        max_length=50,
        help_text="The title of the thread"
    )
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="The user who created ths thread"
    )
    created=models.DateTimeField(
        'created',
        auto_now_add=True,
        help_text="The date/time this therad was created"
    )
    file = models.ImageField(
        upload_to='gallery/'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class Placement(models.Model):
    title=models.CharField(
        'title',
        max_length=20,
        blank=True,
        help_text='The title to be displayed for this placement'
    )
    list_order = models.CharField(
        max_length=1,
        blank=True,
        default='~',
        help_text="A character to determine the place on the list. Numbers are higher than capital letters, which are higher than small letters"
    )
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('list_order', 'title',)
    
class Post(models.Model):
    title = models.CharField(
        'Title',
        max_length=50,
        help_text="The title of the thread"
    )
    title_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='The image to display above the title, and to use for social media graphs'
    )
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The user who created ths thread"
    )
    show_author_flag = models.BooleanField(
        'show_author',
        default=True,
        help_text="Flag indicating if the author should be shown.  This is just a flag - the template has to be coded appropriately for this to work"
    )
    created=models.DateTimeField(
        'created',
        auto_now_add=True,
        help_text="The date/time this therad was created"
    )
    show_created_flag = models.BooleanField(
        'show_created',
        default=True,
        help_text="Flag indicating if the creation date should be shown.  This is just a flag - the template has to be coded appropriately for this to work"
    )
    placement=models.ForeignKey(
        Placement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The place on the home page"
    )
    content_format = models.CharField(
        'content format',
        max_length=20,
        choices=(
            ('markdown', 'markdown'),
            ('html','html'),
        ),
        default='markdown',
        help_text="The format (or markup method) used for the content"
    )
    content = models.TextField(
        "content",
        blank=True,
        help_text="The content of the post"
    )
    summary_format = models.CharField(
        'summary format',
        max_length=20,
        choices=(
            ('same', 'same as content'),
            ('markdown', 'markdown'),
            ('html','html'),
        ),
        default='same',
        help_text="The format (or markup method) used for the summary"
    )
    summary = models.TextField(
        "summary",
        blank=True,
        help_text="A shorter version of the content"
    )
    list_order = models.CharField(
        max_length=1,
        blank=True,
        default='~',
        help_text="A character to determine the place on the list. Numbers are higher than capital letters, which are higher than small letters"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('list_order', '-created',)

    
class Event(models.Model):
    title = models.CharField(
        'title',
        max_length=50,
        help_text="The title of the thread"
    )
    title_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='The image to display above the title, and to use for social media graphs'
    )
    starttime = models.TimeField(
        'starting',
        blank=True,
        null=True,
        help_text='The start time of the event'
    )
    lenmin = models.IntegerField(
        'length(minutes)',
        blank=True,
        default=0,
        help_text='How long the event lasts (0 indicates indefinite or unkown)'
    )
    content_format = models.CharField(
        'content format',
        max_length=20,
        choices=(
            ('markdown', 'markdown'),
            ('html','html'),
        ),
        default='markdown',
        help_text="The format (or markup method) used for the content"
    )
    content = models.TextField(
        "content",
        blank=True,
        help_text="The content of the post"
    )
    summary_format = models.CharField(
        'content format',
        max_length=20,
        choices=(
            ('same', 'same as content'),
            ('markdown', 'markdown'),
            ('html','html'),
        ),
        default='same',
        help_text="The format (or markup method) used for the summary"
    )
    summary = models.TextField(
        "summary",
        blank=True,
        help_text="A shorter version of the content"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text = 'The post to use as the content and summary.  If selected, the post content and summary will be used instead of the event\'s content and summary'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering=['starttime', 'lenmin']    

class EventDate(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        help_text="The event to which this date belongs"
    )
    whenday = models.DateField(
        'date',
        help_text="The date of the event"
    )

    def __str__(self):
        return '{} -> {}'.format(self.event, self.whenday)

    class Meta:
        ordering = ('whenday','event')

class Page(models.Model):
    title = models.CharField(
        'Title',
        max_length=50,
        help_text="The title of the thread"
    )
    title_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='The image to display above the title, and to use for social media graphs'
    )
    slug = models.SlugField(
        unique=True,
        help_text="The code that provides a character based ID for this page"
    )
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The user who created ths thread"
    )
    created=models.DateTimeField(
        'created',
        auto_now_add=True,
        help_text="The date/time this therad was created"
    )
    content_format = models.CharField(
        'content format',
        max_length=20,
        choices=(
            ('markdown', 'markdown'),
            ('html','html'),
        ),
        default='markdown',
        help_text="The format (or markup method) used for the content"
    )
    content = models.TextField(
        "content",
        blank=True,
        help_text="The content of the post"
    )
    list_order = models.CharField(
        max_length=1,
        blank=True,
        default='~',
        help_text="A character to determine the place on the list. Numbers are higher than capital letters, which are higher than small letters"
    )
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse("page_detail", kwargs={"slug": self.slug}) 
    
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.name)
        super().save(*args, **kwargs) 

    class Meta:
        ordering = ('list_order', '-created',)

