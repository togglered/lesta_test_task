import math
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FileForm
from .models import File
from .utils import calculate_tf_idf


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return redirect('main:results', file.id)
    else:
        form = FileForm()
    return render(request, 'index/index.html', {'form': form})


def results(request, id):
    if request.method == 'GET':
        file = get_object_or_404(File, id=id)
        results = calculate_tf_idf(file.file.read().decode('utf-8'))
        results.sort(key=lambda x: x['idf'], reverse=True)
        return render(request, 'results/results.html', {'results': results[:50]})


