import os
import time
from django.shortcuts import render
from . import forms
from django.shortcuts import render
from .models import Video,Video_info
from django.views.generic import TemplateView
from .forms import VideoForm, vpreview, vgen
from django.conf import settings
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'first_app/index.html')

def VList(request):

    videos = Video.objects.order_by('name')
    list_videos=[]
    for v in videos:
        list_videos.append(v.name)
    form1 = vpreview()
    context = {
                'form': form1,
                "list_videos": list_videos,
            }
    if request.POST:
        name = request.POST.get('ch')
        temp=Video.objects.filter(name=name)
        for v in temp:
            pv=str(v.videofile)
        pv=pv.split('/')[1]

        context = {'videofile': '/media/videos/' + str(pv),
                   'form': form1,
                   "list_videos": list_videos,
                   }

    return render(request,"first_app/preview.html",context)

def PhotoGrid(request):
    context = {}
    print(request.GET.get('name'))
    import os
    filelist = os.listdir('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/output_frames')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not (fichier.startswith(str(request.GET.get('name')))):
            filelist.remove(fichier)
    print(filelist)
    context['files']=filelist
    #context['counter']=[1,2,3,4,5,6]
    #context['c']=0
    return render(request, "first_app/photogrid.html", context)

def about(request):
    context={}
    return render(request, "first_app/about.html", context)

def Vout(request):
    videos = Video.objects.order_by('name')
    list_videos = []
    for v in videos:
        list_videos.append(v.name)
    context={}
    form1 = vgen()
    context = { 'form': form1,
                'list_videos': list_videos,
            }
    if request.POST:
        form1 = vgen(request.POST)
        if form1.is_valid():
            name=request.POST.get('name')
            f = form1.cleaned_data['fps']
            temp = Video.objects.filter(name=name)
            for v in temp:
                pv = str(v.videofile)
            print(pv)
            path=pv.split('/')
            file_name=path[1]
            fname=file_name.split('.')
            ffname=fname[0]
            import sys
            sys.path.insert(0,'C:/Users/Bipin Gowda/PycharmProjects/GodsEye')
            from main_test import alpha
            print(ffname)
            pathh='C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/output/'+ffname+'_Output_'+str(f)+'.mp4'
            context = {
                       'name': ffname + '-frame_' + str(f),
                       'form': form1,
                       'is_output_generated': 'true',
                       }
            if (os.path.exists(pathh)==False):
                start=time.time()
                ifp,nop=alpha(file_name,f)
                end = time.time()
                t=end-start
                #temp_path='C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/output_frames/'+ffname + '-frame_' + str(f)+'_1.jpg'
                file_list1 = os.listdir('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/output_frames')
                o1=[fn for fn in file_list1 if ffname+'-frame_'+str(f) in fn]
                if len(o1)>0:
                    av='Yes'
                else:
                    av='No'
                new_name=file_name+'('+str(f)+')'
                query=Video_info(name=new_name, ifps=int(ifp), ofps=int(f), no_of_people=int(nop), any_violence=av, time_taken=int(t))
                query.save()
                context['vname']=new_name
                context['ifps']=ifp
                context['ofps'] = f
                context['nop'] = nop
                context['av'] = av
                context['tt'] = t
            else:
                new_name = file_name + '(' + str(f) + ')'
                temp=Video_info.objects.filter(name=new_name)
                for i in temp:
                    context['vname'] = i.name
                    context['ifps'] = i.ifps
                    context['ofps'] = f
                    context['nop'] = i.no_of_people
                    context['av'] = i.any_violence
                    context['tt'] = i.time_taken
            context['videofile']='/media/output/' + ffname + '_Output_' + str(f) + '.mp4'
            print(context)
            #'videofile': 'file:///C:/Users/Bipin Gowda/PycharmProjects/GodsEye/output/' + ffname + '_Output.mp4'

    return render(request,"first_app/output.html",context)

def showvideo(request):
    context={'file_exists': 'false'}
    if len(Video.objects.order_by('name')):
        lastvideo = Video.objects.last()
        videofile = lastvideo.videofile
        context['videofile']=videofile
    form = VideoForm(request.POST or None, request.FILES or None)
    context['form']=form
    print(context)
    if form.is_valid():
        if request.FILES:
            for filename, file in request.FILES.items():
                name = request.FILES[filename].name
                n=Video.objects.filter(name=request.POST.get('name'))
                path = 'C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/videos/'+name
                if (os.path.exists(path) == False and len(n)==0):
                    context['file_exists'] = 'false'
                    context['videofile'] = 'videos/'+name
                    form.save()
                else:
                    if len(n)>0:
                        context['file_exists']='Please choose a different name'
                    else:
                        context['file_exists']='Video already exists!'
    return render(request, 'first_app/video_upload.html', context)
