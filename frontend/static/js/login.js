document.addEventListener("DOMContentLoaded", () => {

    // CSRF 가져오기
    const csrfInput = document.querySelector("[name=csrfmiddlewaretoken]");
    const csrftoken = csrfInput ? csrfInput.value : "";
  
    const urlParams = new URLSearchParams(window.location.search);
    const nextUrl = urlParams.get("next") || "/";
    const alertBox = document.getElementById("login-alert");
  
    const loginBtn = document.getElementById("login-btn");
    const logoutBtn = document.getElementById("logout-btn");
  
    function showAlert(message, type = "error") {
        alertBox.textContent = message;
        alertBox.className = "login-alert is-visible " +
            (type === "success" ? "login-alert--success" : "login-alert--error");
    }
  
    async function requestJson(url, payload) {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            credentials: "include",
            body: JSON.stringify(payload),
        });
  
        const data = await response.json().catch(() => ({}));
  
        if (!response.ok) {
            throw new Error(data.message || "요청 처리 중 오류가 발생했습니다.");
        }
        return data;
    }
  
    /* 로그인 처리*/
    loginBtn.addEventListener("click", async () => {
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();
  
        if (!username || !password) {
            showAlert("아이디와 비밀번호를 모두 입력해주세요.");
            return;
        }
  
        try {
            await requestJson("/api/login/", { username, password });  // ★ 수정됨
            showAlert("로그인 성공! 잠시 후 이동합니다.", "success");
            setTimeout(() => window.location.href = nextUrl, 600);
  
        } catch (error) {
            showAlert(error.message);
        }
    });
  
    /* 로그아웃 처리*/
    logoutBtn.addEventListener("click", async () => {
        try {
            await requestJson("/api/logout/", {});
            showAlert("로그아웃했습니다.", "success");
  
            setTimeout(() => {
                window.location.href = "/logindemo/";
            }, 500);
  
        } catch (error) {
            showAlert(error.message);
        }
    });
  
  });