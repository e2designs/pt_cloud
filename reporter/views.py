from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reporter.serializers import TestSuiteSerializer, TestCaseSerializer
from .models import TestSuite, TestCase
import matplotlib

matplotlib.use('Agg')

from matplotlib.backends.backend_agg import FigureCanvas
from matplotlib import pyplot


def pie_chart(request):
    suites = TestSuite.objects.raw('select *, max(date_run) '
                                   'from reporter_testsuite group by '
                                   'suite_name')

    plot_values = {'total': 0, 'passed': 0, 'skipped': 0, 'failed': 0}
    for suite in suites:
        plot_values['total'] += suite.num_tests
        plot_values['passed'] += suite.num_passed
        plot_values['skipped'] += suite.num_skipped
        plot_values['failed'] += suite.num_failed

    labels = 'Passed', 'Skipped', 'Failed'
    sizes = [plot_values['passed'], plot_values['skipped'], plot_values['failed']]
    colors = ['green', 'yellow', 'red']
    explode = (0, 0.1, 0)

    fig = pyplot.figure(0)
    # Plot
    fig.add_subplot = pyplot.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False,
                                 startangle=140)

    fig.add_axes = pyplot.axis('equal')
    figCanvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    figCanvas.print_png(response)
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
def display_test_status(request):
    """
    :param request: default page request
    :return: aggregated test results, parsed from database
    """

    if request.method == 'GET':

        suites = TestSuite.objects.raw('select *, max(date_run) '
                                       'from reporter_testsuite group by '
                                       'suite_name')

        plot_values = {'total': 0, 'passed': 0, 'skipped': 0, 'failed': 0}
        for suite in suites:
            plot_values['total'] += suite.num_tests
            plot_values['passed'] += suite.num_passed
            plot_values['skipped'] += suite.num_skipped
            plot_values['failed'] += suite.num_failed

        context = {
            'suites': suites,
            'plot_values': plot_values,
        }
        return render(request, 'test_status.html', context)

    elif request.method == 'POST':

        serializer = TestSuiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def display_testcase_status(request):
    """
    :param request: default page request
    :return: aggregated test results, parsed from database
    """

    if request.method == 'GET':

        tests = TestCase.objects.all()

        context = {
            'tests': tests,
        }
        return render(request, 'testcase_status.html', context)

    elif request.method == 'POST':

        serializer = TestCaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
