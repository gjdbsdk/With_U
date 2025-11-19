const csrfInput = document.querySelector("[name=csrfmiddlewaretoken]");
  const csrftoken = csrfInput ? csrfInput.value : "";
  const urlParams = new URLSearchParams(window.location.search);
  const redirectUrl = urlParams.get("next") || "/citizen/";
  const registerAlert = document.getElementById("register-alert");

  function setRegisterAlert(message, type = "error") {
    registerAlert.textContent = message;
    registerAlert.className = "register-alert is-visible " + (type === "success" ? "register-alert--success" : "register-alert--error");
  }

  async function requestJson(url, payload) {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) {
      throw data;
    }
    return data;
  }

  document.getElementById("register-btn").addEventListener("click", async () => {
    const username = document.getElementById("reg-username").value.trim();
    const email = document.getElementById("reg-email").value.trim();
    const password = document.getElementById("reg-password").value.trim();
    const password2 = document.getElementById("reg-password2").value.trim();

    if (!username || !email || !password || !password2) {
      setRegisterAlert("모든 입력칸을 채워주세요.");
      return;
    }
    if (password.length < 8) {
      setRegisterAlert("비밀번호는 8자 이상이어야 합니다.");
      return;
    }
    if (password !== password2) {
      setRegisterAlert("비밀번호가 일치하지 않습니다.");
      return;
    }

    try {
      await requestJson("/api/register/", { username, email, password });
      setRegisterAlert("회원가입이 완료되었습니다. 잠시 후 로그인 페이지로 이동합니다.", "success");
      setTimeout(() => {
        window.location.href = `/logindemo/?next=${encodeURIComponent(redirectUrl)}`;
      }, 800);
    } catch (error) {
      if (error.username) {
        setRegisterAlert(error.username[0]);
      } else if (error.email) {
        setRegisterAlert(error.email[0]);
      } else {
        setRegisterAlert(error.message || "회원가입 처리에 실패했습니다.");
      }
    }
  });
