document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("file");
  const fileName = document.querySelector(".file-name");
  const form = document.querySelector(".content-share__form");
  const content = document.getElementById("content");
  const submitBtn = document.querySelector(".submit-btn");

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
    submitBtn.addEventListener("click", function () {
      const textLength = content.value.trim().length;

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
