from django.db import models

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['content'] == '' or len(postData['content']) < 5 or len(postData['content']) > 255:
            errors['content'] = 'Comment should have 5 characters to 255 characters long'
        return errors

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['course_name'] == '' or len(postData['course_name']) < 5 or len(postData['course_name']) > 255:
            errors['course_name'] = 'Course name field should have 5 characters to 255 characters long'
        if postData['description'] == '' or len(postData['description']) < 15 or len(postData['description']) > 255:
            errors['description'] = 'Description field should have 15 characters to 255 characters long'
        return errors

class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.OneToOneField(Description,related_name="course",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course,related_name="has_comments",on_delete=models.CASCADE)

    objects = CommentManager()

