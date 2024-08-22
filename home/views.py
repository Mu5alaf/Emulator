import os
import sys
from django.http import JsonResponse
from django.utils.translation import activate
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import app_form
from .models import App
import subprocess
from django.conf import settings

# Create your views here.
@login_required
def home_view(request):
    app_list = App.objects.filter(uploaded_by=request.user)
    return render(request,'home.html',{'app_list':app_list})


@login_required
def upload_app(request):
    if request.method == 'POST':
        form = app_form(request.POST,request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.uploaded_by = request.user
            app.save()
            messages.success(request,'Your APK uploaded Successfully')
            return redirect('home:home_page')
        else:
            messages.error(request,'Something went wrong')
            return redirect('home:upload_app')
    else:
        form = app_form()
    return render(request,'upload.html',{'form':form})

'''''
why subprocess model ?
we need subprocess model to run app in sequences and call our 
run_app file that have the instruction
'''''
@login_required
def run_app(request,id):
    if request.method == 'POST':
        try:
            app = App.objects.get(id=id)
            python_executable = sys.executable
            script_path = os.path.join(settings.BASE_DIR, 'home', 'run_app.py')
            env = os.environ.copy()
            env['PYTHONPATH'] = f"{env.get('PYTHONPATH', '')}:{sys.prefix}/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages"
            subprocess.run([python_executable,script_path,str(app.id)],check=True,env=env)
            print(script_path)
            messages.success(request,'App Done Successfully ')
            return redirect('home:home_page')
        except subprocess.CalledProcessError as e:
            messages.error(request, f'Error running the APK: {e}')
        return redirect('home:home_page')
    else:
        #handel non-post request
        return redirect('home:run_app')
    
@login_required
def app_info(request,id):
    app = App.objects.filter(id=id)
    context = {'app':app}
    return render(request,'apk_info.html',context)

def change_language(request):
    lang = request.GET.get('lang')
    if lang in [lang[0] for lang in settings.LANGUAGES]:
        activate(lang)
        response = JsonResponse({'success':True})
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME,lang)
        return response
    response = JsonResponse({'success':True})
