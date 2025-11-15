document.addEventListener("DOMContentLoaded", () => {

  const submitBtn = document.querySelector(".submit-btn");
  const form = document.querySelector(".content-share__form");

  // 버튼 클릭
  submitBtn.addEventListener("click", async (e) => {
    e.preventDefault();  // 기본 form 제출 막기 (중요!!!)

    const formData = new FormData(form);

    const res = await fetch("/api/citizen/upload/", {
      method: "POST",
      body: formData
    });

    if (res.status === 401) {
      alert("로그인이 필요합니다!");
      location.href = "/logindemo/";
      return;
    }

    const data = await res.json();

    if (res.ok) {
      alert("콘텐츠가 정상적으로 제출되었습니다!");
      location.reload();
    } else {
      alert("제출 실패: " + JSON.stringify(data));
    }
  });

});
