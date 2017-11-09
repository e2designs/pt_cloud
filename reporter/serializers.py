from .models import TestSuite, TestCase
from rest_framework import serializers


class TestSuiteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    suite_name = serializers.CharField(required=True, max_length=200)
    date_run = serializers.DateTimeField(required=False)
    system = serializers.CharField(required=False)
    num_tests = serializers.IntegerField(required=True)
    num_passed = serializers.IntegerField(required=True)
    num_skipped = serializers.IntegerField(required=True)
    num_failed = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `TestSuite` instance, given the validated data.
        """
        return TestSuite.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TestSuite` instance, given the validated data.
        """
        instance.suite_name = validated_data.get('suite_name', instance.suite_name)
        instance.date_run = validated_data.get('date_run', instance.date_run)
        instance.system = validated_data.get('system', instance.system)
        instance.num_tests = validated_data.get('num_tests', instance.num_tests)
        instance.num_passed = validated_data.get('num_passed', instance.num_passed)
        instance.num_skipped = validated_data.get('num_skipped', instance.num_skipped)
        instance.num_failed = validated_data.get('num_failed', instance.num_failed)
        instance.save()
        return instance


class TestCaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    test_suite = serializers.CharField(required=True, max_length=200)
    test_module = serializers.CharField(required=True, max_length=200)
    test_name = serializers.CharField(required=True, max_length=200)
    date_run = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=True, max_length=50)
    failing_context = serializers.CharField(required=False, max_length=500)

    def create(self, validated_data):
        """
        Create and return a new `TestSuite` instance, given the validated data.
        """
        return TestCase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TestSuite` instance, given the validated data.
        """
        instance.test_suite = validated_data.get('test_suite', instance.test_suite)
        instance.test_module = validated_data.get('test_module', instance.test_module)
        instance.test_name = validated_data.get('test_name', instance.test_name)
        instance.status = validated_data.get('date_run', instance.date_run)
        instance.status = validated_data.get('status', instance.status)
        instance.failing_context = validated_data.get('failing_context',
                                                      instance.failing_context)
        instance.save()
        return instance
