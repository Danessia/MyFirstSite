from django import forms
from .models import Question, Variant, ResultQuestion


class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['right_variant'].queryset = Variant.objects.filter(question=self.instance)
        else:
            self.fields['right_variant'].queryset = Variant.objects.none()

    class Meta:
        model = Question
        fields = ('title', 'question', 'right_variant', 'complexity')


class ResultQuestionForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Variant.objects.none(),
        required=True,
        widget=forms.RadioSelect(),
        empty_label=None,
    )
    question = forms.ModelChoiceField(
        queryset=Question.objects.all(),
        widget=forms.HiddenInput(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(ResultQuestionForm, self).__init__(*args, **kwargs)
        self.fields['answer'].queryset = Variant.objects.filter(question=self.initial['question'])

    class Meta:
        model = ResultQuestion
        fields = ('question', 'answer')


class ClearResults(forms.Form):
    clear = forms.BooleanField()
