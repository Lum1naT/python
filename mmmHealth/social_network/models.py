from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)


    CZECH = 'CZE'
    SLOVAKIA = 'SVK'
    GERMANY = 'GER'
    AUSTRIA = 'AUS'

    COUNTRY_CHOICES = [
        (CZECH, 'Czech'),
        (SLOVAKIA, 'Slovakia'),
        (GERMANY, 'Germany'),
        (AUSTRIA, 'Austria'),
    ]

    country = models.CharField(
        max_length=4,
        choices= COUNTRY_CHOICES,
        default= CZECH,
    )

    country = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    account_status = models.SmallIntegerField(default = 1)

    def __str__(self):
        return self.email + ' as ' + self.first_name + ' ' + self.last_name


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = 'sender')
    reciever = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = 'reciever')
    dt_sent = models.DateTimeField(auto_now = True)
    dt_seen = models.DateTimeField(blank = True, null = True)
    file = models.FileField(upload_to = 'uploads/', blank = True, null = True)

    def __str__(self):
        return self.sender + ' > ' + self.reciever
