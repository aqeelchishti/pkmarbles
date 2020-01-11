from django.shortcuts import render, render_to_response
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import get_template
from django.views.generic.edit import FormView

from main.forms import ContactForm, SubscribeForm
from main.models import ContactUser, SubscribeUser, Product


def subscribe_mail(self, request):
    form2 = SubscribeForm(request.POST or None)
    if request.method == 'POST':
        if form2.is_valid():
            instance = form2.save(commit=False)
            if SubscribeUser.objects.filter(email=instance.email).exists():
                messages.warning(request, '<div class="form-error">Please provide another email, email already exist.</div>', extra_tags='html_safe')
            else:
                instance.save()
                subject = 'Thank You for Subscribe Our Newsletter'
                email_from = settings.EMAIL_HOST_USER
                to_email = [instance.email]
                join_message = """ Welcome to Pakistan Marbles """
                form2.send_mail(subject=subject, from_email=email_from, recipient_list=to_email, message=join_message, fail_silently=False)
                messages.success(request, '<div class="form-success">Successfully submited</div>', extra_tags='html_safe')

            return HttpResponseRedirect(instance.get_absolute_url())

"""class SubscribeFormView(FormView):
    form_class = SubscribeForm

    def subscribe_mail(self, form2):
        form2 = SubscribeForm(request.POST or None)
        if request.method == 'POST':
            if form2.is_valid():
                instance = form2.save(commit=False)
                if SubscribeUser.objects.filter(email=instance.email).exists():
                    messages.warning(request, '<div class="form-error">Please provide another email, email already exist.</div>', extra_tags='html_safe')
                else:
                    instance.save()
                    subject = 'Thank You for Subscribe Our Newsletter'
                    email_from = settings.EMAIL_HOST_USER
                    to_email = [instance.email]
                    join_message = " Welcome to Pakistan Marbles "
                    form2.send_mail(subject=subject, from_email=email_from, recipient_list=to_email, message=join_message, fail_silently=False)
                    messages.success(request, '<div class="form-success">Successfully submited</div>', extra_tags='html_safe')

                #return HttpResponseRedirect(instance.get_absolute_url())
                return super().subscribe_mail(form2)"""

def home(request):
    form2 = SubscribeForm(request.POST or None)
    subscribe = subscribe_mail(form2, request)
    context = {
      'form2': form2
    }
    return render(request, 'main/home.html', context)

def about(request):
    form2 = SubscribeForm(request.POST or None)
    subscribe = subscribe_mail(form2, request)
    context = {
      'form2': form2
    }
    return render(request, 'main/about.html', context)

def product(request):
    form2 = SubscribeForm(request.POST or None)
    products = Product.objects.all()
    subscribe = subscribe_mail(form2, request)
    context = {
      'products': products,
      'form2': form2
    }
    return render(request, 'main/products.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    form2 = SubscribeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            if ContactUser.objects.filter(email=instance.email).exists():
                messages.warning(request, '<div class="form-error">Please provide another email, email already exist.</div>', extra_tags='html_safe')
            else:
                instance.save()
                subject = 'Thank You for Joining Our Newsletter'
                email_from = settings.EMAIL_HOST_USER
                to_email = [instance.email]
                join_message = """ Welcome to Pakistan Marbles """
                send_mail(subject=subject, from_email=email_from, recipient_list=to_email, message=join_message, fail_silently=False)
                messages.success(request, '<div class="form-success">Successfully submited</div>', extra_tags='html_safe')

            return HttpResponseRedirect(instance.get_absolute_url())

    subscribe = subscribe_mail(form2, request)
    context = {
        'form': form,
        'form2': form2
    }
    template = "main/contacts.html"
    return render(request, template, context)


def portfolio(request):
    form2 = SubscribeForm(request.POST or None)
    subscribe = subscribe_mail(form2, request)
    context = {
      'form2': form2
    }
    return render(request, 'main/portfolio.html', context)
