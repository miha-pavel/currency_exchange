from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from .forms import CustomUserCreationForm, ContactForm
from .tasks import send_mail_task


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        send_mail_task.delay(
            subject=form.cleaned_data.get('title'),
            message=form.cleaned_data.get('text'),
            from_email=form.cleaned_data.get('email'))
        return super().form_valid(form)
