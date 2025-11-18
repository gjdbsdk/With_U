document.addEventListener('DOMContentLoaded', function() {
    const writeBtn = document.getElementById("write-btn");

    if (writeBtn) { 
        writeBtn.addEventListener("click", async (e) => {
            e.preventDefault(); // 기본 링크 이동 막기

            try {
                const response = await fetch("/api/check-login/", {
                    method: "GET",
                    credentials: "include", // 세션 쿠키 포함해서 요청
                });

                if (!response.ok) {
                    throw new Error('로그인 확인 중 서버 오류가 발생했습니다.');
                }

                const data = await response.json();

                if (data.is_authenticated) {
                    // 로그인 되어 있으면 글쓰기 페이지로 이동
                    window.location.href = "/writing/";
                } else {
                    // 로그인 안 되어 있으면 로그인 페이지로 이동
                    alert("글쓰기는 로그인 후 이용할 수 있습니다.");
                    window.location.href = "/logindemo/";
                }
            } catch (error) {
                console.error("Login check failed:", error);
                alert("로그인 상태 확인 중 오류가 발생했습니다. 다시 시도해주세요.");
            }
        });
    }

    const likeButtons = document.querySelectorAll('.like-btn');

    likeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            const btn = event.currentTarget;

            // 1. 로그인 여부 확인 (HTML에 있는 data 속성 활용)
            const isAuthenticated = btn.dataset.isAuthenticated === 'true';

            if (!isAuthenticated) {
                // 로그인 X
                if(confirm("로그인이 필요한 서비스입니다.\n로그인 페이지로 이동하시겠습니까?")) {
                    window.location.href = "/logindemo/"; // 로그인 페이지 URL
                }
                return;
            }
            
            // 로그인 O
            const postId = btn.dataset.postId;
            // handleLike 함수는 DOMContentLoaded 리스너 밖에 정의
            handleLike(postId, btn);
        });
    });

});


async function handleLike(postId, btn) {
    // API 주소
    const url = `/api/community/like/${postId}/`; 

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                'post_id': postId
            })
        });

        if (!response.ok) {
            throw new Error('서버 응답에 문제가 있습니다. (로그인 필요 등)');
        }

        // 서버로부터 JSON 응답을 받습니다.
        // data 구조 예시: { "likes_count": 12, "is_liked": true }
        const data = await response.json();
        
        const icon = btn.querySelector('i'); // 버튼 안의 아이콘
        const countSpan = btn.querySelector('span'); // 버튼 안의 숫자
        
        // 숫자 업데이트
        countSpan.innerText = data.likes_count;

        // 아이콘 및 상태 업데이트
        if (data.is_liked) {
            btn.dataset.liked = "true";
            icon.classList.remove('fa-regular', 'text-gray-500'); // 빈 하트 스타일 제거
            icon.classList.add('fa-solid', 'text-red-500');       // 빨간 하트 스타일 추가
        } else {
            btn.dataset.liked = "false";
            icon.classList.remove('fa-solid', 'text-red-500');     // 빨간 하트 스타일 제거
            icon.classList.add('fa-regular', 'text-gray-500');     // 빈 하트 스타일 추가
        }

    } catch (error) {
        console.error('Error:', error);
        alert('좋아요 처리에 실패했습니다. 잠시 후 다시 시도해주세요.');
    }
}