from django.shortcuts import get_object_or_404, render
from blog import metrics
from django.views import generic 
from .models import Post


def postList(request):
    metrics.custom_home_page_views.inc()
    post_list= Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'index.html', {'post_list':post_list})

def postDetail(request, post):
    metrics.custom_post_detail_views.inc()
    zpost = get_object_or_404(Post, slug=post, status=1)
    return render(request, 'post_detail.html', {'post': zpost})

# class PostList(generic.ListView):
#     # metrics.home_page_views.inc()
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
    
# class PostDetails(generic.DetailView):
#     # metrics.post_detail_views.inc()
#     model = Post
#     print('\n\nPOST OPEN\n\n')
#     template_name = 'post_detail.html'