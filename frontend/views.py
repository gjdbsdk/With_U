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
                        'content': '''조의금 봉투 앞면에는 고인을 애도하는 한자를 세로로 작성합니다. 아래 여섯 가지 한자를 많이 사용합니다.<br><br>
• 근조(謹弔) : 죽음에 대해 삼가 슬퍼하는 마음<br>
• 애도(哀悼) : 사람의 죽음에 대해 슬퍼함<br>
• 추모(追慕) : 죽은 사람을 그리며 생각함<br>
• 추도(追悼) : 죽은 사람에 대해 슬퍼함<br>
• 부의(賻儀) : 상가에 부조로 보내는 돈<br>
• 위령(慰靈) : 죽은 사람의 영혼을 위로함<br><br>
뒷면 좌측 하단에 본인의 이름과 소속을 표시합니다. 만약 단체나 소속에서 부의금을 보낸다면, 뒷면에 단체나 회사명만 적어도 무방합니다.'''
                    },
                    {
                        'title': '장례식장 방문 시 기본 예절',
                        'content': '''<b>복장</b><br>
남녀 공통으로 검정색 정장이 기본입니다. 남성은 검은색 양말, 여성은 짧은 치마와 화려한 액세서리를 피하고 스타킹을 착용합니다.<br><br>
<b>공수법(손 모으는 자세)</b><br>
흉사(喪) 시에는 평상시와 반대로 <b>남자는 오른손이 위, 여자는 왼손이 위</b>로 합니다.<br><br>
<b>절하는 법</b><br>
고인에게 두 번 절(재배)을 합니다.<br><br>
<b>주의 사항</b><br>
사망 원인 상세히 묻기, 상주에게 악수 청하기, 식사 자리에서 건배하기, 유가족 붙잡고 계속 말 시키기는 행동은 삼갑니다.<br><br>
<b>문상 절차</b><br>
외투를 벗고 부의금을 전달한 후, 영정 앞에 헌화/분향하고 묵념 또는 재배합니다. 상주와 맞절 후 짧게 위로의 말을 건네고, 물러 나올 때는 뒤로 물러난 뒤 몸을 돌려 나옵니다.'''
                    },
                    {
                        'title': '헌화 및 분향 순서',
                        'content': '''<b>헌화</b><br>
오른손으로 꽃줄기 하단을 잡고 왼손 바닥으로 오른손을 받쳐 들어, 두 손으로 <b>꽃 봉우리가 영정 쪽으로 향하게</b> 제단 위에 헌화한 뒤 잠깐 묵념합니다.<br><br>
<b>분향</b><br>
막대향 1~2개를 집어 촛불에 불을 붙인 후, <b>가볍게 흔들어</b> 불을 끕니다 (절대로 입으로 불면 안 됩니다). 두 손으로 향로에 꽂습니다.'''
                    },
                ]
            },
            {
                    'title': '결혼식 예절',
                    'description': '결혼식 참석 시 하객이 지켜야 할 예절과 신랑 신부에게 축하의 마음을 전달하는 방법을 설명합니다.',
                'icon_path': 'img/wedding.png', # static/img/wedding.png
                'topics': [
                    {
                        'title': '하객 복장 가이드',
                        'content': '''<b>남자</b><br>
블랙, 네이비, 그레이 톤의 기본 정장 또는 세미 정장이 좋으며, 올 화이트 정장, 반바지, 슬리퍼 등은 피합니다.<br><br>
<b>여자</b><br>무릎 길이 이상의 스커트, 단정한 투피스 등이 좋으며, <b>신부의 색상인 흰색 계열 원피스</b>와 지나치게 화려하거나 노출이 심한 복장은 피합니다. 파스텔톤, 네이비, 베이지 등 차분한 색상을 추천합니다.'''
                    },
                    {
                        'title': '축의금 전달 및 인사',
                        'content': '''<b>축의금 봉투</b><br>
앞면에 '축 결혼' 또는 신랑측은 '축 결혼', 신부측은 '축 화혼'을 적고, 뒷면 왼쪽 아래에는 <b>이름과 소속</b>을 차례로 적습니다.<br><br>
<b>축의금 전달</b><br>축의대에 내는 것이 일반적이며, 금액은 <b>홀수</b>로, 가급적 신권으로 준비하는 것이 예의입니다. 방명록 작성을 잊지 마세요.'''
                    },
                    {
                        'title': '피로연 예절',
                        'content': '''<b>참석 여부 회신</b><br>초대장을 받은 즉시 또는 기한 내에 회신합니다.<br><br>
<b>복장</b><br>신랑신부보다 튀는 복장은 삼가고 단정하게 입습니다.<br><br>
<b>행동</b><br>신랑신부에게 진심 어린 축하 인사를 건네며, 음식을 남기지 않게 적당량 담습니다. 식사 중에는 적절한 대화 볼륨을 유지하고, 다른 하객 사진 촬영에 방해되지 않도록 자리를 독점하지 않습니다.'''
                    },
                ]
            },
            {
                'title': '제례 의식',
                'description': '조상를 기리는 제례 의식의 의미와 기본적인 절차, 예절에 대해 안내합니다.',
                'icon_path': 'img/ancestral.png', # static/img/ancestral.png
                'topics': [
                    {
                        'title': '차례상 차리는 법',
                        'content': '''차례상은 보통 5열로 차립니다. <b>신위(지방)가 있는 쪽이 북쪽</b>입니다.<br><br>
<b>기본 원칙</b>:<br>
• <b>1열 (식사류)</b><br>반서갱동 (밥/술잔은 서쪽, 국/떡국은 동쪽), 시접거중 (수저 그릇은 가운데)<br>
• <b>2열 (주요리)</b><br>어동육서 (생선은 동쪽, 고기는 서쪽), 동두서미 (생선 머리는 동쪽, 꼬리는 서쪽)<br>
• <b>3열 (탕류)</b><br>고기탕은 서쪽, 어탕은 동쪽에 배치<br>
• <b>4열 (밑반찬류)</b><br>좌포우혜 (포는 서쪽, 식혜는 동쪽)<br>
• <b>5열 (과일)</b><br>조율이시 (서쪽부터 대추, 밤, 배, 감 순서), 홍동백서 (붉은 과일은 동쪽, 흰 과일은 서쪽)<br><br>
<b>주의할 점</b><br>'치'가 들어간 생선, 복숭아 등 털 있는 과일, 강한 향신료(고춧가루, 마늘) 사용을 금합니다. 음식 개수는 <b>홀수</b>로 맞추고 붉은 팥고물 대신 흰 고물 떡을 씁니다.'''
                    },
                    {
                        'title': '차례 시 복장 및 자세',
                        'content': '''<b>복장</b><br>단정한 한복이 기본이며, 없다면 단정하고 깨끗한 일반 의복으로 대체합니다. 무채색이나 차분한 계열이 좋습니다.<br><br>
<b>자세</b><br>조상이 편안히 흠향하실 수 있도록 경건하고 엄숙한 자세를 유지하며, 장난이나 잡담을 삼가고 공수법에 맞게 절합니다.'''
                    },
                    {
                        'title': '절차와 의의',
                        'content': '''<b>주요 절차(간소화)</b><br>강신(降神, 조상 혼령 모시기) → 참신(參神, 인사) → 헌주(獻酒, 술 올리기) → 삽시정저(插匙正箸, 수저 꽂아 식사 권하기) → 철상(撤床) → 음복(飮福, 복 받기).<br><br>
<b>의의</b><br>조상의 은혜에 감사하고 추모하며, 가족과 친척 간의 화목을 다지는 중요한 전통 의례입니다.'''
                    },
                ]
            },
            {
                'title': '병문안 예절',
                'description': '환자를 방문하여 위로할 때 지켜야 할 예절과 배려심 있는 행동에 대해 안내합니다.',
                'icon_path': 'img/visit.png', # static/img/visit.png
                'topics': [
                    {
                        'title': '방문 시간 및 기간',
                        'content': '''<b>방문 시간</b><br>병원의 면회 시간과 환자의 식사, 검사, 회진 시간을 피하여 준수합니다.<br><br>
<b>방문 기간</b><br>환자가 입원한 직후나 수술 전후 1~2일은 피하고, 환자가 안정을 찾은 후 30분 내외로 짧게 방문합니다.'''
                    },
                    {
                        'title': '선물 선택 가이드',
                        'content': '''<b>피해야 할 선물</b><br>꽃(알레르기/향), 환자가 먹지 못하는 음식, 소리가 큰 물건.<br><br>
<b>추천 선물</b><br>휴대가 간편한 과일, 즙이 많은 음료, 책이나 신문, 간단한 위생/편의용품 등 환자의 필요에 맞는 물품.'''
                    },
                    {
                        'title': '대화 및 행동 시 주의사항',
                        'content': '''<b>대화</b><br>긍정적인 말과 격려를 해주고, 환자의 병세에 대해 상세히 묻거나 지나친 걱정, 충고는 삼갑니다. 다른 환자에게 방해되지 않도록 작은 목소리로 대화합니다.<br><br>
<b>행동</b><br>침대나 환자의 물건에 함부로 손대지 않고, 방문 전후로 손 소독을 철저히 합니다.'''
                    },
                    {
                        'title': '병문안 자제의 필요성',
                        'content': '''환자에게 휴식은 매우 중요합니다. 잦은 방문은 환자의 피로도를 높일 수 있으며, 본인에게 감기나 전염병 증세가 있거나 감염 우려가 있을 경우 환자와 방문객 모두를 위해 방문을 자제하고 메시지 등으로 위로를 전하는 것이 좋습니다.'''
                    },
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
