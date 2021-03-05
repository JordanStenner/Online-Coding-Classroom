from django.db import models

### LANGUAGE/LESSON MODELS - MAY BE MOVED INTO ITS OWN APP ###


class LanguageManager(models.Manager):
    """ Manager class for language methods """
    def get_lesson_count(self, lesson, language):
        """ Method for returning the lesson count for a particular language """
        count = lesson.objects.filter(language__language_name__iexact=language.language_name).count()
        return count

class ProgrammingEnvironment(models.Model):
    """ Model for Programming Types """
    environment_name = models.CharField(max_length=30, unique=True, primary_key=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.environment_name

class Language(models.Model):
    """ Model for Programming Environments """
    language_name = models.CharField(max_length=15, unique=True)
    description = models.TextField(max_length=100)

    environment = models.ForeignKey(ProgrammingEnvironment, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.language_name

class Lesson(models.Model):
    """ Model for Lessons """
    lesson_title = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    lesson_description = models.TextField()
    lesson_content = models.TextField()
    lesson_code = models.TextField()
    check_result = models.TextField()
    lesson_number = models.IntegerField()

    def __str__(self):
        return self.lesson_title

class LessonHint(models.Model):
    """ Model for Lesson Hints - One Lesson has many LessonHints """
    hint_title = models.CharField(max_length=15)
    hint_description = models.TextField(max_length=40)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.hint_title