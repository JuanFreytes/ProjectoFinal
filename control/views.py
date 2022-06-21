from django.shortcuts import render

from control.models import Control
from control.forms import ControlForm


def controles(request):
    controles = Control.objects.all()

    context_dict = {
        'controles': controles
    }

    return render(
        request=request,
        context=context_dict,
        template_name="control/control_list.html"
    )


def control_form(request):
    if request.method == 'POST':
        control_form = ControlForm(request.POST)
        if control_form.is_valid():
            data = control_form.cleaned_data
            control = Control(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            control.save()

            controles = Control.objects.all()
            context_dict = {
                'controles': controles
            }
            return render(
                request=request,
                context=context_dict,
                template_name="control/control_list.html"
            )

    control_form = ControlForm(request.POST)
    context_dict = {
        'control_form': control_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='control/control_form.html'
    )

def delete_control(request, pk: int):
    control = Control.objects.get(pk=pk)
    if request.method == 'POST':
        control.delete()

        controles = Control.objects.all()
        context_dict = {
            'controles': controles
        }
        return render(
            request=request,
            context=context_dict,
            template_name="control/control_list.html"
        )

    context_dict = {
        'control': control,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='control/control_confirm_delete.html'
    )