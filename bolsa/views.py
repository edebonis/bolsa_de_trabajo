from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from bolsa.forms import SignUpForm, NuevaOportunidad
from bolsa.models import Oportunidad, Profile
from bolsa.tokens import account_activation_token
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now



@login_required
def inicio(request):
    context = {'Oportunidad': Oportunidad.objects.all,
               'Usuario': User.objects.all}
    return render(request, 'inicio.html', context)


@login_required
def nueva(request):
    if request.method == "POST":
        form = NuevaOportunidad(request.POST)
        if form.is_valid():
            print("NUEVA")
            try:
                preform = form.save(commit=False)
                preform.user = request.user
                preform.save()
                print("Guardado")
                return redirect('/')
            except:
                print("Error")
                pass
    else:
        form = NuevaOportunidad()

    return render(request, 'nueva_oportunidad.html', {'form': form})




def account_activation_sent(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.profile.es_alumno = False
        user.profile.es_oferente = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'account_activation_invalid.html')


def signup(request):
    if request.method == 'POST':
        print("signup")
        form = SignUpForm(request.POST)

        if form.is_valid():
            print("form is valid")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})