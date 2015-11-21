from django.shortcuts import render

from .models import *


def portfolio(request):

    return render(request, 'portfolio/_chart.html', {})




def get_sub_chart(category):
    dict =[]
    title = [category, 'Revenue']
    dict.append(title)
    topCategory = TopCategory.objects.get(name=category)
    subCategories = SubCategory.objects.filter(top_category = topCategory)
    for ele in subCategories:
        dict.append([ele.name, float(ele.revenue)])
        print (dict)
    return dict



def fixed_income(request):

    data = get_sub_chart("Fixed Income")
    context = {'fixed_income': data}
    return render(request, 'portfolio/_chart.html', context)


def stock(request):

    data = get_sub_chart("Stock")
    context = {'stock': data}
    return render(request, 'portfolio/_chart.html', context)


def alternative(request):

    data = get_sub_chart("Derivatives")
    context = {'derivatives': data}
    return render(request, 'portfolio/_chart.html', context)


def cash(request):

    data = get_sub_chart("Cash and Cash Eq")
    context = {'cache': data}
    return render(request, 'portfolio/_chart.html', context)
