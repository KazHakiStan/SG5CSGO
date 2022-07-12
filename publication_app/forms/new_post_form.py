from django import forms
from publication_app.models import Post


class AddPostForm(forms.ModelForm):
    title = forms.CharField(label='Введите название поста')
    text = forms.CharField(
        label='Введите текст к посту',
        widget=forms.Textarea()
    )
    is_public = forms.BooleanField(
        label='Публичная запись ?',
        initial=True,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', ]


class ImagePostForm(AddPostForm):

    image = forms.ImageField(
        label='Выберите фотографии',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(AddPostForm.Meta):
        fields = AddPostForm.Meta.fields + ['image', ]


