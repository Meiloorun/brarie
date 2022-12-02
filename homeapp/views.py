from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'homeapp/home.html', context)

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = name + ':\n' + form.cleaned_data['message']
            try:
                send_mail(subject, message, email,['myemail@mydomain.com'])
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'Message Not Sent')
                return HttpResponse("Invalid header found.")
            messages.add_message(request, messages.SUCCESS, 'Message Sent')
            return redirect(reverse('home')) 
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Message Not Sent') 
    return render(request, 'homeapp/contact.html', {"form": form})