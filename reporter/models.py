
from django.db import models
from django.utils import timezone


class TestSuite(models.Model):
    suite_name = models.CharField(max_length=200)
    date_run = models.DateTimeField(default=timezone.now)
    system = models.CharField(max_length=200, default='')
    test_bench = models.CharField(max_length=200, default='')
    num_tests = models.IntegerField(default=0)
    num_passed = models.IntegerField(default=0)
    num_skipped = models.IntegerField(default=0)
    num_failed = models.IntegerField(default=0)

    def __str__(self):
        return self.suite_name


class TestCase(models.Model):
    suite_name = models.CharField(max_length=200)
    test_module = models.CharField(max_length=200)
    test_name = models.CharField(max_length=200)
    date_run = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    failing_context = models.CharField(max_length=900, default='NA')

    def __str__(self):
        return self.test_name
