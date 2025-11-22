// static/js/base.js

// CSRF 토큰을 쿠키에서 가져오는 헬퍼 함수 (Django POST 요청 시 필수)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", () => {
  /* ============================================================
       1. 회원정보 모달 (드롭다운) 로직
    ============================================================ */
  const userBtn = document.querySelector(".user-menu-btn"); // 클릭 버튼
  const modal = document.getElementById("user-modal"); // 모달창
  const closeBtn = document.querySelector(".close-modal"); // 닫기(X) 버튼 (없을 수도 있음)

  if (userBtn && modal) {
    // 1-1. 버튼 클릭 시 모달 열기/닫기 (토글)
    userBtn.addEventListener("click", (e) => {
      e.stopPropagation(); // 이벤트가 document로 전파되는 것을 막음
      modal.classList.toggle("hidden");
    });

    // 1-2. 모달 닫기 버튼(X)이 있다면 처리
    if (closeBtn) {
      closeBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        modal.classList.add("hidden");
      });
    }

    // 1-3. 화면의 다른 곳(바깥)을 클릭하면 닫기
    document.addEventListener("click", (e) => {
      // 모달이 열려있고, 클릭한 곳이 모달 내부가 아니고, 버튼도 아니라면 닫기
      if (
        !modal.classList.contains("hidden") &&
        !modal.contains(e.target) &&
        !userBtn.contains(e.target)
      ) {
        modal.classList.add("hidden");
      }
    });
  }

  /* ============================================================
       2. 로그아웃 로직
    ============================================================ */
  const logoutBtn = document.getElementById("logout-btn");

  // 로그아웃 버튼은 로그인 상태일 때만 존재하므로 if문으로 체크
  if (logoutBtn) {
    logoutBtn.addEventListener("click", async (e) => {
      e.preventDefault(); // 기본 동작 방지

      // 확인 메시지 (선택사항)
      if (!confirm("정말 로그아웃 하시겠습니까?")) return;

      const csrfToken = getCookie("csrftoken"); // CSRF 토큰 가져오기

      try {
        const res = await fetch("/api/logout/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken, // 헤더에 토큰 추가
          },
          credentials: "include",
        });

        if (res.ok) {
          alert("로그아웃되었습니다!");
          window.location.href = "/"; // 메인 페이지로 이동
        } else {
          console.error("로그아웃 실패 status:", res.status);
          alert("로그아웃 처리에 실패했습니다.");
        }
      } catch (error) {
        console.error("Logout Error:", error);
        alert("서버 통신 중 오류가 발생했습니다.");
      }
    });
  }

  /* ============================================================
       3. (추가) 좋아요/글쓰기 등 다른 기능이 있다면 아래에 유지
    ============================================================ */
  // ... 기존에 있던 다른 로직들 ...
});
