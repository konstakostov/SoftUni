from filecmp import clear_cache
from importlib.metadata import requires
from importlib.resources import contents

from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from django.template.defaultfilters import title

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


class PostAuthorForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': "Enter your post title.",
                'max_length': f"Title is too long. Please, keep it under {Post.TITLE_MAX_LENGTH} characters!"
            },
            'author': {
                'required': "Please, enter and author",
            },
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author[0].isupper():
            raise ValidationError('Author name should start with a capital letter.')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('name')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError('The post title cannot be included in the post description.')

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    disabled_fields = (
        # '__all__',
    )


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'get'
    #     self.helper.form_class = 'form_inline'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': {
                'required': "Author name is required!",
            },
            'content': {
                'required': "Content is required!"
            },
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message...',
        })


CommentFormSet = formset_factory(CommentForm, extra=1)


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices
#     )