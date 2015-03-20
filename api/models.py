from django.db import models


STATUS_CHOICES = (
    ('Submitted', 'Submitted'), #when a user submits the expense
    ('Approved', 'Approved'), #when a manager approves the hours
    ('Declined', 'Declined'), #when a manager declines the hours    
)

class Expense(models.Model):

    def __unicode__(self):
        return self.title 
    
    user = models.CharField(max_length=200, db_index=True) 
    project = models.CharField(max_length=200, db_index=True, blank=False, null=False, default=None)   

    title = models.CharField(max_length=100)
    description = models.TextField()

    date = models.DateTimeField('Start Date', blank=False, null=False, db_index=True)
    receipt_image = models.ImageField(blank=True, null=True)

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Submitted')

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

