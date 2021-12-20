from django.shortcuts import render

# Create your views here.


def play(request):
    secret_numbers = [2, 3, 5, 7]
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        bull_cow = []
        count = ''
        numbers = int(request.POST.get('numbers'))
        numbers = list(map(int, ['numbers'][0].split()))
        while True:
            for i, j in zip(secret_numbers, numbers):
                if j in secret_numbers:
                    if j == i:
                        bull_cow[0] += 1
                        if bull_cow[0] == 4:
                            count = "You got it right"
                    else:
                        bull_cow[1] += 1
                        count = f"{bull_cow[0]} bulls, {bull_cow[1]} cows"
        context = {
            'numbers': request.POST.get('numbers'),
            'count': count,
            'bull_cow': bull_cow
        }
        return render(request, 'index.html', context)