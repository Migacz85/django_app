from django.shortcuts import render
from charts.charts import FeaturePieChart, BugPieChart


def charts(request):
    """ Charts """
    return render(request, 'charts.html',
                  {'feature_chart': FeaturePieChart(),
                   'bugs_chart': BugPieChart()
                   })

