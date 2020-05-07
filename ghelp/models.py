from django.db import models
from django.utils import timezone
import datetime
import os
from uuid import uuid4

# Create your models here.

class Family(models.Model):
    regdt=models.DateTimeField(auto_now_add=True)
    gov=models.CharField(verbose_name="المحافظة", max_length=50,null=True, blank=True)
    wly=models.CharField(verbose_name="الولاية", max_length=50, null=True, blank=True)
    vill=models.CharField(verbose_name="القرية",max_length=50, null=True, blank=True)
    stre=models.CharField(verbose_name="الشارع", max_length=50, null=True, blank=True)
    ftype=models.CharField(verbose_name="فئة الأسرة", max_length=50,null=True, blank=True)
    hasname=models.CharField(verbose_name="إسم الزوج", max_length=300, null=True, blank=True)
    hasnat=models.CharField(verbose_name="جنسية الزوج", max_length=50,null=True, blank=True)
    hasid=models.CharField(verbose_name="الرقم المدني", max_length=50,null=True, blank=True)
    hasmobile=models.CharField(verbose_name="هاتف الزوج", max_length=50,null=True, blank=True)
    hasstatus=models.CharField(verbose_name="حالة الزوج", max_length=50, null=True)
    hasstatus_others=models.TextField(verbose_name="أخري", null=True)
    wfname=models.CharField(verbose_name="إسم الزوجة", max_length=300,null=True, blank=True)
    wfnat=models.CharField(verbose_name="جنسية الزوجة", max_length=50,null=True, blank=True)
    wfid=models.CharField(verbose_name="الرقم المدني", max_length=50,null=True, blank=True)
    wfmobile=models.CharField(verbose_name="رقم الهاتف", max_length=50,null=True, blank=True)
    wfstatus=models.CharField(verbose_name="حالة الزوجة", max_length=300, null=True, blank=True)
    wfstatus_others=models.TextField(verbose_name="أخرى", null=True)
    orph=models.CharField(verbose_name="إسم ولي أمر الأيتام أو الوكيل", max_length=300, null=True)
    orph_id=models.CharField(verbose_name="الرقم المدني", max_length=50, null=True)
    orph_rel=models.CharField(verbose_name="صلة القرابة", max_length=50, null=True)
    orphmobile=models.CharField(verbose_name="رقم الهاتف", max_length=50, null=True)

    def __str__(self):
        return self.hasname

class FamilyMember(models.Model):
    inhouse_no=models.IntegerField(verbose_name="عدد أفراد الأسرة المقيمين بالمنزل بصفة دائمة",  null=True, blank=True)
    above18=models.IntegerField(verbose_name="عدد الأبناء فوق سن ١٨ سنة",null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الإبتدائي", null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الإعدادي",  null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الثانوي", null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الجامعي",  null=True,blank=True)

class FamilyMemberDetail(models.Model):
    fullname=models.CharField(verbose_name="الأسم الثلاثي و القبيلة",  max_length=300,null=True, blank=True)
    rel=models.CharField(verbose_name="صلة القرابة", max_length=50, null=True, blank=True)
    familystatus=models.CharField(verbose_name="الحالة الإجتماعية", max_length=300,null=True, blank=True)
    dateofbirth=models.CharField(verbose_name="سنة الميلاد", max_length=50,null=True, blank=True)
    education=models.CharField(verbose_name="المرحلة الدراسية",  max_length=50,null=True, blank=True)
    job=models.CharField(verbose_name="الوظيفة", max_length=50,null=True, blank=True)
    jobplace=models.CharField(verbose_name="جهة العمل", max_length=50,null=True, blank=True)
    montlyincom=models.DecimalField(verbose_name="مبلغ الدخل الشهري", max_digits=6, decimal_places=2)
    loan=models.DecimalField(verbose_name="مبلغ القرض", max_digits=6, decimal_places=2)
    installment=models.DecimalField(verbose_name="مبلغ القسط الشهري", max_digits=6, decimal_places=2)
    loandesc=models.TextField(verbose_name="سبب القرض",null=True, blank=True)
    healthstatus=models.TextField(verbose_name="إسم الحالة الصحية",null=True, blank=True)

class FamilyIncome(models.Model):
    mainIncom=models.DecimalField(verbose_name="مبلغ الراتب",max_digits=6, decimal_places=2)
    retirIncom=models.DecimalField(verbose_name="مبلغ التقاعد",max_digits=6, decimal_places=2)
    insuIncom=models.DecimalField(verbose_name="الضمان",max_digits=6, decimal_places=2)
    sctIncom=models.DecimalField(verbose_name="مبلغ فريق صلالة الخيري",max_digits=6, decimal_places=2)
    othersIncom=models.DecimalField(verbose_name="مبالغ أخرى",max_digits=6, decimal_places=2)

class FamilyHouse(models.Model):
    housetype=models.CharField(verbose_name="نوع السكن", max_length=50,null=True, blank=True)
    houseothers=models.CharField(verbose_name="أخرى", max_length=50,null=True, blank=True)
    houseontype=models.CharField(verbose_name="نوع حيازة السكن", max_length=50,null=True, blank=True)
    houseroom_n=models.IntegerField(verbose_name="عددالغرف",null=True,blank=True)
    housersetting_n=models.IntegerField(verbose_name="عددالمجالس",null=True,blank=True)
    housekitten_n=models.IntegerField(verbose_name="عددالمطابخ", null=True,blank=True)
    housebath_n=models.IntegerField(verbose_name="عددالحمامات", null=True,blank=True)
    houserent_t=models.DecimalField(verbose_name="مبالغ الإيجار الشهري",max_digits=6, decimal_places=2)
    houserent_r=models.DecimalField(verbose_name="المتبقي من الإيجار الشهري",max_digits=6, decimal_places=2)
    houseelec_r=models.DecimalField(verbose_name="مبالغ فاتورة الكهرباء",max_digits=6, decimal_places=2)
    housewater_r=models.DecimalField(verbose_name="مبالغ فاتورةالمياة",max_digits=6, decimal_places=2)

class FamilyAssit(models.Model):
    assit_private_cars=models.IntegerField(verbose_name="السيارات الخاصة", null=True,blank=True)
    assit_taxi=models.IntegerField(verbose_name="تاكسي",  null=True,blank=True)
    assit_school_bus=models.IntegerField(verbose_name="حافلات المدرسة", null=True,blank=True)
    assit_gaz_car=models.IntegerField(verbose_name="سيارات الغاز",  null=True,blank=True)
    assit_others=models.TextField(verbose_name="أخرى", null=True)


class FamilyLoan(models.Model):
    loantype=models.IntegerField(verbose_name="نوع القرض",  null=True,blank=True)
    nameloner=models.DecimalField(verbose_name="إسم الجهة المناعة للقرض أو التمويل",max_digits=6, decimal_places=2)
    totalloan=models.DecimalField(verbose_name="مبلغ القرض",max_digits=6, decimal_places=2)
    instllament=models.DecimalField(verbose_name="القسط الشهري",max_digits=6, decimal_places=2)
    balanc=models.DecimalField(verbose_name="المبلغ المتبقي",max_digits=6, decimal_places=2)

class FamilyNeeds(models.Model):
    food_supply=models.BooleanField(verbose_name="كفالة مواد غذائية",default=False)
    orp_care=models.BooleanField(verbose_name="كفالة أسر أيتام",default=False)
    elec_needs=models.TextField(verbose_name="المواد الكهربائية", null=True, blank=True)
    furn_needs=models.TextField(verbose_name="الأثاث المنزلي",  null=True, blank=True)
    other_needs=models.TextField(verbose_name="متطلبات أخري",  null=True, blank=True)

class FamilyReport(models.Model):
    fid=models.ForeignKey(Family, on_delete=models.CASCADE)
    family_report=models.TextField(verbose_name="تقرير الباحث الإجتماعي عن حالة الأسرة",null=True, blank=True)


#Indivual help to people such as forign workers
class Person(models.Model):
    HELP_TYPE_CHOICES = (
        ("غذائية","غذائية"),
        ("مالية","مالية"),
        ("صحية","صحية"),
        ("أخرى","أخرى"),
        )

    COUNTIRES_CHOICES = (
        ("اليمن","اليمن"),
        ("مصر","مصر"),
        ("السودان","السودان"),
        ("الأردن","الأردن"),
        ("فلسطين","فلسطين"),
        ("سوريا","سوريا"),
        ("العراق","العراق"),
        ("تونس","تونس"),
        ("الجرائر","الجزائر"),
        ("المغرب","المغرب"),
        ("ليبيا","ليبيا"),
        ("الهند","الهند"),
        ("باكستان","باكستان"),
        ("بنجلاديش","بنجلاديش"),
        ("الفليبين","الفليبين"),
        ("سيرلانا","سيرلانكا"),
        ("أثيوبيا","أثيوبيا"),
        ("الصومال","الصومال"),
        ("إلتيريا","إلتيريا"),
        ("تركيا","تركيا"),
        ("لبنان","لبنان"),

        )

    dt = models.DateTimeField(auto_now_add=True)
    name=models.CharField(verbose_name="الإسم", max_length=300,null=True, blank=True)
    nationality=models.CharField(verbose_name="الجنسية", max_length=20, choices = COUNTIRES_CHOICES, default = '1')
    #nationality=CountryField(verbose_name="الجنسية", blank_label='(select country)',default="OM")
    cardid=models.CharField(verbose_name="رقم البطاقة", max_length=50,default="12")
    #uploadImg=models.ImageField(upload_to = 'pic_folder/%Y/%m/%d/%H/%M/%S/', default = 'pic_folder/None/no-img.jpg')
    uploadImg=models.ImageField(upload_to = 'pic_folder', default = 'pic_folder/None/no-img.jpg')
    helptype=models.CharField(verbose_name="نوع المساعدة",max_length=10, choices = HELP_TYPE_CHOICES, default = '1')
    comments=models.TextField(verbose_name="ملاحظات",null=True, blank=True)

    class Meta:
        ordering = ('dt',)

    def __str__(self):
        return f'Name {self.name} id {self.cardid}'


class Charityapp(models.Model):
    HOUSING_TYPE_CHOICES = (
        ("ملك","ملك"),
        ("إيجار","إيجار"),
        )
    dt = models.DateTimeField(auto_now_add=True)
    name=models.CharField(verbose_name="الأسم الثلاثي و القبيلة", max_length=300,null=True, blank=True)
    tel=models.CharField(verbose_name="رقم الهاتف", max_length=300,null=True, blank=True)
    health  =models.CharField(verbose_name="هل أحد أفراد الأسرة يعاني من مرض مزمن", max_length=300,null=True, blank=True)
    debt   =models.CharField(verbose_name="قيمة المديونيات", max_length=300,null=True, blank=True)
    housing  =models.CharField(verbose_name="نوع السكن",max_length=10, choices = HOUSING_TYPE_CHOICES, default = '1')
    totalicone =models.CharField(verbose_name="إجمالي دخل الأسرة", max_length=300,null=True, blank=True)
    familyno   =models.CharField(verbose_name="عدد أفراد الأسرة", max_length=300,null=True, blank=True)
    soc        =models.CharField(verbose_name="الحالة الإجتماعية لطالب المساعدة", max_length=300,null=True, blank=True)
    Helptype   =models.CharField(verbose_name="نوع المساعدة المطلوبة", max_length=300,null=True, blank=True)


    class Meta:
        ordering = ('dt',)

    def __str__(self):
        return self.name

class Charityappfiels(models.Model):
    """
    may also be a callable, such as a function, which will be called to obtain the upload path, 
    including the filename. This callable must be able to accept two arguments, and return a 
    Unix-style path (with forward slashes) to be passed along to the storage system. The 
    two arguments that will be passed are:
    1- "instance": An instance of the model where the FileField is defined. More specifically, this is the particular instance where the current file is being attached.
    2- "filename":The filename that was originally given to the file. This may or may not be taken into account when determining the final destination path.
    
    """
    # def path_and_rename(path):
    #     def wrapper(instance, filename):
    #         ext = filename.split('.')[-1]
    #         # get filename
    #         if instance.pk:
    #             filename = '{}.{}'.format(instance.pk, ext)
    #         else:
    #             # set filename as random string
    #             filename = '{}.{}'.format(uuid4().hex, ext)
    #         # return the whole path to the file
    #         return os.path.join(path, filename)
    #     return wrapper

    def path_and_rename(path, prefix):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            #project = "pid_%s" % (instance.project.id,)
            # get filename
            if instance.pk:
                complaint_id = "cid_%s" % (instance.pk,)
                filename = '{}.{}.{}'.format(prefix, complaint_id, ext)
            else:
                # set filename as random string
                random_id = "rid_%s" % (uuid4().hex,)
                filename = '{}.{}.{}'.format(prefix, random_id, ext)
                # return the whole path to the file
                today = datetime.datetime.now()
                path = "{year}/{month}/{day}".format(
                year=today.year,
                month=today.month,
                day=today.day,
                )
            return os.path.join(path, filename)
        return wrapper


    charityapp = models.ForeignKey(Charityapp, on_delete=models.CASCADE)
    upload_1 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name=" إرفاق صورة من البطاقة الشخصية أو جواز السفر", null=True, blank=True)
    upload_2 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق شهادة راتب أو شهادة راتب تقاعدي وان كان لايعمل شهادة إثبات من القوى العامل",null=True, blank=True)
    upload_3 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق صورة من شهادة الوفاة أو عقد الزواج أو وثيقة الطلاق", null=True, blank=True)
    upload_4 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق صور من البطاقات الشخصية أو جوازات السفر لأفراد الأسرة الكبار", null=True, blank=True)
    upload_5 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق صور شهادات الميلاد لأفراد الأسرة الصغار", null=True, blank=True)
    upload_6 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق صورة بطاقة الضمان الإجتماعي إن وجدت", null=True, blank=True)
    upload_7 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name=" (إرفاق إثبات من من الأحوال المدنية موضح فيه عدد الأبناء -( إختياري", null=True, blank=True)
    upload_8 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق صورة من الملكية أو عقد الإيجار", null=True, blank=True)
    upload_9 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name=" إرفاق كشف الحساب للقرض البنكي أو المديونيات لأفراد الأسرة أو الاستقطاعات التمويلية", null=True, blank=True)
    upload_10 =models.FileField(upload_to=path_and_rename('app_upload','charity'), verbose_name="إرفاق صورة من التقرير الطبي", null=True, blank=True)


    def __str__(self):
        return self.post

    # def path_and_rename(instance, filename):
    #     upload_to = 'app_upload/%Y/%m/%d'
    #     ext = filename.split('.')[-1]
    #     # get filename
    #     if instance.pk:
    #         filename = '{}.{}'.format(instance.pk, ext)
    #     else:
    #         # set filename as random string
    #         filename = '{}.{}'.format(uuid4().hex, ext)
    #     # return the whole path to the file
    #     return os.path.join(upload_to, filename)

    # def path_and_rename(path):
    #     def wrapper(instance, filename):
    #         ext = filename.split('.')[-1]
    #         # get filename
    #         if instance.pk:
    #             filename = '{}.{}'.format(instance.pk, ext)
    #         else:
    #             # set filename as random string
    #             filename = '{}.{}'.format(uuid4().hex, ext)
    #         # return the whole path to the file
    #         return os.path.join(path, filename)
    #     return wrapper



class Salct(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    health = models.TextField(blank=True, null=True)
    debt = models.TextField(blank=True, null=True)
    housing = models.TextField(blank=True, null=True)
    totalicone = models.TextField(blank=True, null=True)
    familyno = models.TextField(blank=True, null=True)
    soc = models.TextField(blank=True, null=True)
    helptype = models.TextField(db_column='Helptype', blank=True, null=True)  # Field name made lowercase.
    tel = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    upload_2 = models.TextField(blank=True, null=True)
    upload_4 = models.TextField(blank=True, null=True)
    upload_3 = models.TextField(blank=True, null=True)
    upload_1 = models.TextField(blank=True, null=True)
    upload_9 = models.TextField(db_column='Upload_9', blank=True, null=True)  # Field name made lowercase.
    upload_8 = models.TextField(db_column='Upload_8', blank=True, null=True)  # Field name made lowercase.
    upload_5 = models.TextField(blank=True, null=True)
    upload_7 = models.TextField(db_column='Upload_7', blank=True, null=True)  # Field name made lowercase.
    upload_6 = models.TextField(db_column='Upload_6', blank=True, null=True)  # Field name made lowercase.
    upload_10 = models.TextField(blank=True, null=True)
    upload_11 = models.TextField(blank=True, null=True)
    charityapp_id = models.IntegerField(blank=True, null=True)