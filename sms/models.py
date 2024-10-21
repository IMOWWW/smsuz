from django.db import models

# Create your models here.


class Sms(models.Model):

    class SmsStatus(models.TextChoices):
        DELIVERED = 'DELIVERED', 'Delivered'
        UNDELIVERED = 'UNDELIVERED', 'Undelivered'
        EXPIRED = 'EXPIRED', 'Expired'

    transactionid = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    status = models.CharField(max_length=12, choices=SmsStatus.choices)
    statusdate = models.DateTimeField(default=None, null=True, blank=True)
    partinfo = models.CharField(max_length=25, blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']