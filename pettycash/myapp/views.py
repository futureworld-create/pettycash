
# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .forms import RegisterModelForm
from .models import *
from django.db.models import Sum

def home(request):
    """Home page view"""
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash the password
            user.save()
              # optional: auto-login after registration
            return redirect('login_user')  # or home/dashboard
    else:
        form = RegisterModelForm()
    
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('submit_expense')  # Redirect after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect after logout

@login_required
def submit_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.submitted_by = request.user
            expense.save()
            return HttpResponse("success") # replace with your actual URL name
    else:
        form = ExpenseForm()
    return render(request, 'expenses/submit_expense.html', {'form': form})


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(submitted_by=request.user).order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def petty_cash_summary(request):
    # Get latest petty cash amount (if model exists)
    petty_cash = PettyCash.objects.last()
    print(petty_cash)
    total_cash = petty_cash.total_cash if petty_cash else 10000  # fallback to 10k

    # Total expenses made
    total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0

    # Remaining cash
    balance = total_cash - total_expenses

    return render(request, 'expenses/petty_cash_summary.html', {
        'total_cash': total_cash,
        'total_expenses': total_expenses,
        'balance': balance
    })