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
    description = models.TextField(blank=True, null=True)

    date = models.DateTimeField('Start Date', blank=False, null=False, db_index=True, auto_now_add=True)
    receipt_image = models.ImageField(blank=True, null=True, upload_to='expenses')

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Submitted')

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    @staticmethod
    def quick_create(title=None, description=None, user=1, project=1, receipt_image=None):

        if title is None:
            title = "An expense"

        if title is None:
            title = "lorum ipsum init"

        data = {
            "title": title,
            "description": description,
            "user": user,
            "project": project,
        }

        if receipt_image is not None:
            data.update({
                "receipt_image": receipt_image,
            })

        return Expense.objects.create(**data)

