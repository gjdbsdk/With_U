document.addEventListener("DOMContentLoaded", () => {
  const submitBtn = document.querySelector(".submit-btn");
  const form = document.querySelector(".content-share__form");
  const fileInput = document.getElementById("file");
  const fileNameSpan = document.querySelector(".file-name");
  const contentInput = document.getElementById("content");

  function shortenFileName(name, maxLength = 25) {
    if (name.length <= maxLength) return name;

    const extIndex = name.lastIndexOf(".");
    const ext = extIndex !== -1 ? name.slice(extIndex) : "";
    const base = name.slice(0, extIndex);

    const keepFront = 12;
    const keepBack = 10;

    return base.slice(0, keepFront) + "..." + base.slice(-keepBack) + ext;
  }

  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      const file = fileInput.files[0];

      if (file.size > 5 * 1024 * 1024) {
        alert("첨부 파일은 최대 5MB까지만 업로드할 수 있습니다.");
        fileInput.value = "";
        fileNameSpan.textContent = "선택된 파일이 없습니다.";
        return;
      }

      const originalName = file.name;
      fileNameSpan.textContent = shortenFileName(originalName);
    } else {
      fileNameSpan.textContent = "선택된 파일이 없습니다.";
    }
  });

  contentInput.addEventListener("input", () => {
    if (contentInput.value.length > 150) {
      alert("내용은 최대 150자까지 입력할 수 있습니다.");
      contentInput.value = contentInput.value.slice(0, 150);
    }
  });

  submitBtn.addEventListener("click", async (e) => {
    e.preventDefault();

    if (contentInput.value.length > 150) {
      alert("내용은 150자 이하로 작성해야 합니다.");
      return;
    }

    const formData = new FormData(form);

    const res = await fetch("/api/citizen/upload/", {
      method: "POST",
      body: formData,
    });

    if (res.status === 401) {
      alert("로그인이 필요합니다.");
      location.href = "/logindemo/";
      return;
    }

    const data = await res.json();

    if (res.ok) {
      alert("콘텐츠가 정상적으로 제출되었습니다.");
      location.reload();
    } else {
      alert("제출 실패: " + JSON.stringify(data));
    }
  });
});
