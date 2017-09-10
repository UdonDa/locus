from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import subprocess


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print('if start')
        if form.is_valid():
            form.save()
            print('uploaded!')
            items = []
            img = Document.objects.latest("id")
            file_name = img.document.name[10:]
            subprocess.call('th ~/colorise.lua ' + '~/locus/media/' + img.document.name + ' ~/locus/media/document/result-' + file_name)
            for item in Document.objects.all():
                items.append({'image':item.document})
    #        return render_to_response('home/view.html', {'items':items},
            return render(request, 'core/upload_complete.html', {
                # 'picture': form.Meta.model.document,
                'items': items,
                'img': img.document.url,
                'name': file_name
            })
            # return render(request, 'core/upload_complete.html', {
            #     'form': form
            # })
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

#context_instance=RequestContext(request))

def upload_complete(request):
    return render(request, 'core/upload_complete.html')
