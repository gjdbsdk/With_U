document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("file");
  const fileName = document.querySelector(".file-name");
  const form = document.querySelector(".content-share__form");
  const content = document.getElementById("content");
  const submitBtn = document.querySelector(".submit-btn");
  const LOGIN_URL = "/logindemo/?next=/citizen/";
  const SESSION_URL = "/api/session/";

  const loginModal = document.getElementById("login-required-modal");
  const loginConfirmBtn = document.getElementById("login-modal-confirm");
  const modalDismissEls = document.querySelectorAll("[data-modal-dismiss]");

  const normalize = (text) => (text || "").trim();

  function openLoginModal() {
    if (!loginModal) return;
    loginModal.classList.add("is-visible");
    loginModal.setAttribute("aria-hidden", "false");
  }

  function closeLoginModal() {
    if (!loginModal) return;
    loginModal.classList.remove("is-visible");
    loginModal.setAttribute("aria-hidden", "true");
  }

  modalDismissEls.forEach((el) => {
    el.addEventListener("click", closeLoginModal);
  });

  if (loginConfirmBtn) {
    loginConfirmBtn.addEventListener("click", () => {
      closeLoginModal();
      window.location.href = LOGIN_URL;
    });
  }

  async function checkSession() {
    try {
      const response = await fetch(SESSION_URL, {
        method: "GET",
        credentials: "same-origin",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      if (!response.ok) {
        throw new Error("세션 확인 실패");
      }
      const data = await response.json();
      return data.authenticated === true;
    } catch (error) {
      console.error("세션 확인 오류", error);
      return false;
    }
  }

  if (fileInput && fileName) {
    fileInput.addEventListener("change", function () {
      if (this.files.length > 0) {
        const file = this.files[0];
        const maxSize = 5 * 1024 * 1024;

        if (file.size > maxSize) {
          alert("파일 크기는 최대 5MB까지 업로드 가능합니다.");
          this.value = "";
          fileName.textContent = "선택된 파일이 없습니다.";
          return;
        }

        fileName.textContent = file.name;
      } else {
        fileName.textContent = "선택된 파일이 없습니다.";
      }
    });
  }

  if (submitBtn && form && content) {
    submitBtn.addEventListener("click", async function () {
      // seohaein 11/14: 시민 콘텐츠 제출 시 로그인 세션 확인
      const isAuthenticated = await checkSession();
      if (!isAuthenticated) {
        // seohaein 11/14: 경고 모달로 전환
        openLoginModal();
        return;
      }

      const textLength = normalize(content.value).length;

      if (textLength < 100) {
        alert("내용은 최소 100자 이상 작성해야 합니다.");
        content.focus();
        return;
      }

      form.querySelectorAll("input, textarea, button").forEach((el) => {
        el.disabled = true;
      });

      form.classList.add("form-disabled");
      alert("제출 완료되었습니다. 감사합니다.");
      submitBtn.textContent = "제출 완료";
    });
  }
});
