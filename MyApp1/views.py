from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    result = None

    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        operation = request.POST.get('operation')

        # Perform the selected operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'

    return render(request, 'MyApp1/calculator.html', {'result': result})
