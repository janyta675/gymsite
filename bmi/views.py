from django.shortcuts import render
import math
# Create your views here.

def bmi(request):
    response="none"
    bmi=0.0
    # my_bmi=list(BMI.items())    
    try:
        if request.method=="POST":
            num1=float(request.POST.get('height'))
            num2=float(request.POST.get('weight'))
            weight = num2 / 2.20462 
            height = num1 * 0.0328084
            fbmi=((((weight / height)* 703) / 10000) - 4.0)
            bmi=round(fbmi, 1)
            if bmi <= 18.5:
                response="Under Weight!!"
            elif bmi>18.5 and bmi<=25:
                response="Normal(Healthy Weight)"
            else:
                response="Overweight!!"
        return render(request,'bmi/bmi.html',{'response':response,'bmi':bmi,})
    except:
        response = "none"
        bmi = 0.0
        # my_bmi=BMI.values()
        return render(request, 'bmi/bmi.html', {'response': response, 'bmi': bmi,})
