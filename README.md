신용카드사 상품 가입 고객 예측
=========================


## 프로젝트 배경 
 - 은행 및 카드사는 고객 맞춤 상품을 기획/서비스하기 위해 고객의 정보나 결제내역 등을 분석하여 고객들을 세분화하고 있다.
 
 - 프로젝트에 쓰인 데이터는 고객 정보(객들의 나이, 직업, 지역, 가입기간, 평균 계좌 잔액, 대출 및 신용 상품 이용 등 인구통계학적, 행동적 특성)들로 구성되어 있다. 분석을 통해 고객을 분류하면 특정 고객에 맞는 서비스를 제공하여 비용 절감, 충성 고객 증가, 상품 기획 방향 제시 등의 장점이 있을 것으로 기대된다.
 
 - 가상의 카드사 회원 정보를 통해 이진 분류 예측 프로젝트를 작업해보았다.


## 문제 정의
 - 가상의 카드사 회원 데이터셋을 사용해, 카드사 기존 고객 중 recommended credit card 가입 제안을 수락할 고객을 예측하는 이진 분류 모델.


## 데이터셋 설명
Kaggle의 [Credit Card Lead Prediction](https://www.kaggle.com/datasets/sajidhussain3/jobathon-may-2021-credit-card-lead-prediction) 데이터셋.

- Train Dataset : 245,725 rows
- Test Dataset : 105,312 rows

***
    - ID : Unique Identifier for a row
    - Gender : Gender of the Customer
    - Age : Age of the Customer (in Years)
    - Region_Code : Code of the Region for the customers
    - Occupation : Occupation Type for the customer
    - Channel_Code : Acquisition Channel Code for the Customer (Encoded)
    - Vintage : Vintage for the Customer (In Months)
    - Credit_Product : If the Customer has any active credit product (Home loan, Personal loan, Credit Card etc.)
    - Avg_Account_Balance : Average Account Balance for the Customer in last 12 Months
    - Is_Active : If the Customer is Active in last 3 Months
    - Is_Lead : If the Customer is interested for the Credit Card [0 : Customer is not interested], [1 : Customer is interested]


#### 평가지표 
 - 해당 데이터는 imbalanced class를 가지고 있기 때문에 f1 scroe나 roc-auc curve를 평가지표로 사용한다.

## 프로젝트 진행 과정

A. Data Preprocessing


- EDA : Numerical features와 Categorical features 분포확인 및 시각화, 가설 검정
- Data Cleaning : 이상치 제거, 불필요한 column 삭제, 결측치 처리(Credit_Product의 결측치 -> 최빈값으로 처리)
- Data Reduction : Region_Code의 cardinality가 35로 높아 해당 특성 삭제 후 모델링 진행


B. Model 


- LogisticRegression
    
      report        precision    recall  f1-score   support

                 0       0.81      0.95      0.87     35359
                 1       0.63      0.25      0.36     10864

      accuracy                               0.79     46223
      macro avg          0.72      0.60      0.62     46223
      weighted avg       0.76      0.79      0.75     46223

      roc_auc_score:  0.6030095131210644


- DecisionTreeClassifier


      report        precision    recall  f1-score   support
      
                 0       0.81      0.95      0.87     35359
                 1       0.63      0.25      0.36     10864
 
      accuracy                               0.79     46223
      macro avg          0.72      0.60      0.62     46223
      weighted avg       0.76      0.79      0.75     46223

      roc_auc_score:  0.6030095131210644


- RandomForestClassifier


      report        precision    recall  f1-score   support

                 0       0.82      0.89      0.85     35359
                 1       0.49      0.34      0.40     10864
                              
      accuracy                               0.76     46223
      macro avg          0.65      0.62      0.63     46223
      weighted avg       0.74      0.76      0.75     46223

      roc_auc_score:  0.6173718483952587


- XGBClassifier


     
      report        precision    recall  f1-score   support

                 0       0.81      0.95      0.88     35359
                 1       0.64      0.28      0.39     10864

      accuracy                               0.79     46223
      macro avg          0.73      0.61      0.63     46223
      weighted avg       0.77      0.79      0.76     46223

      roc_auc_score:  0.6143925362287541
      

## 한계점 및 해결 방안.

#### 프로젝트 1차 완성 후

- 가설 검증에 필요한 데이터 분석이 미흡했다. 시각화도 제대로 이루어지지 못했고, 특성별 비율을 고려하지 않은 분석의 오류가 많았다.
- ML 모델을 구현했지만 사용한 모델에 대한 이해도는 부족한 상태로 마무리했다.

#### 프로젝트 개선 후 

- 기존에 부족했던 부분을 개선했다. 기본적으로 특성별 분포를 확인하기 위한 시각화와 가설 검정, 통계 분석 등을 한층 더 이해해 보는 시간이었다.
- Model 및 성능 개선에 목적을 두지 않은 개선이었기에 1차 완성보다 모델 성능이 떨어졌다. 기본적인 알고리즘에 대한 개념을 다시 리뷰하면서 하이퍼파라미터 튜닝과 교차검증을 다음 목표로 둔다.

