from django.db import models


# Create your models here.
class Profile(models.Model):
    BG_COLOR_YELLOW = "yellow"
    BG_COLOR_BLUE = "blue"
    BG_COLOR_GREEN = "green"

    BG_CHOICES = (
        (BG_COLOR_BLUE, "Blue"),
        (BG_COLOR_YELLOW, "Yellow"),
        (BG_COLOR_GREEN, "Green"),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    bg_color = models.CharField(
        max_length=50, choices=BG_CHOICES, default=BG_COLOR_BLUE
    )

    def __str__(self):
        return self.name


class Link(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f"{self.profile} | {self.url}"
