import pygal
from bugs.models import Issues


def sum_chart(ticket_type, issue_type):
    """Show summary for features"""

    waiting = ticket_type.objects.filter(status='Waiting', issue_type=issue_type).count()
    progress = ticket_type.objects.filter(status='In progress', issue_type=issue_type).count()
    completed = ticket_type.objects.filter(status='Completed', issue_type=issue_type).count()
    p_chart = pygal.Pie(
        print_values=True,
        inner_radius=0.4
    )

    p_chart.add('Waiting', waiting)
    p_chart.add('In Progress', progress)
    p_chart.add('Completed', completed)
    return p_chart.render()


def FeaturePieChart():
    chart = sum_chart(Issues, "Feature")
    return chart

def BugPieChart():
    chart = sum_chart(Issues, "Bug")
    return chart
