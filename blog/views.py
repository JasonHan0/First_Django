from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):

    # select * from Post;
    posts = Post.objects.all().order_by('-pk')
    # 기본 값은 오름차순 .order_by('-pk') 하면 내림차순(최신 포스트부터 보기)

    return render(
        request,  # 사용자가 요청하면 요청자에게 하기 html을 줌으로써 응답한다.
        # django 앞에서 자동으로 /templates/ 라는 경로를 붙여준다

        'blog/index.html',
        {
            'posts': posts
        }
    )
# pk 같이 클라이언트가 서버에 보내는 데이터 : parameter
# post, posts 등 서버가 클라이언트에 보내는 데이터 : attribute
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )