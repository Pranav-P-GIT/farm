from django.shortcuts import render,redirect
from .models import comment
from home.models import FarmProduct
from django.http.response import JsonResponse

# Create your views here.

def product(request):
    id=request.GET["id"]
    data=FarmProduct.objects.get(id=id)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    
    Comment=comment.objects.filter(pro_id=id)
    if "his" in request.session:
        if id in request.session["his"]:
            request.session["his"].remove(id)
            request.session["his"].insert(0, id)
        else:
            request.session["his"].insert(0, id)
        if len(request.session["his"]) > 4:
                request.session["his"].pop()
        print(request.session["his"])
        recent = FarmProduct.objects.filter(id__in=request.session["his"])
        print(recent)
        request.session.modified = True
        return render(request, "product.html", {"det": data, "total": total, "recent": recent,"comment":Comment})

    else:
        print("hello")
        request.session["his"] = [id]
        print(request.session["his"])
        return render(request, "product.html", {"det": data, "total": total,"comment":Comment})


def Cmt(request):
    comments=request.POST["comment"]
    name=request.POST["user"]
    id=request.POST["id"]
    mt=comment.objects.create(cmnt=comments,name=name,pro_id=id)
    mt.save();
    return redirect("/product/?id="+id)


def search(request):
    
       



    return render(request, "search.html")


def autosearch(request):
    if 'term' in request.GET:
        a = request.GET["term"]
        
        pro = FarmProduct.objects.filter(name__istartswith=a)
        li=[]
        for i in pro:
            li.append(i.name)
        print(li)
        return JsonResponse(li,safe=False)

        

    