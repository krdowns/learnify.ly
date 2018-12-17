from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    COURSE_CATEGORIES = [
        ('arts_humanities', 'Arts and Humanities'),
        ('business', 'Business'),
        ('computer_science', 'Computer Science'),
        ('health_fitness', 'Health and Fitness'),
        ('languages', 'Languages'),
        ('math_logic', 'Math and Logic'),
        ('music', 'Music'),
        ('personal_developement', 'Personal Developement'),
    ]
    title = models.CharField(max_length=50)
    category = models.CharField(choices=COURSE_CATEGORIES, max_length=50)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    isFeatured = models.BooleanField(default=False)
    date_created = models.DateField(
        auto_now=True, auto_now_add=False, editable=False)
    date_updated = models.DateField(auto_now=False, auto_now_add=True)
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='course')
    preview_video = models.FileField(upload_to='preview_videos', blank=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='course_videos', blank=True)
    description = models.TextField(blank=True)
    order_number = models.IntegerField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.title


class Purchase(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.DO_NOTHING, related_name='purchases')
    purchaser = models.ForeignKey(
        UserProfile, on_delete=models.DO_NOTHING, related_name='purchases')

    def __str__(self):
        return self.course.title
