document.addEventListener("DOMContentLoaded", function () {
  const params = new URLSearchParams(window.location.search);
  const page = params.get("page");
  const topic = params.get("topic");

  const title = document.getElementById("detail-title");
  const text = document.getElementById("detail-text");
  const youtube = document.getElementById("youtube-frame");

  // 아래에 작성하시면 됩니다.
  const contents = {
    emotional: {
      loss: {
        title: "상실감 회복하기",
        text: "상실감은 누구에게나 예기치 않게 찾아오며, 삶의 균형을 무너뜨리는 깊은 정서적 충격을 남깁니다. 그러나 상실감의 회복은 단순히 슬픔을 잊는 과정이 아니라, 그 감정을 이해하고 받아들이며 스스로를 다시 세워가는 여정입니다. 이 영상에서는 상실의 순간부터 회복의 단계까지, 감정의 흐름을 인식하고 건강하게 극복하기 위한 다양한 방법을 소개합니다.<br><br>특히, 상실이 가져오는 공허함과 무력감을 완화하기 위한 실질적인 대처 전략을 다루며, 일상 속 작은 변화가 회복 과정에 어떤 긍정적인 영향을 미치는지 구체적으로 설명합니다. 또한 자기 돌봄의 중요성과 주변과의 관계 회복, 그리고 상실 속에서 새로운 의미를 찾아가는 과정에 대해 심층적으로 탐구합니다.<br><br>본 영상은 상실의 아픔 속에 있는 이들뿐 아니라, 이미 회복의 길을 걷고 있으나 방향성을 잃은 이들에게도 도움이 될 것입니다. 상실을 완전히 지워내려 하기보다, 그 경험을 삶의 일부로 받아들이며 성장의 계기로 전환하는 것이 진정한 회복의 시작임을 제시합니다.",
        youtube:
          "https://www.youtube.com/embed/nByss5eNj4k?si=aX-OtOVEnPjWFbiZ",
      },
      lonely: {
        title: "외로움 관리하기",
        text: "외로움 관리는 현대 사회를 살아가는 개인의 정서적 안녕과 삶의 질을 유지하는 데 필수적인 요소입니다. 이는 단순히 혼자 있는 상태를 넘어, 타인과의 의미 있는 연결이 부족하다고 느끼는 주관적인 고립감을 다루는 과정을 포함합니다. 이 비디오에서는 외로움의 본질을 이해하고, 이를 건강하게 극복하기 위한 다양한 전략과 모범 사례를 자세히 설명합니다.<br><br>특히, 일시적인 외로움과 만성적인 고립감의 차이를 분석하고, 디지털 시대가 개인의 사회적 연결에 미치는 영향에 대해 심층적으로 다룹니다. 각자가 느끼는 외로움의 근본 원인을 파악하고 상황에 맞는 접근법을 선택하는 것의 중요성을 강조합니다.<br><br>또한, 자기 돌봄, 마음챙김 명상과 같은 내면적 치유 전략과 더불어, 의미 있는 사회적 관계 구축, 공동체 참여, 필요시 전문가의 도움을 구하는 것과 같은 실질적인 행동 지침을 제공합니다. 이를 통해 시청자가 겪을 수 있는 다양한 정서적 도전을 효과적으로 극복할 수 있도록 돕습니다.<br><br>본 비디오는 문득 고립감을 느끼는 현대인부터, 지속적인 외로움으로 어려움을 겪는 이들까지 모든 이들에게 유익한 통찰을 제공할 것입니다. 복잡한 감정의 파도를 건강하게 헤쳐나가고 더 충만한 삶을 가꾸기 위한 실용적인 지혜와 기법들을 익혀보세요.",
        youtube:
          "https://www.youtube.com/embed/i0-pjnjcxqU?si=2TDlrnKvehKpxAoj",
      },
      stress: {
        title: "스트레스 및 불안 완화",
        text: "효과적인 스트레스 및 불안 관리는 급변하는 현대 사회에서 개인의 정신적 안녕과 삶의 질을 유지하는 데 필수적인 요소입니다. 이는 단순히 일시적인 감정을 억누르는 것을 넘어, 스트레스의 근본 원인을 파악하고 신체적, 심리적 반응을 조절하며 정서적 회복탄력성을 높이는 과정을 포함합니다. 이 비디오에서는 스트레스와 불안의 신호를 인지하고, 이에 건강하게 대처하는 각 단계별 주요 전략과 모범 사례를 자세히 설명합니다.<br><br>특히, 마음챙김(Mindfulness) 기반 스트레스 완화와 인지행동치료(CBT) 접근법의 장단점을 비교하고, 각 개인의 상황과 기질에 적합한 이완 방식을 선택하는 방법에 대해 심층적으로 다룹니다. 또한, 호흡 조절, 수면 위생 관리, 신체 활동과 같은 중요한 자기 관리 영역에 대한 실질적인 조언을 제공하여 시청자들이 직면할 수 있는 다양한 정서적 도전을 효과적으로 극복할 수 있도록 돕습니다.<br><br>본 비디오는 일상적인 스트레스 관리에 어려움을 겪는 초심자부터, 만성적인 불안을 다스리고자 하는 이들까지 모든 이들에게 유익한 정보를 제공할 것입니다. 복잡한 감정의 압박을 건강하게 관리하고 더 평온한 일상을 이끌기 위한 실용적인 도구와 기법들을 익혀보세요.",
        youtube:
          "https://www.youtube.com/embed/7XCx1XcVP5w?si=IXk2ksX9HJzKe6R9",
      },
      mental: {
        title: "정신 건강 이해하기",
        text: "정신 건강은 신체 건강만큼이나 중요하지만, 종종 보이지 않는다는 이유로 간과되기 쉽습니다. 그러나 정신 건강을 돌보는 것은 단순히 부정적인 감정을 회피하는 과정이 아니라, 자신의 감정을 솔직하게 인식하고 수용하며 내면의 힘을 키워가는 여정입니다. 이 영상에서는 정신 건강의 중요성을 인식하는 순간부터 지속적인 관리까지, 감정의 변화를 이해하고 건강하게 다스리기 위한 다양한 방법을 소개합니다.<br><br>특히, 일상적인 스트레스와 불안이 정신 건강에 미치는 영향을 분석하고, 이를 완화하기 위한 실질적인 대처 전략을 다룹니다. 또한 자기 인식의 중요성과 건강한 대인 관계 형성, 그리고 정서적 회복탄력성을 높이는 습관들에 대해 심층적으로 탐구합니다.<br><br>본 영상은 자신의 마음 상태를 점검하고 싶은 초심자뿐 아니라, 이미 정서적 어려움을 겪고 있으나 대처에 막막함을 느끼는 이들에게도 도움이 될 것입니다. 정신 건강 문제를 외면하려 하기보다, 그 신호를 자신을 더 깊이 이해하는 기회로 삼고 적극적으로 관리하는 것이 진정한 내면의 평화를 향한 시작임을 제시합니다.",
        youtube:
          "https://www.youtube.com/embed/BZQ4t_kfPXI?si=8XGYi3T-NqGyYcmp",
      },
    },
    health: {
      safety: {
        title: "생활 안전 수칙",
        text: "화재, 감전, 낙상 등 일상 속 안전사고를 예방하기 위한 기본 원칙을 다룹니다.",
        youtube: "https://www.youtube.com/embed/7uOYZs0y3H0",
      },
      privacy: {
        title: "개인 정보 보호",
        text: "온라인과 오프라인에서 개인정보를 안전하게 관리하는 방법을 배워보세요.",
        youtube: "https://www.youtube.com/embed/xQ0Ds8j3lrw",
      },
      labor: {
        title: "기본 노동 권리",
        text: "근로자의 권리와 법적 보호장치, 근로계약서의 핵심을 설명합니다.",
        youtube: "https://www.youtube.com/embed/3m0G7Jp0fkg",
      },
      insurance: {
        title: "건강 보험 활용 가이드",
        text: "보험료 납부, 혜택 청구, 추가 보장제도를 이해하는 방법을 다룹니다.",
        youtube: "https://www.youtube.com/embed/sv_ojh7n-1s",
      },
    },
    lifestyle: {
      bank: {
        title: "은행 계좌 개설 및 ATM 사용",
        text: "은행 업무 초보자도 따라할 수 있는 쉬운 계좌 개설과 ATM 사용법입니다.",
        youtube: "https://www.youtube.com/embed/n8pAEH_wQeE",
      },
      tax: {
        title: "세금 신고 및 관리",
        text: "연말정산부터 종합소득세 신고까지, 세금의 기초를 배워봅니다.",
        youtube: "https://www.youtube.com/embed/qgH3OZpFPlc",
      },
      rent: {
        title: "월세 계약 이해하기",
        text: "임대차 계약서 작성, 보증금 보호, 전입신고 등 필수 절차를 다룹니다.",
        youtube: "https://www.youtube.com/embed/Yv9QeQb5lNo",
      },
      aid: {
        title: "공공 지원 신청",
        text: "정부 및 지자체 지원금 신청 방법을 단계별로 안내합니다.",
        youtube: "https://www.youtube.com/embed/kNfqHb7vFW4",
      },
      transport: {
        title: "지하철 노선도 읽는 법",
        text: "초보자를 위한 대중교통 노선도 해석법과 환승 팁을 알려드립니다.",
        youtube: "https://www.youtube.com/embed/QhaHbGsa7Sg",
      },
      shopping: {
        title: "생활 필수품 현명하게 구매하기",
        text: "합리적 소비와 할인 전략으로 경제적 생활을 유지하는 방법을 배워보세요.",
        youtube: "https://www.youtube.com/embed/TbRi8dTRRHQ",
      },
    },
  };
  
  const content = contents[page]?.[topic];

  if (content) {
    title.textContent = content.title;
    text.innerHTML = content.text;
    youtube.src = content.youtube;
  } else {
    title.textContent = "콘텐츠를 찾을 수 없습니다.";
    text.textContent = "URL이 잘못되었거나 콘텐츠가 준비 중입니다.";
  }
});
