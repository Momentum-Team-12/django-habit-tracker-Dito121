from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import HabitForm
from .models import CustomUser, Habit, DateRecord

def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habit/list_habits.html", {'habits': habits})


def habit_details(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, "habit/habit_details.html", {'habit': habit})


def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habit/add_habit.html", {"form": form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habit/edit_habit.html", {
        "form": form,
        "habit": habit,
    })


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')

    return render(request, "habit/delete_habit.html", {"habit": habit})
