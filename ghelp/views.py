from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Person,  Charityapp, Charityappfiels
from .forms import addNewForm,CharityForm, CharityappfielsForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.forms import modelformset_factory
from django.template import RequestContext


# Create your views here.
@xframe_options_exempt
def addnew(request):
    form = addNewForm(request.POST or None, request.FILES or None)
    msg="الرجاء تعبئة الفورمة"
    if request.method == "POST":
        pname= request.POST.get("name")
        pnationality = request.POST.get("nationality")
        pcardid = request.POST.get("cardid")
        phelptype = request.POST.get("helptype")
        puploadImg = request.POST.get("uploadImg")
        pcomments = request.POST.get("comments")

        getcardid=Person.objects.filter(cardid=pcardid)
        if getcardid:
            msg="رقم البطاقة مكرر"
            context = {'form': form,
                   'msg': msg,
                   'code':1}
            return render(request, "ghelp/add_new.html", context)
        else:
            #new_person= Person()
            #new_person = Person(name=pname, nationality=pnationality, cardid=pcardid, helptype=phelptype, comments=pcomments)
            #upload_file=request.FILES['uploadImg']
            #fs=FileSystemStorage()
            #fs.save(uploaded_file.name,uploaded_file)
            #new_person.save()
            form.save()
            form=addNewForm()
            msg="تم تعبئة الإستمارة بنجاح"
            context = {'form': form,
                'msg': msg,
                'code':0}
            return render(request, "ghelp/add_new.html", context)

        # getting the id of the Place which will be saved. the id will be sent inside a hidden filed from the form

        """pname= request.POST.get("name")
        pnationality = request.POST.get("nationality")
        pcardid = request.POST.get("cardid")
        phelptype = request.POST.get("helptype")
        pcomments = request.POST.get("comments")


        # adding data to the model
        new_person = Person(name=pname, nationality=pnationality, cardid=pcardid, comments=pcomments)
        new_person.save()"""


    else:
        form=addNewForm()
        context = {'form': form,
                   'msg': msg,
                   'code':2}
        return render(request, "ghelp/add_new.html", context)

def plist(request):
    getall=Person.objects.all()
    context={
        'lst':getall
        }

    return render(request,"ghelp/plist.html",context)

def newcharity(request):
    ImageFormSet = modelformset_factory(Charityappfiels,form=CharityappfielsForm,)
    #ImageFormSet = modelformset_factory(Charityappfiels,fields=('upload_1',))

    if request.method == 'POST':
        postForm = CharityForm(request.POST) #contains the data of the user
        formset = ImageFormSet(request.POST or None, request.FILES,queryset=Charityappfiels.objects.none()) #Charityappfiles.objects.none() this is used to prevent displaying the previous added data

       # if postForm.is_valid() and formset.is_valid():
        post_form = postForm.save()
        #post_form.user = request.user
        instances=formset.save(commit=False)
        chrapp=Charityappfiels()
        #for f in instances:
        for f in request.FILES.getlist('upload_1'):
            with open(Path(settings.MEDIA_ROOT + "/" + f.name).resolve(), 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
            instances.charityapp=post_form
            instances.upload_1=f
            #charityappfiles.objects.create(charityapp=post_form,upload_1=file)
            instances.save()
            """
            up1 = f.cleaned_data['upload_1']
            up2 = f.cleaned_data['upload_2']
                up3 = f.cleaned_data['upload_3']
                up4 = f.cleaned_data['upload_4']
                up5 = f.cleaned_data['upload_5']
                up6 = f.cleaned_data['upload_6']
                up7 = f.cleaned_data['upload_7']
                up8 = f.cleaned_data['upload_8']
                up9 = f.cleaned_data['upload_9']
                up10 = f.cleaned_data['upload_10']
                chrapp = Charityappfiels(charityapp=post_form,
                upload_2=up2,
                upload_3=up3,
                upload_4=up4,
                upload_5=up5,
                upload_6=up6,
                upload_7=up7,
                upload_8=up8,
                upload_9=up9,
                upload_10=up10,
                )
                chrapp.save()"""
            return HttpResponseRedirect("/")
        #else:
         #   print postForm.errors, formset.errors
    else:
        postForm = CharityForm()
        formset = ImageFormSet(queryset=Charityappfiels.objects.none())
    return render(request, 'ghelp/charity_app.html',
                  {'postForm': postForm, 'formset': formset})




