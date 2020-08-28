from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from twilio.rest import Client


# Create your models here.
class SendSms(models.Model):
    date_paid = models.DateField("date_paid(mm/dd/yy)", auto_now_add=False, auto_now=False, blank=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    address = models.TextField(null=True, blank=True)
    suite_number = models.IntegerField()
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.date_paid)

    def save(self, *args, **kwargs):
        if self.date_paid is True:
            account_sid = 'AC6e67d227c543a656616a92adadd34255'
            auth_token = 'd0f93fc24380abc50f20a9c6aac01bb2'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Hi there! Please remember to sort out your rent',
                from_='+17738400140',
                to='+2347051889628'
            )

            print(message.sid)
        return super().save(*args, **kwargs)
