from django.shortcuts import render, redirect
from django.views import View

from comments_app.forms.new_comment import AddCommentsForm
from publication_app.models import Post


class PostView(View):
    @staticmethod
    def get(request, pk):
        posts = Post.objects.get(pk=pk)
        form = AddCommentsForm()

        context = {
            'title': 'Пост',
            'name_text': 'Публикации',
            'posts': posts,
            'form': form
        }
        return render(request, 'publication_app/post.html', context)

    @staticmethod
    def post(request, pk):
        new_request = request.POST.copy()
        new_request['user'] = request.user.pk
        new_request['post'] = pk

        form = AddCommentsForm(data=new_request)
        if form.is_valid:
            form.save()
            return redirect(f'/post/{pk}')
