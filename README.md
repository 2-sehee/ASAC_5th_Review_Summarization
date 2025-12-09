# ASAC_5th_Review_Summarization  
### 고객 탐색 경험 향상을 위한 리뷰 키워드 요약 서비스  
**기간: 2024.06 ~ 2024.08**

---

## 📌 1. 프로젝트 개요

리뷰 플랫폼에서 “핵심 정보를 빠르게 파악하기 어렵다”는 문제를 해결하기 위해  
**키워드 기반 리뷰 요약 및 지역 기반 필터링 서비스**를 Streamlit으로 구현한 프로젝트입니다.

### 🎯 프로젝트 목표
- 긴 리뷰를 읽지 않아도 **핵심 내용만 빠르게 이해**할 수 있도록 요약 제공  
- 사용자 방문 지역 정보를 활용해 **가장 신뢰도 높은 리뷰만 필터링**  
- 시각화 기반 UI로 **효율적인 탐색 경험 제공**  

---

## 💡 2. 문제 정의

### 왜 리뷰 요약이 필요한가?
- 불필요한 내용, 중복 리뷰로 인해 **핵심 정보 파악이 어려움**
- 앱/웹에서 짧은 체류 시간 내에 의사결정을 내려야 함  
- 요약을 통해 리뷰 품질 개선 가능 (불필요 문장 제거)

👉 **목표: 사용자에게 필요한 정보를 최소한의 시간으로 제공하는 요약 모델 개발**

---

## 🚀 3. 프로젝트 최종 데모

👉 **Streamlit Demo 바로가기:**  
https://asac-map.streamlit.app/

<img src="https://github.com/user-attachments/assets/0ed6f500-2db2-479c-9c63-81e75fd62a1d" width="500px"/>
<img src="https://github.com/user-attachments/assets/0c7e2530-07d0-4649-a425-98ad3e735bab" width="500px"/>

---

## 🧠 4. 비즈니스 인사이트

<img src="https://github.com/user-attachments/assets/dba8b524-f771-4888-b629-002906af3fde"/>

---

## 🛠️ 5. 모델링 및 기술 구조

### 📌 사용 모델
<img src="https://github.com/user-attachments/assets/13f12d77-4132-4682-8bd2-8d276f856289"/>

---

## 📈 6. 모델 평가

### ✔ 정량적 평가

#### 키워드 추출 (KeyBERT)
- 4개 모델 비교 → **KeyBERT 성능 최고**
<img src="https://github.com/user-attachments/assets/4464dbc6-6b35-40b4-ac3a-6458c592afc3" width="300px"/>
<img src="https://github.com/user-attachments/assets/b57c9b7a-052b-4497-97f2-71459bb5ef36" width="500px"/>

#### 토픽 분류 (OpenAI API)
- coherence 평가를 통해 **최적 토픽: 6개**
<img src="https://github.com/user-attachments/assets/8a81ff87-12fc-4f5d-8b41-12c16f05f660"/>

- TF-IDF 기반 topic separability:
<img src="https://github.com/user-attachments/assets/7229db3e-8229-4de1-aeb4-99f257f2f36b"/>
→ 전체 유사도 0.1~0.3 → **토픽 간 분리도 양호**

---

### ✔ 정성적 평가

- 팀원 200개 샘플 직접 평가(5점 척도)
<img src="https://github.com/user-attachments/assets/0d633720-5497-4dc3-b43d-b3dd2cfcd912"/>
→ Bi-gram 기반 요약이 자연스러움  
→ 토픽 분류 성능도 우수

---

## 🗂️ 7. Edge Case 관리

프로젝트 효율적 운영을 위해  
**Edge Case / Backlog를 Notion 기반으로 체계적으로 관리**

<img src="https://github.com/user-attachments/assets/541aae15-d7f7-4906-9430-343a583539ad" width="450px"/>
<img src="https://github.com/user-attachments/assets/2d0a1821-3d55-4530-9c25-7b7046dd4025" width="450px"/>

👉 요구사항 정의 · 예외 처리 기준 · QA 흐름을 정리하며  
서비스 신뢰도를 높이는 데 기여함.

---

## 👥 8. 팀 구성 및 역할

<table>
  <tbody>
    <tr>
      <td align="center" width="250px;"><a href="https://github.com/daphoon">
          <img src="https://github.com/user-attachments/assets/2348b3b6-b7ae-408c-819d-829cd4a51d6a" height="100px;" alt=""/><br /><sub><b>박훈</b></sub></a><br />
       - 모델링 Lead <br/>
       - 프로젝트 기획 <br/>
       - EDA 
      </td>
      <td align="center" width="250px;"><a href="https://github.com/yeomsta">
          <img src="https://github.com/user-attachments/assets/93a88285-0aa4-4070-936f-07abf05cf1ad" height="100px;" alt=""/><br /><sub><b>염혜지</b></sub></a><br />
       - 분석 보고서 Lead<br/>
       - 기획 <br/>
       - EDA 
      </td>
      <td align="center" width="250px;"><a href="https://github.com/2-sehee">
          <img src="https://github.com/user-attachments/assets/2e14948f-e2c8-4efc-872d-25279bee052f" height="100px;" alt=""/><br /><sub><b>이세희</b></sub></a><br />
       - 서비스 구현 Lead<br/>
       - Streamlit UI/기능 개발<br/>
       - Edge Case 관리, 가설 설정
      </td>
      <td align="center" width="250px;"><a href="https://github.com/Euunz2">
          <img src="https://github.com/user-attachments/assets/c2db8a05-5b68-4849-a49b-100be43ae770" height="100px;" alt=""/><br /><sub><b>장은지</b></sub></a><br />
       - 지표 구축 Lead<br/>
       - 기획 <br/>
       - 모델링 
      </td>      
    </tr>
  </tbody>
</table>

---

## 🛠️ 9. Tech Stack

<div>
 <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
 <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
 <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
 <img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white" />
 <img src="https://img.shields.io/badge/polars-CD792C?style=flat-square&logo=polars&logoColor=white" />
 <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white" />
</div>

---

## 📎 10. 설치 및 실행 방법

```bash
git clone https://github.com/2-sehee/ASAC_5th_Review_Summarization.git
cd ASAC_5th_Review_Summarization

pip install -r requirements.txt

streamlit run app.py
