from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    authors = models.ManyToManyField(Author, related_name='blogs')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authored_blogs')

    def __str__(self):
        return self.title

class Entry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='entries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=100)

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     authors = models.ManyToManyField(Author, related_name='blogs')

# class Entry(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True, null=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    