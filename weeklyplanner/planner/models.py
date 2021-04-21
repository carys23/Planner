from django.db import models
import datetime
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    # start_time = models.DateTimeField(default=datetime.date.today)
    day = models.DateField()
    
    
    def __str__(self):
        return self.title
        @property
        def get_html_url(self):
            url = reverse('event_edit', args=(self.id,))
            return f'<p>{self.title}</p><a href="{url}">edit</a>'