from django.views.generic import TemplateView
import datetime     # 'timesince' 필터 및 임시 데이터 생성을 위해 임포트
from django.shortcuts import render, redirect
        # 함수 기반 뷰(FBV) 및 리다이렉트를 위해 임포트
from django.http import Http404
from django import forms


# [MOCK DB] 임시 데이터 저장소
# 리스트 페이지와 상세 페이지가 이 데이터를 공유합니다.
def get_dummy_db():
    # 날짜 계산용
    now = datetime.datetime.now()
    
    return [
        {
            'id': 1,  # 고유 ID 부여
            'author_initial': '김',
            'title': '첫 번째 테스트 포스트입니다',
            'author_name': '김테스트',
            'created_at': now - datetime.timedelta(hours=2),
            'content': '이것은 상세 페이지 내용입니다.\n\n줄바꿈이 잘 적용되는지 확인해보세요.\n상세 페이지 디자인이 아주 깔끔하게 나왔으면 좋겠네요.',
            'snippet': '이것은 뷰에서 넘어온 가짜 데이터입니다. 루프가 잘 도는지 확인해보세요...',
            'likes_count': 12,
            'comments_count': 2, # 아래 더미 댓글 개수와 맞춤
            'views': 150,
            'is_liked': False, # 내가 좋아요 눌렀는지 여부
        },
        {
            'id': 2,
            'author_initial': '이',
            'title': '두 번째 테스트: 월세 계약 시 주의사항',
            'author_name': '이장고',
            'created_at': now - datetime.timedelta(days=1),
            'content': '월세 계약할 때 등기부등본 꼭 확인하세요.\n근저당이 너무 많이 잡혀있으면 위험합니다.\n\n1. 등기부등본 확인\n2. 집주인 신분증 확인\n3. 특약사항 꼼꼼히 넣기',
            'snippet': '두 번째 가짜 데이터입니다. 둥근 모서리 카드 스타일이 잘 나오는지 확인합니다.',
            'likes_count': 5,
            'comments_count': 0,
            'views': 42,
            'is_liked': True, 
        }
    ]


# Forms
#TODO: 추후 Post 모델 만들고 ModelForm으로 교체하기
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
                    {'title': '조의금 봉투 작성법', 'content': '조의금 봉투 앞면에는 \'부의(賻儀)\', \'조의(弔儀)\' 등을 세로로 씁니다. 뒷면 좌측 하단에 이름을 씁니다.'},
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



class CommunityView(TemplateView):
    template_name = "community/community.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 전역 함수에서 데이터 가져오기
        posts = get_dummy_db()
        
        # 각 포스트에 상세 페이지 URL 연결 (하드코딩 방식)
        # 나중에 urls.py 설정에 따라 '/community/1/' 등으로 자동 생성해야 함
        for post in posts:
            # {% url 'frontend:post_detail' post.id %} 와 같은 효과를 내기 위해 
            # 템플릿에서 처리하도록 여기서는 id만 잘 넘겨주기
            post['detail_url'] = f"/community/{post['id']}/" 
            
        context['posts'] = posts
        return context
    

# 상세 페이지 뷰
def post_detail_view(request, post_id):
    # 1. 전체 더미 데이터 가져오기
    posts = get_dummy_db()
    
    # 2. 요청된 post_id와 일치하는 데이터 찾기
    # (Python 리스트에서 검색)
    target_post = None
    for post in posts:
        if post['id'] == post_id:
            target_post = post
            break
    
    # 3. 없으면 404 에러
    if target_post is None:
        raise Http404("게시글을 찾을 수 없습니다.")

    # 4. 더미 댓글 데이터 생성 (상세 페이지용)
    dummy_comments = [
        {
            'author_initial': '박',
            'author_name': '박댓글',
            'created_at': datetime.datetime.now(),
            'content': '정말 유용한 정보네요! 감사합니다.'
        },
        {
            'author_initial': 'Guest',
            'author_name': '지나가던행인',
            'created_at': datetime.datetime.now() - datetime.timedelta(minutes=30),
            'content': '디자인이 깔끔해서 보기 좋아요.'
        }
    ]

    context = {
        'post': target_post,
        'comments': dummy_comments if target_post['id'] == 1 else [], # 1번 글에만 댓글이 있다고 가정
    }
    
    return render(request, 'community/post_detail.html', context)

    
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


# 아래 작성해주신 건 연동 후에 사용할 수 있을 것 같아 일단 새로 위에 작성해서 구현했습니다
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #TODO : [DB 연동] 유효한 폼 데이터를 실제 Post 모델에 저장하는 로직 필요

            # 글 작성 후, 'community_list'라는 이름의 URL로 리다이렉트
            # (urls.py에서 CommunityView의 name='community_list' 설정 필요)
            return redirect('community_list') 
    else:
        form = PostForm()   # GET 요청 시 빈 폼 생성
    
    context = {
        'form': form,
        'page_title': '새 토론 작성' # 글 작성 html에서 사용 - {{ page_title }}로 사용하기
    }
    return render(request, 'community/post_form.html', context)
