document.addEventListener("DOMContentLoaded", () => {
    const writeBtn = document.getElementById("write-btn");

    writeBtn.addEventListener("click", async (e) => {
        e.preventDefault(); // 기본 링크 이동 막기

        const response = await fetch("/api/check-login/", {
            method: "GET",
            credentials: "include", // 세션 쿠키 포함해서 요청
        });

        const data = await response.json();

        if (data.is_authenticated) {
            // 로그인 되어 있으면 글쓰기 페이지로 이동
            window.location.href = "/writing/";
        } else {
            // 로그인 안 되어 있으면 로그인 페이지로 이동
            alert("글쓰기는 로그인 후 이용할 수 있습니다.");
            window.location.href = "/logindemo/";
        }
    });
});
