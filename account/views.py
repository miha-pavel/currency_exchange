from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .forms import CustomUserCreationForm
from .tasks import send_mail_task
from .models import User, Contact


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyProfile(UpdateView):
    template_name = 'my_profile.html'
    queryset = User.objects.filter(is_active=True)
    fields = ('email', )
    success_url = reverse_lazy('index')


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
