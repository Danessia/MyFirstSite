from django.contrib import admin
from .models import Question, Variant, ResultQuestion, Complexity, UserProgress
from .forms import QuestionForm

class VariantAdmin(admin.TabularInline):
    model = Variant
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = (VariantAdmin, )
    fields = ('title', 'question', 'right_variant', 'complexity')
    form = QuestionForm


class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_right')

    def is_right(self, instance):
        return instance.is_right_answer()


class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_level', 'is_done')


admin.site.register(Question, QuestionAdmin)
admin.site.register(ResultQuestion, ResultAdmin)
admin.site.register(Complexity)
admin.site.register(UserProgress, UserProgressAdmin)
