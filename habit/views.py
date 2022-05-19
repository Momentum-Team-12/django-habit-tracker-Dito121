from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import HabitForm
from .models import User, Habit, DateRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def list_habits(request):
    logout(request)
    return redirect("log_out")


@login_required
def list_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, "habit/list_habits.html", {'habits': habits})


@login_required
def habit_details(request, pk):
    habit = Habit.objects.get(pk=pk)
    # date_records = DateRecord.objects.filter(habit=request.habit)
    return render(request, "habit/habit_details.html", {'habit': habit})


@login_required
def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='list_habits')

    return render(request, "habit/add_habit.html", {"form": form})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='list_habits')

    return render(request, "habit/edit_habit.html", {
        "form": form,
        "habit": habit,
    })


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')

    return render(request, "habit/delete_habit.html", {"habit": habit})
