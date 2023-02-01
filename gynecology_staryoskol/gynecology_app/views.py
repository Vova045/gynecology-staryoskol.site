from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import resolve
from django.core.mail import send_mail

def send_recall_message(request):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            telephone = request.POST.get('recall_phone')
            message = request.POST.get('recall_message')
            recall_time_check=f"Нужно перезвонить в ближайшее время"
            need_msg = recall_time_check
            if message == '':
                rcl_msg=(f"Поступила заявка на звонок от {telephone}.{need_msg}")
            else:
                rcl_msg=(f'Поступила заявка на звонок от {telephone}.{need_msg}. Также оставили сообщение"{message}".')
            if str(request.get_full_path()[1:]) == '':
                return render(request,str(resolve(request.path_info).url_name)+'.html', {'rcl_msg': rcl_msg, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
            return render(request,str(request.get_full_path()[1:])+'.html', {'rcl_msg': rcl_msg, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
        if request.POST.get("form_type") == 'formThree':
            subject='Заявка на звонок'
            form_email = settings.EMAIL_HOST_USER
            telephone = "телефон"
            rcl_msg = request.POST.get('g-recaptcha_rcl_msg')
            if request.recaptcha_is_valid:
                send_mail(subject, rcl_msg, form_email,
    ['vovatsar@bk.ru','gynotdelen@mail.ru'], fail_silently=False)
                if str(request.get_full_path()[1:]) == '':
                    return render(request,str(resolve(request.path_info).url_name)+'.html', {'telephone': telephone,'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
                return render(request,str(request.get_full_path()[1:])+'.html', {'telephone': telephone,'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
    else:
        if str(request.get_full_path()[1:]) == '':
            return render (request, str(resolve(request.path_info).url_name)+'.html',) 
        return render(request,str(request.get_full_path()[1:])+'.html')
def send_ask_message(request):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formTwo':
            subject='Новый вопрос'
            firstname = request.POST.get('ask_modal_firstname')
            lastname = request.POST.get('ask_modal_lastname')
            mail = request.POST.get('ask_modal_mail')
            phone = request.POST.get('ask_modal_phone')
            message = request.POST.get('ask_modal_message')
            msg=(f"Поступила новый вопрос на сайте от {lastname}{firstname}.Текст такой:{message}.Электронная почта:{mail},Телефонный номер:{phone}")
            if str(request.get_full_path()[1:]) == '':
                return render(request,str(resolve(request.path_info).url_name)+'.html', {'msg': msg, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
            return render(request,str(request.get_full_path()[1:])+'.html', {'msg': msg, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
        if request.POST.get("form_type") == 'formFour':
            msg = request.POST.get('g-recaptcha_msg')
            subject='Новый вопрос'
            mail = "отправлено"
            form_email = settings.EMAIL_HOST_USER
            if request.recaptcha_is_valid:
                send_mail(subject, msg, form_email,
    ['vovatsar@bk.ru','gynecology-staryoskol@mail.ru'], fail_silently=False)
                if str(request.get_full_path()[1:]) == '':
                    return render(request,str(resolve(request.path_info).url_name)+'.html', {'mail': mail, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
                return render(request,str(request.get_full_path()[1:])+'.html', {'mail': mail, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
    else:
        if str(request.get_full_path()[1:]) == '':
            return render (request, str(resolve(request.path_info).url_name)+'.html',) 
        return render (request, str(request.get_full_path()[1:])+'.html',) 


def home(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'home.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY}) 
def diagnostics(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'diagnostics.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def for_clients(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'for_clients.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def department(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'department.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def hospital(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'hospital.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def contacts(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'contacts.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def services(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'services.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def doctors(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'doctors.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def questions_and_answers(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'questions_and_answers.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def privacy_policy(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'privacy_policy.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def paid_services(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'paid_services.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def consultations(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'consultations.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def surgery(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'surgery.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def client_support(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'client_support.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def hospital_support(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'hospital_support.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def emergency_care(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'emergency_care.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def non_resident_clients(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'non-resident_clients.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def abort(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'articles/abort.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})


def hysteroscopy(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'services/hysteroscopy.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
def laparoscopy(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formTwo':
            return send_ask_message(request)
        elif request.POST.get("form_type") == 'formOne':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formThree':
            return send_recall_message(request)
        elif request.POST.get("form_type") == 'formFour':
            return send_ask_message(request)
    return render (request, 'services/laparoscopy.html', {'site_key': settings.RECAPTCHA_PUBLIC_KEY})
