# ASAC_5th_Review_Summarization  
### 고객 탐색 경험 향상을 위한 키워드 기반 리뷰 요약 서비스
**기간 : 2024.06 ~ 2024.08**

---

## 📌 1. 프로젝트 개요

리뷰 플랫폼에서 “핵심 정보를 빠르게 파악하기 어렵다”는 문제를 해결하기 위해  
**키워드 기반 리뷰 요약 및 지역 기반 필터링 서비스**를 Streamlit으로 구현한 프로젝트입니다.

### 🎯 프로젝트 목표
- 긴 리뷰를 읽지 않아도 **핵심 내용만 빠르게 이해**할 수 있도록 요약 제공  
- 사용자 방문 지역 정보를 활용하여 **신뢰도 높은 리뷰만 필터링**  
- 시각화 기반 UI를 통한 **효율적 탐색 경험 제공**  

---

## 💡 2. 문제 정의

- 리뷰는 길고 중복이 많아 핵심 파악이 어려움  
- 모바일 환경에서는 긴 글보다 **요약된 정보**가 필요  
- 사용자 체류 시간이 짧기 때문에 **빠른 의사결정**이 중요  

👉 **목표 : 필요한 정보를 최소한의 시간으로 이해할 수 있는 요약 모델 개발**

---

## 🚀 3. 프로젝트 최종 데모

👉 **Streamlit Demo 바로가기 :**  https://asac-map.streamlit.app/

<p align="center">
  <img alt="결과1" src="https://github.com/user-attachments/assets/12cb4bfd-5cf8-4788-b67f-6efae86d0ada" width="100%" />
</p>

<p align="center">
  <img alt="결과2" src="https://github.com/user-attachments/assets/dc2e08e8-cba7-4170-b080-47645b5a2531" width="100%" />
</p>

---

## 🧠 4. 비즈니스 인사이트

<p align="center">
  <img src="https://github.com/user-attachments/assets/dba8b524-f771-4888-b629-002906af3fde" width="80%"/>
</p>

---

## 🗃️ 5. 데이터 전처리 및 최종 스키마

본 프로젝트는 **Yelp Open Dataset**을 기반으로 진행되었으며, 핵심 정보만 남기기 위해 아래와 같은 전처리 과정을 수행했습니다.

### 🔧 전처리 주요 단계

- **카테고리 세분화 및 필터링**  
  - business 테이블의 JSON category에서 *food / restaurant* 관련 업장만 필터링

- **리뷰 데이터 정제**  
  - 최근 **5개년 리뷰만 사용**  
  - 가게별 리뷰 수 **10개 이상** 유지하여 데이터 품질 확보

- **사용자 지역 정보 생성**  
  - user 테이블에서 사용자별 **최빈 방문 지역** 추출  
  - (방문 횟수 3회 미만일 경우 신뢰도 기준으로 공란 처리)

- **핵심 지표 재계산**  
  - 필터링된 데이터에 맞춰 **review count / stars 등 주요 지표 재산정**

- **테이블 정합성 검증 및 인코딩**  
  - business–review–user 테이블 간 key 매칭 정합성 확인  
  - 복잡한 id 값은 **라벨 인코딩(label encoding)** 적용하여 간소화

- **샘플링 및 이상치 제거**  
  - 데이터 불균형(skew) 완화를 위해  
    - 고밀도 구간과 기타 구간을 분리하여 **층화 샘플링** 진행  
  - 이상치 제거 후 분포 검증  
  - 샘플링 이후에도 평점·리뷰 분포가 **기존 패턴 유지**됨 확인

### 📦 최종 스키마
<p align="center">
  <!-- 여기에 스키마 이미지 -->
  <img alt="데이터셋 스키마" src="https://github.com/user-attachments/assets/168c3e5e-48fb-4869-9766-b51b1193336e" width="100%"/>
</p>

---

## 🛠️ 6. 사용 모델

<p align="center">
  <img src="https://github.com/user-attachments/assets/13f12d77-4132-4682-8bd2-8d276f856289" width="80%"/>
</p>

---

## 📈 7. 모델 평가

### ✔ 정량적 평가

#### 🔹 키워드 추출 (KeyBERT)
- 다양한 키워드 모델을 비교한 결과, **KeyBERT가 가장 높은 일관성과 정확도를 보여 최종 모델로 선정**
- Bi-gram이 문장 의미를 더 잘 포착하여 전체적인 요약 품질 향상
<p align="center">
  <img src="https://github.com/user-attachments/assets/4464dbc6-6b35-40b4-ac3a-6458c592afc3" width="45%"/>
  <img src="https://github.com/user-attachments/assets/b57c9b7a-052b-4497-97f2-71459bb5ef36" width="50%"/>
</p>

#### 🔹 토픽 분류 (OpenAI API)
- pyLDAvis 기반 coherence score로 토픽 응집도를 계산  
→ **6개의 토픽이 가장 높은 coherence를 보임**
- TF-IDF 코사인 유사도 분석 결과  
→ **토픽 간 유사도가 낮아(0.1~0.3)** 토픽이 잘 분리됨을 확인
<p align="center">
  <img src="https://github.com/user-attachments/assets/8a81ff87-12fc-4f5d-8b41-12c16f05f660" width="80%"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/7229db3e-8229-4de1-aeb4-99f257f2f36b" width="80%"/>
</p>

---

### ✔ 정성적 평가 (팀원 평가)
- 약 200개 샘플을 기준으로 5점 척도 평가 진행  
- KeyBERT + Bi-gram 조합이 **가독성과 핵심 요약 측면에서 가장 높은 점수**를 획득  
- 토픽 분류 결과 역시 **사람이 판단해도 자연스럽게 묶이는 구성** 확인됨
<p align="center">
  <img src="https://github.com/user-attachments/assets/0d633720-5497-4dc3-b43d-b3dd2cfcd912" width="80%"/>
</p>

---

## 🗂️ 8. Edge Case 관리

프로젝트의 예외 상황을 체계적으로 관리하기 위해  
**Edge Case / Backlog를 Notion 기반으로 정리 및 기능 범위 조정**

👉 **실제 관리 페이지** https://seheehee.notion.site/Edge-case-e4bd792032cf4159a9395fdab43e68de 
<p align="center">
  <img src="https://github.com/user-attachments/assets/541aae15-d7f7-4906-9430-343a583539ad" width="80%"/>
  <img src="https://github.com/user-attachments/assets/2d0a1821-3d55-4530-9c25-7b7046dd4025" width="80%"/>
</p>

---

## 👥 9. 팀 구성 및 역할

<table>
  <tbody>
    <tr>
      <td align="center" width="250px;"><a href="https://github.com/daphoon">
          <img src="https://github.com/user-attachments/assets/2348b3b6-b7ae-408c-819d-829cd4a51d6a" height="120px;" alt=""/><br /><sub><b>박훈</b></sub></a><br />
       - 모델링 Lead <br/>
       - 프로젝트 기획 <br/>
       - EDA 
      </td>
      <td align="center" width="250px;"><a href="https://github.com/yeomsta">
          <img src="https://github.com/user-attachments/assets/93a88285-0aa4-4070-936f-07abf05cf1ad" height="120px;" alt=""/><br /><sub><b>염혜지</b></sub></a><br />
       - 분석 보고서 Lead<br/>
       - 기획 <br/>
       - EDA 
      </td>
      <td align="center" width="250px;"><a href="https://github.com/2-sehee">
          <img src="https://github.com/user-attachments/assets/2e14948f-e2c8-4efc-872d-25279bee052f" height="120px;" alt=""/><br /><sub><b>이세희</b></sub></a><br />
       - 서비스 구현 Lead<br/>
       - Streamlit UI/기능 개발<br/>
       - Edge Case 관리, 가설 설정
      </td>
      <td align="center" width="250px;"><a href="https://github.com/Euunz2">
          <img src="https://github.com/user-attachments/assets/c2db8a05-5b68-4849-a49b-100be43ae770" height="120px;" alt=""/><br /><sub><b>장은지</b></sub></a><br />
       - 지표 구축 Lead<br/>
       - 기획 <br/>
       - 모델링 
      </td>      
    </tr>
  </tbody>
</table>

---

## 🛠️ 10. Tech Stack

<div>
 <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
 <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
 <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
 <img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white" />
 <img src="https://img.shields.io/badge/polars-CD792C?style=flat-square&logo=polars&logoColor=white" />
 <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white" />
</div>

---


