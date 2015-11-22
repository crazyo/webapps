from django.shortcuts import render

from .models import *
from django.db.models import Sum

def portfolio(request):
    dict = []
    dict.append(["Total", "Revenue"])
    topCategory = TopCategory.objects.all()
    for ele in topCategory:
        dict.append([ele.name, float(SubCategory.objects.filter(top_category=ele).aggregate(Sum('revenue'))['revenue__sum'])])


    data = get_sub_chart("Fixed Income")

    context = {"top_data":dict, 'fixed_income': data}
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





def return_rate_by_date(request):
      #get all referring sites
    ReferringSites  = ReturnRate.objects.all()
    column = []
    #loop through referring sites

    for element in ReferringSites:
        column.append([element.url.encode("utf-8"), Article.objects.filter(url = element.url).count(), element.name.encode("utf-8")])

    #sort the referring sites by the number of articles they have.
    column.sort(key = lambda x: x[1], reverse=True)
    #get top 10 referring sites based on the number of articles
    column = column[0:10]
    msites_name = []
    for a in range(len(column)):
        msites_name.append(column[a][2])

    for a in range(len(column)):
        column[a] = column[a][0]

    data = []

    pre_date = None

    #loop through articles
    for art in Article.objects.all():
        new=[]
        #get day month, and year of each article
        date = art.date_added.strftime("%B %d, %Y")
        day = art.date_added.strftime("%d")
        month = art.date_added.strftime("%m")
        year = art.date_added.strftime("%Y")

        if date != pre_date:
            pre_date = date
            new.append(date)
            for url in column:
                #count the number of articles added on that day, and add to the list.
                new.append(Article.objects.filter(domain = url, date_added__day = day, date_added__month = month, date_added__year = year).count())
            data.append(new)

    return msites_name, data





    return render(request, 'portfolio/_chart.html', context)















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

    data = get_sub_chart("Alternative")
    context = {'alternative': data}
    return render(request, 'portfolio/_chart.html', context)



def cash(request):

    data = get_sub_chart("Cash and Cash Eq")
    context = {'cash': data}
    return render(request, 'portfolio/_chart.html', context)