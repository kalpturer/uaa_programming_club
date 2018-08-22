from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Post, Tag, Comment
from django.utils.decorators import method_decorator
from .forms import CommentForm
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def codefest(request, year):
    range = ["1", "2", "3", "4", "5"]
    return render(request, 'codefest.html', {'year': year, "range": range})

@method_decorator(login_required, name='dispatch')
class post_list_view(generic.ListView):
    model = Post
    template_name = 'announcements.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()

@method_decorator(login_required, name='dispatch')
class post_detail_view(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})
