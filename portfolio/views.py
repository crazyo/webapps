import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from django.db.models import Sum

current_sections = []

def portfolio(request):
    dict = []
    dict.append(["Total", "Revenue"])
    topCategory = TopCategory.objects.all()
    for ele in topCategory:
        dict.append([ele.name, float(SubCategory.objects.filter(top_category=ele).aggregate(Sum('revenue'))['revenue__sum'])])


    # data = get_sub_chart("Fixed Income")

    global current_sections
    current_sections = [x[0] for x in dict[1:]]
    context = {"top_data":dict}
    return render(request, 'portfolio/_chart.html', context)


def comparasion(request):
    dict = []
    dict.append(["Total", "Revenue"])
    topCategory = TopCategory.objects.all()
    for ele in topCategory:
        dict.append([ele.name, float(SubCategory.objects.filter(top_category=ele).aggregate(Sum('revenue'))['revenue__sum'])])


    data = get_sub_chart("Fixed Income")

    context = {"top_data":dict, 'fixed_income': data}
    return render(request, 'portfolio/_comparasion.html', context)


def get_sub_chart(request):
    index = int(request.GET.get('index'))
    category = current_sections[index]
    dict = []
    title = [category, 'Revenue']
    dict.append(title)
    topCategory = TopCategory.objects.get(name=category)
    subCategories = SubCategory.objects.filter(top_category = topCategory)
    for ele in subCategories:
        dict.append([ele.name, float(ele.revenue)])
        # print (dict)
    return HttpResponse(
        json.dumps({'data': dict, 'title': category}),
        content_type="application/json"
    )



# def fixed_income(request):

#     data = get_sub_chart("Fixed Income")
#     context = {'fixed_income': data}
#     return render(request, 'portfolio/_chart.html', context)


# def stock(request):

#     data = get_sub_chart("Stock")
#     context = {'stock': data}
#     return render(request, 'portfolio/_chart.html', context)


# def alternative(request):

#     data = get_sub_chart("Alternative")
#     context = {'alternative': data}
#     return render(request, 'portfolio/_chart.html', context)



# def cash(request):

#     data = get_sub_chart("Cash and Cash Eq")
#     context = {'cash': data}
#     return render(request, 'portfolio/_chart.html', context)
