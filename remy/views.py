from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import DataCollection

from .resources import DataResource


# Create your views here.
def Home(request):

    if request.method=='POST':
        dataForm=DataForm(request.POST)

        if dataForm.is_valid():
            data=dataForm.cleaned_data['data']
            dataForm.save()


            context= {
            'data': data
            }

            template=loader.get_template('thankyou.html')

            return HttpResponse(template.render(context, request))

    else:
        form=DataForm()

    return render(request, 'base.html', {'form':form})

def export_data(request):
    if request.method=='POST':
        file_format=request.POST['file-format']
        data_resource=DataResource()
        dataset=data_resource.export()
        if file_format=='CSV':
            response=HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition']='attachment; filename="exported_data.csv"'
            return response

        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response

        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response

    return render(request, 'export.html')
