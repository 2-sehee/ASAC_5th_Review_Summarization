# ASAC_5th_Review_Summarization
고객 탐색 경험 향상을 위한 리뷰 키워드 요약 (with YELP dataset)
<br/>
2024. 06 ~ 2024. 08


<br/>


## 💡 프로젝트 문제정의
* 요약의 궁극적인 목표는 **핵심만 추출하여 간결하게 표현하는 것**
* 유저들이 **한 눈에 리뷰의 정보에 대해 파악**할 수 있도록 요약하는 것이 우리의 목표
* 요약의 필요성
  * 리뷰의 핵심 내용을 빠르게 파악할 수 있음 → 빠르고 효율적인 의사결정
  * 짧은 시간 내에 다양한 리뷰를 읽을 수 있음 → 짧은 앱 체류시간 내 요약된 리뷰를 여러개 제공해 **충분한 의사결정의 근거 제공**
  * 리뷰의 품질 향상가능 → 중복되거나, 불필요한 내용이 제거된 리뷰 확인 가능

<br/>

## 💻 프로젝트 최종목표 
배포된 최종 서비스 데모 체험하기 👉🏻 https://asac-map.streamlit.app/ <br/> 
![image](https://github.com/user-attachments/assets/0ed6f500-2db2-479c-9c63-81e75fd62a1d)
![image](https://github.com/user-attachments/assets/0c7e2530-07d0-4649-a425-98ad3e735bab)


<br/>

## 🗣️ 비즈니스 인사이트
![image](https://github.com/user-attachments/assets/dba8b524-f771-4888-b629-002906af3fde)


<br/>

## 👨🏻‍🔧 사용 모델
![image](https://github.com/user-attachments/assets/13f12d77-4132-4682-8bd2-8d276f856289)

<br/>

## 📊 모델 평가
* **정량적 평가**
  
  * 키워드 추출 (KeyBERT)
    <br/> ✅ 키워드를 추출하는 모델 4가지 비교 결과, KeyBERT의 성능이 가장 높아 해당 모델 선정 <br/>
    <img src="https://github.com/user-attachments/assets/4464dbc6-6b35-40b4-ac3a-6458c592afc3" width="300px"/>
    <img src="https://github.com/user-attachments/assets/b57c9b7a-052b-4497-97f2-71459bb5ef36" width="500px"/>
    
  * 토픽 분류 (OpenAI API)
    <br/> ✅ pyLDAvis를 통해 분류된 토픽 내 Keyword들의 coherence를 측정, **keyword 간 응집도가 높은지** 평가 진행
    ![image](https://github.com/user-attachments/assets/8a81ff87-12fc-4f5d-8b41-12c16f05f660)   <br/>
    → coherence가 가장 높은 **최적의 topic 개수는 6개로** 잘 분류되었음을 확인  <br/>
    <br/> ✅ 또한, TF-IDF 기반 코사인 유사도 측정, **토픽 간 분리도가 높은지 평가** 진행
    ![image](https://github.com/user-attachments/assets/7229db3e-8229-4de1-aeb4-99f257f2f36b)  <br/>
    → **전반적인 코사인 유사도 값은 0.1~0.3으로 낮기에, 토픽 간 분리도가 높다고 볼 수 있음**

* **정성적 평가**
  
  * 키워드 추출 (KeyBERT)
    <br/> ✅ 팀원들이 직접 5점 척도를 기준으로 약 200개의 샘플에 대해 평가 진행
    ![image](https://github.com/user-attachments/assets/0d633720-5497-4dc3-b43d-b3dd2cfcd912)  <br/>
    → Uni-gram보다 **Bi-gram이 문장을 비교적 잘 요약하고 있다**고 평가하였으며, **토픽 분류에 대한 부분도 잘 되었다고 평가함**

<br/>    

## 🚨 Edge case
✅ Edge case와 Back log를 관리하며 프로젝트 규모 및 디테일 조정
![image](https://github.com/user-attachments/assets/541aae15-d7f7-4906-9430-343a583539ad)
![image](https://github.com/user-attachments/assets/2d0a1821-3d55-4530-9c25-7b7046dd4025)


<br/>

## 🙋🏻 프로젝트 팀원
<table>
  <tbody>
    <tr>
      <td align="center" width="250px;"><a href="https://github.com/daphoon">
          <img src="https://github.com/user-attachments/assets/2348b3b6-b7ae-408c-819d-829cd4a51d6a" height="100px;" alt=""/><br /><sub><b>박훈</b></sub></a><br />
       - 모델링 Lead <br/>
       - 프로젝트 기획 <br/>
       - EDA <br/>
      </td>
      <td align="center" width="250px;"><a href="https://github.com/yeomsta">
          <img src="https://github.com/user-attachments/assets/93a88285-0aa4-4070-936f-07abf05cf1ad" height="100px;" alt=""/><br /><sub><b>염혜지</b></sub></a><br />
       - 분석 보고서 작성 Lead<br/>
       - 프로젝트 기획 <br/>
       - EDA <br/>
      </td>
      <td align="center" width="250px;"><a href="https://github.com/2-sehee">
          <img src="https://github.com/user-attachments/assets/2e14948f-e2c8-4efc-872d-25279bee052f" height="100px;" alt=""/><br /><sub><b>이세희</b></sub></a><br />
       - 프로젝트 서비스 구현 Lead<br/>
       - 프로젝트 기획 및 Edge case 관리<br/>
       - EDA 및 가설설정<br/>
      </td>
      <td align="center" width="250px;"><a href="https://github.com/Euunz2">
          <img src="https://github.com/user-attachments/assets/c2db8a05-5b68-4849-a49b-100be43ae770" height="100px;" alt=""/><br /><sub><b>장은지</b></sub></a><br />
       - EDA 및 평가지표 구축 Lead<br/>
       - 프로젝트 기획 <br/>
       - 모델링 <br/>
      </td>      
    </tr>
  </tbody>
</table>


<br/>
<hr/>
<br/>

## 🛠️ Languages and Libraries

<div>
 <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
 <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
 <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
 <img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white" />
 <img src="https://img.shields.io/badge/polars-CD792C?style=flat-square&logo=polars&logoColor=white" />
 <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white" />
</div>
