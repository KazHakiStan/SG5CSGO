from django.shortcuts import render, redirect
from django.views import View

from publication_app.forms.new_post_form import ImagePostForm
from publication_app.models import Post, ImagePost


class AddPost(View):
    @staticmethod
    def get(request):
        form = ImagePostForm()

        context = {
            'title': 'Добавление нового поста',
            'form': form
        }

        return render(request, 'publication_app/new_post.html', context)

    @staticmethod
    def post(request):

        form = ImagePostForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('image')
        if len(files) > 4:
            raise Exception("Я вам запрещаю прикреплять больше 4ех картинок")

        if form.is_valid():
            tags = form.cleaned_data.get('tag')
            post_obj = Post.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                is_public=form.cleaned_data['is_public'],
            )

            for file in files:
                ImagePost.objects.create(
                    post=post_obj,
                    image=file
                )

            for tag in tags:
                post_obj.tag.add(tag)

            return redirect('posts')

        else:
            context = {
                'title': 'Добавление нового поста',
                'form': form
            }
            return render(request, 'publication_app/new_post.html', context)