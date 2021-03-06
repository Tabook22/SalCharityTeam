from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Person,  Charityapp, Charityappfiels, Salct
from .forms import addNewForm,CharityForm, CharityappfielsForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.forms import modelformset_factory
from django.template import RequestContext
from django.forms.models import inlineformset_factory


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
        print("(1)--------------In the name of god most mercy most mercifull-------------------")
        postForm = CharityForm(request.POST) #contains the data of the user
        formset = ImageFormSet(request.POST or None, request.FILES,queryset=Charityappfiels.objects.none()) #Charityappfiles.objects.none() this is used to prevent displaying the previous added data

       #if postForm.is_valid() and formset.is_valid():
        post_form=postForm.save(commit=False)
        post_form.save()
        #post_form.user = request.user
        #instances=formset.save(commit=False)
        for form in formset.cleaned_data:
            up1 = form['upload_1']
            up2 = form['upload_2']
            up3 = form['upload_3']
            up4 = form['upload_4']
            up5 = form['upload_5']
            up6 = form['upload_6']
            up7 = form['upload_7']
            up8 = form['upload_8']
            up9 = form['upload_9']
            up10 = form['upload_10']
            charfle=Charityappfiels(charityapp=post_form,
                upload_1=up1,
                upload_2=up2,
                upload_3=up3,
                upload_4=up4,
                upload_5=up5,
                upload_6=up6,
                upload_7=up7,
                upload_8=up8,
                upload_9=up9,
                upload_10=up10)
            charfle.save()
            return HttpResponseRedirect("/")
            print("(3)--------------In the name of god most mercy most mercifull-------------------")
            #   print postForm.errors, formset.errors
    else:
        print("(4)--------------In the name of god most mercy most mercifull-------------------")
        postForm = CharityForm()
        formset = ImageFormSet(queryset=Charityappfiels.objects.none())
    return render(request, 'ghelp/charity_app.html',
                  {'postForm': postForm, 'formset': formset})


def newcharity2(request):
    
    if request.method == 'POST':
        postForm = CharityForm(request.POST) #contains the data of the user
        formUpload =CharityappfielsForm(request.POST or None, request.FILES)

        if postForm.is_valid and formUpload.is_valid:
            post=postForm.save()
            fls=formUpload.save(commit=False)
            fls.charityapp=post
            fls.save()
            return HttpResponseRedirect("/")

    else:
        postForm = CharityForm()
        formset = ImageFormSet(queryset=Charityappfiels.objects.none())
    return render(request, 'ghelp/charity_app.html',
                  {'postForm': postForm, 'formset': formset})



def fxtable(request):
    """
    getIds=Charityapp.objects.values_list('id', flat=True).order_by('id')
    getsalct=Salct()
    myid=[]
    for i in getIds:
        if i>=35:
            getsalct=Salct(charityapp_id=i)
            getsalct.save();
            myid.append(i)

    myid2=[]
    myid2=Salct.objects.values_list('charityapp_id', flat=True).order_by('charityapp_id')
    print(myid2)
    context={
        'myd':myid
    }
    """
    get_total=Charityappfiels.objects.all().count()
    get_img=Charityappfiels.objects.all()
    context={
        'get_img':get_img,
        'get_total':get_total
    }
   
    return render(request,"ghelp/test.html", context)


#----------------------------------------- Need more coding to fix inlineformset ----------------
# def addchrityapp(request):
#     #This is an instance of  inlineformset to connect two modles togather , the parent model and the child model
#     #The parent model is: Charityapp and the child model is: Charityappfiels
#     #here we are going to reference from Charityappfiels model to Charityapp model
#     #we have alos to tell it which fields to allow for the child object or model

#     #UploadfiledForm is an instance of the formset
#     UploadfileFormSet = inlineformset_factory(
#         Charityapp, Charityappfiels,
#         fields=['upload_1',
#             'upload_2',
#             'upload_3',
#             'upload_4',
#             'upload_5',
#             'upload_6',
#             'upload_7',
#             'upload_8',
#             'upload_9',
#             'upload_10',], extra=1, can_delete=True
#         )
#     #here am going to create the form for the formset, notice i already created the instance of the formset
#     # so i need to create a form for that instance
#     postForm=CharityForm() #this form for the parenet object
#     formset =UploadfileFormSet() 
#     #check to see if the request method is post
#     if request.method == "POST":
#         postForm = CharityForm(request.POST) #contains the data of the user
#         formset=UploadfileFormSet(request.POST or None, request.FILES)
#         getapp_id=postForm()
#         getapp_id.save()

#         if formset.is_valid():
#             instances=formset.save(commit=False)
#             for i in instances:
#                 i['charityapp']=getapp_id
#                 i.save()
    
#     context={
#         'appuser':postForm,
#         'appatt':formUpload
#     }
#     return render(request,"ghelp/addnewapp.html", context)