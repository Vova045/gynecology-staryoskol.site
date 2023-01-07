from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

   
def send_recall_message(request):
    if request.method == 'POST':
        subject='Заявка на звонок'
        telephone = request.POST.get('recall_phone')
        time = request.POST.get('recall_time')
        check = request.POST.get('recall_time_check')
        form_email = settings.EMAIL_HOST_USER
        to='vovatsar@bk.ru'
        recall_time_check=f"Нужно перезвонить в ближайшее время"
        recall_time=f"Нужно перезвонить в {time}."
        if check != None:
            need_msg = recall_time_check
        else:
            need_msg = recall_time
        msg=(f"<p>Поступила заявка на звонок от {telephone}.{need_msg}</p>")
        msg = EmailMultiAlternatives(subject,msg,form_email,[to])
        msg.content_subtype='html'
        msg.send()
        return render(request,"home.html", {'telephone': telephone})
    else:
        return render (request, 'home.html',) 

def send_ask_message(request):
    if request.method == 'POST':
        subject='Новый вопрос'
        firstname = request.POST.get('ask_modal_firstname')
        lastname = request.POST.get('ask_modal_lastname')
        mail = request.POST.get('ask_modal_mail')
        phone = request.POST.get('ask_modal_phone')
        message = request.POST.get('ask_modal_message')
        form_email = settings.EMAIL_HOST_USER
        to='vovatsar@bk.ru'
        msg=(f"<p>Поступила новый вопрос на сайте от {lastname}{firstname}.Текст такой:{message}.<br> Электронная почта:{mail},Телефонный номер:{phone}</p>")
        msg = EmailMultiAlternatives(subject,msg,form_email,[to])
        msg.content_subtype='html'
        msg.send()
        return render(request,"home.html", {'mail': mail})
    else:
        return render (request, 'home.html',) 


def home(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        else:
            return send_recall_message(request)
    return render (request, 'home.html',) 
def diagnostics(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'diagnostics.html',) 
def for_clients(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'for_clients.html',) 
def department(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'department.html',) 
def hospital(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'hospital.html',) 
def contacts(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'contacts.html',) 
def services(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'services.html',) 
def doctors(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'doctors.html',) 
def questions_and_answers(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'questions_and_answers.html',) 
def privacy_policy(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'privacy_policy.html',) 
def paid_services(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'paid_services.html',) 
def consultations(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'consultations.html',) 
def surgery(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'surgery.html',) 
def client_support(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'client_support.html',) 
def hospital_support(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'hospital_support.html',) 
def emergency_care(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'emergency_care.html',) 
def non_resident_clients(request):
    if request.method == "POST":
        return send_recall_message(request)
    return render (request, 'non-resident_clients.html',) 
