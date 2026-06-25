from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Chai Model
class ChaiVarity(models.Model):
    CHAI_TYPE = [
        ('ML', 'Masala'),
        ('EL', 'Elachi'),
        ('PL', 'Plain'),
        ('KL', 'Kiwi'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_add = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


# One-to-Many Relationship
# One Chai -> Many Reviews
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVarity,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s review for {self.chai.name}"


# Many-to-Many Relationship
# One Store -> Many Chais
# One Chai -> Available in Many Stores
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    chai_varity = models.ManyToManyField(
        ChaiVarity,
        related_name='stores'
    )

    def __str__(self):
        return self.name


# One-to-One Relationship
# One Chai -> One Certificate
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVarity,
        on_delete=models.CASCADE,
        related_name='certificate'
    )

    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    expired_date = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.chai.name}"