# Generated by Django 3.0.5 on 2020-04-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charityapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='الأسم الثلاثي و القبيلة')),
                ('tel', models.CharField(blank=True, max_length=300, null=True, verbose_name='رقم الهاتف')),
                ('health', models.CharField(blank=True, max_length=300, null=True, verbose_name='هل أحد أفراد الأسرة يعاني من مرض مزمن')),
                ('debt', models.CharField(blank=True, max_length=300, null=True, verbose_name='قيمة المديونيات')),
                ('housing', models.CharField(choices=[('ملك', 'ملك'), ('إيجار', 'إيجار')], default='1', max_length=10, verbose_name='نوع السكن')),
                ('totalicone', models.CharField(blank=True, max_length=300, null=True, verbose_name='إجمالي دخل الأسرة')),
                ('familyno', models.CharField(blank=True, max_length=300, null=True, verbose_name='عدد أفراد الأسرة')),
                ('soc', models.CharField(blank=True, max_length=300, null=True, verbose_name='الحالة الإجتماعية لطالب المساعدة')),
                ('Helptype', models.CharField(blank=True, max_length=300, null=True, verbose_name='نوع المساعدة المطلوبة')),
            ],
            options={
                'ordering': ('dt',),
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regdt', models.DateTimeField(auto_now_add=True)),
                ('gov', models.CharField(blank=True, max_length=50, null=True, verbose_name='المحافظة')),
                ('wly', models.CharField(blank=True, max_length=50, null=True, verbose_name='الولاية')),
                ('vill', models.CharField(blank=True, max_length=50, null=True, verbose_name='القرية')),
                ('stre', models.CharField(blank=True, max_length=50, null=True, verbose_name='الشارع')),
                ('ftype', models.CharField(blank=True, max_length=50, null=True, verbose_name='فئة الأسرة')),
                ('hasname', models.CharField(blank=True, max_length=300, null=True, verbose_name='إسم الزوج')),
                ('hasnat', models.CharField(blank=True, max_length=50, null=True, verbose_name='جنسية الزوج')),
                ('hasid', models.CharField(blank=True, max_length=50, null=True, verbose_name='الرقم المدني')),
                ('hasmobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='هاتف الزوج')),
                ('hasstatus', models.CharField(max_length=50, null=True, verbose_name='حالة الزوج')),
                ('hasstatus_others', models.TextField(null=True, verbose_name='أخري')),
                ('wfname', models.CharField(blank=True, max_length=300, null=True, verbose_name='إسم الزوجة')),
                ('wfnat', models.CharField(blank=True, max_length=50, null=True, verbose_name='جنسية الزوجة')),
                ('wfid', models.CharField(blank=True, max_length=50, null=True, verbose_name='الرقم المدني')),
                ('wfmobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم الهاتف')),
                ('wfstatus', models.CharField(blank=True, max_length=300, null=True, verbose_name='حالة الزوجة')),
                ('wfstatus_others', models.TextField(null=True, verbose_name='أخرى')),
                ('orph', models.CharField(max_length=300, null=True, verbose_name='إسم ولي أمر الأيتام أو الوكيل')),
                ('orph_id', models.CharField(max_length=50, null=True, verbose_name='الرقم المدني')),
                ('orph_rel', models.CharField(max_length=50, null=True, verbose_name='صلة القرابة')),
                ('orphmobile', models.CharField(max_length=50, null=True, verbose_name='رقم الهاتف')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyAssit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assit_private_cars', models.IntegerField(blank=True, null=True, verbose_name='السيارات الخاصة')),
                ('assit_taxi', models.IntegerField(blank=True, null=True, verbose_name='تاكسي')),
                ('assit_school_bus', models.IntegerField(blank=True, null=True, verbose_name='حافلات المدرسة')),
                ('assit_gaz_car', models.IntegerField(blank=True, null=True, verbose_name='سيارات الغاز')),
                ('assit_others', models.TextField(null=True, verbose_name='أخرى')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housetype', models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع السكن')),
                ('houseothers', models.CharField(blank=True, max_length=50, null=True, verbose_name='أخرى')),
                ('houseontype', models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع حيازة السكن')),
                ('houseroom_n', models.IntegerField(blank=True, null=True, verbose_name='عددالغرف')),
                ('housersetting_n', models.IntegerField(blank=True, null=True, verbose_name='عددالمجالس')),
                ('housekitten_n', models.IntegerField(blank=True, null=True, verbose_name='عددالمطابخ')),
                ('housebath_n', models.IntegerField(blank=True, null=True, verbose_name='عددالحمامات')),
                ('houserent_t', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبالغ الإيجار الشهري')),
                ('houserent_r', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='المتبقي من الإيجار الشهري')),
                ('houseelec_r', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبالغ فاتورة الكهرباء')),
                ('housewater_r', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبالغ فاتورةالمياة')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainIncom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ الراتب')),
                ('retirIncom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ التقاعد')),
                ('insuIncom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='الضمان')),
                ('sctIncom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ فريق صلالة الخيري')),
                ('othersIncom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبالغ أخرى')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loantype', models.IntegerField(blank=True, null=True, verbose_name='نوع القرض')),
                ('nameloner', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='إسم الجهة المناعة للقرض أو التمويل')),
                ('totalloan', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ القرض')),
                ('instllament', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='القسط الشهري')),
                ('balanc', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='المبلغ المتبقي')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhouse_no', models.IntegerField(blank=True, null=True, verbose_name='عدد أفراد الأسرة المقيمين بالمنزل بصفة دائمة')),
                ('above18', models.IntegerField(blank=True, null=True, verbose_name='عدد الأبناء فوق سن ١٨ سنة')),
                ('study_elm', models.IntegerField(blank=True, null=True, verbose_name='عدد الطلبة في الجامعي')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMemberDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=300, null=True, verbose_name='الأسم الثلاثي و القبيلة')),
                ('rel', models.CharField(blank=True, max_length=50, null=True, verbose_name='صلة القرابة')),
                ('familystatus', models.CharField(blank=True, max_length=300, null=True, verbose_name='الحالة الإجتماعية')),
                ('dateofbirth', models.CharField(blank=True, max_length=50, null=True, verbose_name='سنة الميلاد')),
                ('education', models.CharField(blank=True, max_length=50, null=True, verbose_name='المرحلة الدراسية')),
                ('job', models.CharField(blank=True, max_length=50, null=True, verbose_name='الوظيفة')),
                ('jobplace', models.CharField(blank=True, max_length=50, null=True, verbose_name='جهة العمل')),
                ('montlyincom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ الدخل الشهري')),
                ('loan', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ القرض')),
                ('installment', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='مبلغ القسط الشهري')),
                ('loandesc', models.TextField(blank=True, null=True, verbose_name='سبب القرض')),
                ('healthstatus', models.TextField(blank=True, null=True, verbose_name='إسم الحالة الصحية')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyNeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_supply', models.BooleanField(default=False, verbose_name='كفالة مواد غذائية')),
                ('orp_care', models.BooleanField(default=False, verbose_name='كفالة أسر أيتام')),
                ('elec_needs', models.TextField(blank=True, null=True, verbose_name='المواد الكهربائية')),
                ('furn_needs', models.TextField(blank=True, null=True, verbose_name='الأثاث المنزلي')),
                ('other_needs', models.TextField(blank=True, null=True, verbose_name='متطلبات أخري')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='الإسم')),
                ('nationality', models.CharField(choices=[('اليمن', 'اليمن'), ('مصر', 'مصر'), ('السودان', 'السودان'), ('الأردن', 'الأردن'), ('فلسطين', 'فلسطين'), ('سوريا', 'سوريا'), ('العراق', 'العراق'), ('تونس', 'تونس'), ('الجرائر', 'الجزائر'), ('المغرب', 'المغرب'), ('ليبيا', 'ليبيا'), ('الهند', 'الهند'), ('باكستان', 'باكستان'), ('بنجلاديش', 'بنجلاديش'), ('الفليبين', 'الفليبين'), ('سيرلانا', 'سيرلانكا'), ('أثيوبيا', 'أثيوبيا'), ('الصومال', 'الصومال'), ('إلتيريا', 'إلتيريا'), ('تركيا', 'تركيا'), ('لبنان', 'لبنان')], default='1', max_length=20, verbose_name='الجنسية')),
                ('cardid', models.CharField(default='12', max_length=50, verbose_name='رقم البطاقة')),
                ('uploadImg', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder')),
                ('helptype', models.CharField(choices=[('غذائية', 'غذائية'), ('مالية', 'مالية'), ('صحية', 'صحية'), ('أخرى', 'أخرى')], default='1', max_length=10, verbose_name='نوع المساعدة')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
            ],
            options={
                'ordering': ('dt',),
            },
        ),
        migrations.CreateModel(
            name='FamilyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_report', models.TextField(blank=True, null=True, verbose_name='تقرير الباحث الإجتماعي عن حالة الأسرة')),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghelp.Family')),
            ],
        ),
        migrations.CreateModel(
            name='Charityappfiels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_1', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name=' إرفاق صورة من البطاقة الشخصية أو جواز السفر')),
                ('upload_2', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق شهادة راتب أو شهادة راتب تقاعدي وان كان لايعمل شهادة إثبات من القوى العامل')),
                ('upload_3', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق صورة من شهادة الوفاة أو عقد الزواج أو وثيقة الطلاق')),
                ('upload_4', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق صور من البطاقات الشخصية أو جوازات السفر لأفراد الأسرة الكبار')),
                ('upload_5', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق صور شهادات الميلاد لأفراد الأسرة الصغار')),
                ('upload_6', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق صورة بطاقة الضمان الإجتماعي إن وجدت')),
                ('upload_7', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name=' (إرفاق إثبات من من الأحوال المدنية موضح فيه عدد الأبناء -( إختياري')),
                ('upload_8', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق صورة من الملكية أو عقد الإيجار')),
                ('upload_9', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name=' إرفاق كشف الحساب للقرض البنكي أو المديونيات لأفراد الأسرة أو الاستقطاعات التمويلية')),
                ('upload_10', models.FileField(blank=True, null=True, upload_to='charity_apps/%Y/%m/%d', verbose_name='إرفاق صورة من التقرير الطبي')),
                ('charityapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghelp.Charityapp')),
            ],
        ),
    ]
