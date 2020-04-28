from django.contrib import admin
from .models import Family, FamilyMember, FamilyMemberDetail, FamilyIncome, FamilyHouse, FamilyAssit, FamilyLoan, FamilyNeeds, FamilyReport, Person, Charityapp,Charityappfiels
# Register your models here.
admin.site.register(Person)
admin.site.register(Family)
admin.site.register(FamilyMember)
admin.site.register(FamilyMemberDetail)
admin.site.register(FamilyIncome)
admin.site.register(FamilyHouse)
admin.site.register(FamilyAssit)
admin.site.register(FamilyLoan)
admin.site.register(FamilyNeeds)
admin.site.register(FamilyReport)
admin.site.register(Charityapp)
admin.site.register(Charityappfiels)