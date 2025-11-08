async function loadProjects() {
  const target = document.querySelector("#projects");

  try {
    const response = await fetch("/api/projects/");
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    const data = await response.json();

    if (!Array.isArray(data) || data.length === 0) {
      target.innerHTML = "<p>등록된 프로젝트가 아직 없습니다.</p>";
      return;
    }

    target.innerHTML = data
      .map(
        (project) => `
          <article class="project-card">
            <h4>${project.name}</h4>
            <p>${project.description ?? ""}</p>
            <small>생성일: ${new Date(
              project.created_at,
            ).toLocaleString("ko-KR")}</small>
          </article>
        `,
      )
      .join("");
  } catch (error) {
    target.innerHTML = `<p class="error">프로젝트 목록을 불러오지 못했습니다: ${error.message}</p>`;
  }
}

document.addEventListener("DOMContentLoaded", loadProjects);

