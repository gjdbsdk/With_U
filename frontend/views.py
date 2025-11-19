from django.views.generic import TemplateView
import datetime     # 'timesince' 필터 및 임시 데이터 생성을 위해 임포트
from django.shortcuts import render, redirect, get_object_or_404 
        # 함수 기반 뷰(FBV) 및 리다이렉트를 위해 임포트
from django.http import Http404
from django import forms
from api.models import Post, Comment


class PostForm(forms.Form):
    title = forms.CharField(label='제목', max_length=200)
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={'rows': 15}))

class HomeView(TemplateView):
    template_name = "home.html"

class LifestyleView(TemplateView):
    template_name = "lifestyle.html"

class SocietyView(TemplateView):
    template_name = "society.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['etiquette_groups'] = [
            {
                'title': '장례 예절',
                'description': '장례식에 참석하거나 조의를 표할 때 필요한 기본적인 예절과 절차를 안내합니다.',
                'icon_path': 'img/funeral.png',  # static/img/funeral.png
                'topics': [
                    {
                        'title': '조의금 봉투 작성법', 
                        'content': '''조의금 봉투 앞면에는 고인을 애도하는 한자를 세로로 작성합니다. 아래 여섯 가지 한자를 많이 사용합니다.\n
• 근조(謹弔) : 죽음에 대해 삼가 슬퍼하는 마음
• 애도(哀悼) : 사람의 죽음에 대해 슬퍼함
• 추모(追慕) : 죽은 사람을 그리며 생각함
• 추도(追悼) : 죽은 사람에 대해 슬퍼함
• 부의(賻儀) : 상가에 부조로 보내는 돈
• 위령(慰靈) : 죽은 사람의 영혼을 위로함\n
뒷면 좌측 하단에 본인의 이름과 소속을 표시합니다. 만약 단체나 소속에서 부의금을 보낸다면, 뒷면에 단체나 회사명만 적어도 무방합니다.'''
                    },
                    {'title': '장례식장 방문 시 기본 예절', 'content': '외투는 문 밖에서 벗고, 영정 앞에서 분향 또는 헌화 후 두 번 절합니다.'},
                    {'title': '헌화 및 분향 순서', 'content': '헌화는 꽃송이가 영정을 향하게 두고, 분향은 향을 1~3개 집어 촛불에 불을 붙인 후 흔들어 끕니다.'},
                ]
            },
            {
                'title': '결혼식 예절',
                'description': '결혼식 참석 시 하객이 지켜야 할 예절과 신랑 신부에게 축하의 마음을 전달하는 방법을 설명합니다.',
                'icon_path': 'img/wedding.png', # static/img/wedding.png
                'topics': [
                    {'title': '하객 복장 가이드', 'content': '신부의 드레스 색인 흰색은 피하고, 단정하고 깔끔한 복장을 선택합니다. 너무 어두운 색도 피하는 것이 좋습니다.'},
                    {'title': '축의금 전달 및 인사', 'content': '축의금은 미리 준비하여 접수대에 이름을 밝히고 전달합니다. 방명록도 잊지 말고 작성합니다.'},
                    {'title': '피로연 예절', 'content': '피로연은 신랑 신부가 하객에게 감사를 표하는 자리입니다. 가벼운 인사와 함께 축하의 말을 전합니다.'},
                ]
            },
            {
                'title': '제례 의식',
                'description': '조상를 기리는 제례 의식의 의미와 기본적인 절차, 예절에 대해 안내합니다.',
                'icon_path': 'img/ancestral.png', # static/img/ancestral.png
                'topics': [
                    {'title': '차례상 차리는 법', 'content': '홍동백서, 조율이시 등 기본적인 원칙이 있으나, 가정의 전통과 형편에 맞게 정성껏 차리는 것이 중요합니다.'},
                    {'title': '차례 시 복장 및 자세', 'content': '단정한 복장을 착용하고 경건한 마음가짐으로 임합니다.'},
                    {'title': '절차와 의의', 'content': '제례는 조상을 기리고 가족 간의 유대를 다지는 중요한 전통 의식입니다.'},
                ]
            },
            {
                'title': '병문안 예절',
                'description': '환자를 방문하여 위로할 때 지켜야 할 예절과 배려심 있는 행동에 대해 안내합니다.',
                'icon_path': 'img/visit.png', # static/img/visit.png
                'topics': [
                    {'title': '방문 시간 및 기간', 'content': '병원의 면회 시간을 꼭 확인하고, 환자의 휴식에 방해가 되지 않도록 30분 내외로 짧게 방문합니다.'},
                    {'title': '선물 선택 가이드', 'content': '꽃이나 향이 강한 음식보다는 환자가 회복기에 먹을 수 있는 주스나 과일 등이 좋습니다.'},
                    {'title': '대화 및 행동 시 주의사항', 'content': '환자의 기분을 살피며 긍정적인 대화를 나누고, 큰 소리로 떠들거나 너무 많은 질문을 하지 않습니다.'},
                    {'title': '병문안 자제의 필요성', 'content': '환자의 상태가 좋지 않거나 감염의 우려가 있을 때는 방문을 자제하고 메시지 등으로 위로를 전하는 것이 좋습니다.'},
                ]
            }
        ]
        return context

class CitizenView(TemplateView):
    template_name = "citizen.html"

# 커뮤니티 리스트 페이지 (DB기반)
class CommunityView(TemplateView):
    template_name = "community/community.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = Post.objects.all().order_by("-created_at")
        user = self.request.user

        # 게시글에 좋아요 눌렀는지 확인
        for post in posts:
            post.is_liked = (
                user.is_authenticated
                and post.likes.filter(id=user.id).exists()
            )

        context["posts"] = posts
        return context
    
# 상세 페이지 (DB기반) + 댓글 작성
def post_detail_view(request, post_id):
    # 게시글 조회
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")
    
    # 댓글 조회
    comments = Comment.objects.filter(post=post).order_by("-created_at")

    # 좋아요 여부 체크
    if request.user.is_authenticated:
        post.is_liked = post.likes.filter(id=request.user.id).exists()
    else:
        post.is_liked = False

    # 댓글 작성 처리
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/logindemo/")

        content = request.POST.get("content", "").strip()
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            return redirect(f"/community/{post_id}/")
        
    return render(request, "community/post_detail.html", {
        "post": post,
        "comments": comments,
    })
    
class EmotionalView(TemplateView):
    template_name = "emotional.html"

class HealthView(TemplateView):
    template_name = "health.html"

class LocalView(TemplateView):
    template_name = "local.html"


# 회원가입 데모 페이지
class RegisterDemoView(TemplateView):
    template_name = "registerdemo.html"

#로그인 데모 페이지
class LoginDemoView(TemplateView):
    template_name = "logindemo.html"

class DetailView(TemplateView):
    template_name = "detail.html"

class WritingView(TemplateView):
    template_name="writing.html"
