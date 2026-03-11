from django.shortcuts import render
from django.http import HttpResponse

def enroll(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName', "").strip()
        lastName = request.POST.get('lastName', "").strip()
        age = request.POST.get('age', "").strip()
        gender = request.POST.get('gender', "").strip()

        student = Student.objects.create(
            firstName=firstName,
            lastName=lastName,
            age=int(age) if age else 0,
            gender=gender
        )

        info = {
            "submitted": True,
            "firstName": firstName,
            "lastName": lastName,
            "age": age,
            "gender": gender,
        }

        return render(request, 'enroll.html', info)
    
    return render(request, 'enroll.html')





