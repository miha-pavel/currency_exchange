from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View, FormView
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomUserCreationForm, SignUpForm, SignUpSMSForm, ConfirmSMSCodeForm
from .tasks import send_mail_task
from .models import User, Contact, ActivationCode, ActivationCodeSMS


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyProfile(UpdateView):
    template_name = 'my_profile.html'
    queryset = User.objects.filter(is_active=True)
    fields = ('email', )
    success_url = reverse_lazy('index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)


class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    fields = ('email', 'title', 'text')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        send_mail_task.delay(
            subject=form.cleaned_data.get('title'),
            message=form.cleaned_data.get('text'),
            from_email=form.cleaned_data.get('email'))
        return super().form_valid(form)


class SignUpDimaView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('login')
    form_class = SignUpForm


class SignUpSMSView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('login')
    form_class = SignUpSMSForm


class Activate(View):
    def get(self, request, activation_code):
        ac = get_object_or_404(
            ActivationCode.objects.select_related('user'),
            code=activation_code, is_activated=False,
        )

        if ac.is_expired:
            raise Http404

        ac.is_activated = True
        ac.save(update_fields=['is_activated'])

        user = ac.user
        user.is_active = True
        user.save(update_fields=['is_active'])
        return redirect('index')


class ConfirmSMSCodeView(FormView):
    form_class = ConfirmSMSCodeForm
    template_name = 'signup.html'

    # def dispatch(self, request, *args, **kwargs):
    #     super().dispatch()

    def post(self, request):
        user_id = request.session['user_id']
        sms_code = request.POST['sms_code']

        ac = get_object_or_404(
            ActivationCodeSMS.objects.select_related('user'),
            code=sms_code,
            user_id=user_id,
            is_activated=False,
        )

        if ac.is_expired:
            raise Http404

        ac.is_activated = True
        ac.save(update_fields=['is_activated'])

        user = ac.user
        user.is_active = True
        user.save(update_fields=['is_active'])
        return redirect('index')
