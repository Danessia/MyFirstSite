from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, ResultQuestion, UserProgress, Complexity
from .forms import ResultQuestionForm, ClearResults
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# Create your views here.
def post_list(request):
    posts = Question.objects.all()
    return render(request, 'test/post_list.html', {'posts': posts})


def quiz(request):
    progress, _ = UserProgress.objects.get_or_create(user=request.user)
    if not progress.current_level:
        current_level = Complexity.objects.all().order_by('level').first()
        progress.current_level = current_level
        progress.save()

    answers = ResultQuestion.objects.filter(
        user=request.user,
        attempt=progress.attempt,
        question__complexity=progress.current_level
    )
    available_questions = Question.objects.filter(
        complexity=progress.current_level
    ).exclude(
        resultquestion__attempt__lt=progress.attempt
    )
    max_series = min(progress.current_level.series, available_questions.count())
    if available_questions.count() > 0 and answers.count() >= max_series:
        right_answers = list(filter(lambda a: a.is_right_answer(), answers))
        if len(right_answers) < max_series * 0.66:
            if progress.attempt == 0:
                progress.attempt += 1
                progress.save()
            else:
                current_level = progress.current_level.get_previous_level() or progress.current_level
                progress.current_level = current_level
                progress.is_done = True
                progress.save()
                return redirect(reverse('results'))
        else:
            current_level = progress.current_level.get_next_level()
            if current_level:
                progress.current_level = current_level
                progress.attempt = 0
                progress.save()
            else:
                progress.is_done = True
                progress.save()
                return redirect(reverse('results'))

    if progress.current_question:
        question = progress.current_question
    else:
        question = Question.objects.filter(
            complexity=progress.current_level
        ).exclude(
            resultquestion__user=request.user
        ).order_by('?').first()
        progress.current_question = question
        progress.save()

    if not question:
        current_level = progress.current_level.get_previous_level() or progress.current_level
        progress.current_level = current_level
        progress.is_done = True
        progress.save()
        return redirect(reverse('results'))

    initial = {'question': question}
    if request.method == 'GET':
        form = ResultQuestionForm(initial=initial)
        return render(request, 'test/quiz.html', {'form': form, 'question': question})
    else:
        form = ResultQuestionForm(request.POST, initial=initial)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.save()

            progress.current_question = None
            progress.save()

            return HttpResponseRedirect('/quiz/')
        else:
            return render(request, 'test/quiz.html', {'form': form, 'question': question})


def clear_view(request):
    if request.method == 'GET':
        form = ClearResults()
        return render(request, 'test/clear_form.html', {'form': form})
    else:
        form = ClearResults(request.POST)
        if form.is_valid():
            ResultQuestion.objects.filter(user=request.user).delete()
            UserProgress.objects.filter(user=request.user).delete()
            return redirect('/')
        else:
            return render(request, 'test/clear_form.html', {'form': form})


def result_view(request):
    progress, _ = UserProgress.objects.get_or_create(user=request.user)
    return render(request, 'test/results.html', {'progress': progress})
