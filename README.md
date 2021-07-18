### Crawling_Project
## 목차
![image](https://user-images.githubusercontent.com/79970424/126070640-f4e218ae-db73-4bf6-96b3-94bbededa357.png)

---
## 프로젝트 목적
![image](https://user-images.githubusercontent.com/79970424/126070646-180f679b-8b96-4e7f-a5d0-52ac3a47eecb.png)
- 너무 많은 리뷰들로 호텔을 선택할때 판단이 힘듬
- 또한 리뷰들이 섞여 있어 장점만 보고 싶거나, 단점만 보고 싶을 때 골라서 읽어야함
- 한눈에 좋은리뷰만, 한눈에 나쁜리뷰만 볼 수 없을까?
---
## 웹크롤링 진행과정
![image](https://user-images.githubusercontent.com/79970424/126070648-a4b86a62-6658-4fb8-9098-49a2fa658cf6.png)
- 네이버 호텔 크롤링, 서울 호텔 3000개
- 워드클라우드 제작
- 챗봇 서비스 구현, Slack
---
## 웹크롤링 진행과정 도식화
![image](https://user-images.githubusercontent.com/79970424/126070649-7f76c60e-758b-4358-b1c5-3d5a88677540.png)

---
## 웹크롤링 진행과정 네이버 호텔
![image](https://user-images.githubusercontent.com/79970424/126070650-20197f72-e458-432b-b914-08017d0f41ac.png)

---
## 웹크롤링 진행과정 네이버에 있는 부킹닷컴의 리뷰를 클롤링
![image](https://user-images.githubusercontent.com/79970424/126070654-d1dfe28a-d19d-4680-9b58-eb81923d8d00.png)

---
## 웹크롤링 진행과정 호텔리뷰들은 txt, 워드클라우드는 jpg로 서버에 저장
![image](https://user-images.githubusercontent.com/79970424/126070658-34d7e07c-e3a8-4906-9eba-b6a140478020.png)

---
## 웹크롤링 진행과정 호텔정보
![image](https://user-images.githubusercontent.com/79970424/126070660-42d0fe36-1927-44b2-89d9-f56331516315.png)
- 호텔정보는 크롤링하여 Mysql DataBase에 저장하여 업데이트 및 서비스
---
## 웹크롤링 진행과정 '싫어요 워드클라우드'
![image](https://user-images.githubusercontent.com/79970424/126070663-c2e5d69e-9f11-4383-bed5-d6e126020b38.png)

---
## 웹크롤링 진행과정 '좋아요 워드클라우드'
![image](https://user-images.githubusercontent.com/79970424/126070667-97555f16-7b26-4368-b816-211b03d927ae.png)

---
## 웹크롤링 진행과정 서비스화를 위한 Flask구축
![image](https://user-images.githubusercontent.com/79970424/126070669-1cbcb70a-1560-4bda-b1eb-89b811a8511f.png)

---
## 챗봇 서비스 구현
![image](https://user-images.githubusercontent.com/79970424/126070675-6c2255e7-cd6b-4cbf-b955-78163031b275.png)
- $like -> 호텔의 이름을 검색 -> '좋아요 워드클라우드' 제공
- $dislike -> 호텔의 이름을 검색 -> '싫어요 워드클라우드' 제공

---
## 챗봇 서비스 구현
![image](https://user-images.githubusercontent.com/79970424/126070676-8c56b31e-e301-4792-b32e-e53cc3dfa809.png)
- 호텔정보 제공
- 번역 제공
- 환율 제공
