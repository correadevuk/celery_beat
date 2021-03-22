from django import forms
from django_enum_choices.fields import EnumChoiceField
from .enums import TimeInterval, SetupStatus
from .models import Setup
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from django_celery_beat.admin import PeriodicTaskForm


class SetupForm(PeriodicTaskForm):

    class Meta:
        model = PeriodicTask
        fields = ('name', 'regtask', 'enabled', 'interval')

    def __init__(self, *args, **kwargs):
        super(PeriodicTaskForm, self).__init__(*args, **kwargs)
        # Task name
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields[
            'name'].help_text = 'Short Description For This Task'
        self.fields['name'].label = 'Task Name'

        # Task
        self.fields['regtask'].widget.attrs['class'] = 'form-control'
        self.fields[
            'regtask'].help_text = ''
        self.fields['regtask'].label = 'Select Task'

        # Status
        self.fields['enabled'].widget.attrs['class'] = 'form-control'
        self.fields[
            'enabled'].help_text = 'Active'
        self.fields['enabled'].label = ''

        # Interval
        self.fields['interval'].widget.attrs['class'] = 'form-control'
        self.fields[
            'interval'].help_text = ''
        self.fields['interval'].label = 'Select Task'

        # Interval
        self.fields['task'].widget.attrs['class'] = 'invisible'
        self.fields[
            'task'].help_text = ''
        self.fields['task'].label = ''


    # title = forms.CharField(label='Task Name',
    #                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    #
    # # choice = forms.ModelChoiceField(queryset=PeriodicTask.objects.filter("task"))
    #
    # class Meta:
    #     model = Setup
    #     exclude = ('created_at', 'task')

class EditForm(PeriodicTaskForm):

    class Meta:
        model = PeriodicTask
        fields = ('name', 'task', 'enabled', 'interval')

    def __init__(self, *args, **kwargs):
        super(PeriodicTaskForm, self).__init__(*args, **kwargs)
        # Task name
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['name'].label = 'Task Name'

        # Task
        self.fields['task'].widget.attrs['class'] = 'form-control'
        self.fields['task'].widget.attrs['readonly'] = True
        self.fields['task'].label = 'Task'

        # Status
        self.fields['enabled'].widget.attrs['class'] = 'form-control'
        self.fields['enabled'].widget.attrs['disabled'] = 'disabled'
        self.fields[
            'enabled'].help_text = 'Active'
        self.fields['enabled'].label = ''

        # Interval
        self.fields['interval'].widget.attrs['class'] = 'form-control'
        self.fields[
            'interval'].help_text = ''
        self.fields['interval'].label = 'Select Task'

        # Task select
        self.fields['regtask'].widget.attrs['class'] = 'invisible'
        self.fields['regtask'].label = ''


