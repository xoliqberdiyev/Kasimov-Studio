from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='common/videos/')

    def __str__(self):
        return self.video.name
    

class ServiceCategory(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='common/service_category/image/')
    video =  models.FileField(upload_to='common/service_category/video/')

    def __str__(self):
        return f'{self.id} - {self.title}'


class Service(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='common/service/image/')
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.title}'
    

class Gallery(models.Model):
    image = models.ImageField(upload_to='common/gallery/image/')

    def __str__(self):
        return self.image.name
    

class Partner(models.Model):
    icon = models.ImageField(upload_to='common/partner/icon/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.link if self.link else self.icon.name
    

class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='common/about_us/image/')

    def __str__(self):
        return f'{self.id} - {self.title_uz}'
    

class Team(models.Model):
    image = models.ImageField(upload_to='common/team/image/')
    full_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.id} - {self.full_name}'
