from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Проверяем, что есть хотя бы один основной раздел
        is_main_count = 0
        for form in self.forms:
            # Проверяем, что форма не пустая и не помечена на удаление
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_main'):
                    is_main_count += 1

        # Если нет основного раздела
        if is_main_count == 0:
            raise ValidationError('Необходимо выбрать один основной раздел')

        # Если больше одного основного раздела
        if is_main_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'published_at']
    list_filter = ['published_at']
    search_fields = ['title', 'text']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']