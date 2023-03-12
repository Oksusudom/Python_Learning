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



## 평가지표 / Baseline / 가설 설정


#### 평가지표 
 - dataset의 target특성은 'Is_Lead'이다.
 - Train Dataset에서 'Is_Lead'가 '1'인(가입 제안을 수락할) 고객의 데이터를 통해, Test Dataset의 고객 데이터에서 'Is_Lead'를 예측한다.
 - 해당 데이터는 imbalanced class를 가지고 있기 때문에 f1 scroe나 roc-auc curve를 평가지표로 사용한다.


#### Baseline
 - 이 프로젝트는 이진 분류 문제로 Target의 최빈class 비율을 기준 모델로 세운다.

## 프로젝트 진행 과정

### Target
<img src="https://user-images.githubusercontent.com/81462099/193682454-9b9a57da-2297-468e-b6f4-60e6b64ce0fe.png"  width ="545" height="370">
- Target Class가 불균형하기 때문에 f1 score나 roc_auc score로 모델의 성능 측정


### 가설 검증
 이진 분류 모델 구현에 앞서 고객 세분화 및 분류를 위해 5가지 가설을 설정하고 검증을 진행했다.
 
#### 가설 1 : Two Sample T-Test

- 귀무가설 : 'Age'에 상관없이 카드를 발급받을 가능성이 차이가 나지 않을 것이다.
- 대안가설 : Age가 30 ~ 60 사이의 고객이 신용카드를 발급받을 가능성이 유의미하게 높을 것이다.
![가설1](https://user-images.githubusercontent.com/81462099/193642080-5950a605-2e05-45ce-8536-f81d4ceff047.png)
- 가설 1 검증 : 'Age'별 'Is_Lead'가 1인 고객을 비율로 나타내, 'Age'가 40 중반에서 60 중반, 그 다음으로 75 이상인 고객이 신규 카드를 발급받을 가능성이 높다.
 

#### 가설 2 : Two Sample T-Test

- 귀무가설 : 'Vintage'값에 상관없이 카드를 발급받을 가능성이 차이가 나지 않을 것이다.
- 대안가설 : 고객의 'Vintage'값에 카드를 발급받을 가능성이 비례할 것이다.
![가설2](https://user-images.githubusercontent.com/81462099/193642095-2b003e32-3563-4ead-a22f-91238f2865a3.png)
- 가설 2 검증 : 'Vintage'별 'Is_Lead'가 1인 비율로 나타내, 'Vintage'가 80~90인 고객이 카드를 발급받을 가능성이 높다.


#### 가설 3 : Two Sample T-Test ('Credit_Product' 결측치를 삭제하고 진행.)

- 귀무가설 : 'Credit_Product'를 이용하는 고객과 이용하지 않는 고객이 카드를 발급받을 가능성은 차이가 없다.
- 대안가설 : 'Credit_Product'를 이용하는 고객이 카드를 발급받을 가능성이 유의미하게 차이가 난다.
<img width="545" alt="가설3" src="https://user-images.githubusercontent.com/81462099/193642233-cbec145a-c245-4008-b6b3-33d0270c142e.png">
- 가설 3 검증 : 'Creadit_Product'가 Yes/No/NaN(결측치)이고 'Is_Lead'가 1/0인 모든 경우를 직접 비교하여 'Credit_Product'가 NaN인 고객이 목표 고객일 가능성이 높게 나왔다. 하지만 결측치이기 때문에 검증에 확신을 가질 순 없었다.


#### 가설 4 : Two Sample T-Test

- 귀무가설 : 'Avg_Account_Balance'가 적은 고객과 높은 고객의 카드 발급 가능성은 차이가 없다.
- 대안가설 : 'Avg_Account_Balance'가 적은 고객이 카드를 발급받을 가능성에서 유의미하게 차이가 난다.
<img src="https://user-images.githubusercontent.com/81462099/193642244-60aee87e-aba9-4a30-a9eb-3b1558664768.png" width ="545" height="370">
- 가설 4 검증 : 'Is_Lead'별로 'Avg_Account_Balance'를 확인할 수 있게 plot을 개선하여 확인해본 결과, 'Is_Lead'와 'Avg_Account_Balance'는 유의미한 상관이 없는 것으로 확인했다.


#### 가설 5 : Two Sample Chi Squre Test

- 귀무가설 : 'Occupation'에 관계없이 카드를 발급받을 가능성에 유의미한 차이가 없을 것이다.
- 대안가설 : 특정 'Occupation'이 카드를 발급받을 가능성이 유의미하게 높을 것이다.
<img src="https://user-images.githubusercontent.com/81462099/193643623-e2a5482a-bfc5-43ed-af6b-1e9da4ac140f.png"  width ="545" height="370">
- 가설 5 검증 : Entrepreneur가 목표 고객일 가능성이 높긴하지만, 전체 고객 중 Entrepreneur의 절대수가 부족해 충분한 인과관계를 뽑아 내기엔 경우의 수가 너무 적어 일반화할 수 없었다.


### ML Model Test

#### LogisticRegression : f1 score 점수가 나오지 않음.

    train accuracy: 0.7622263342299206
    validation accuracy: 0.7659477057686438
    report               precision    recall  f1-score   support

                     0       0.77      1.00      0.87     30114
                     1       0.00      0.00      0.00      9202

              accuracy                           0.77     39316
             macro avg       0.38      0.50      0.43     39316
          weighted avg       0.59      0.77      0.66     39316

    roc_auc_score:  0.5

#### DecisionTreeClassifier : 과적합 발생.

    train accuracy: 1.0
    validation accuracy: 0.7862193509003967
    report               precision    recall  f1-score   support

                      0       0.87      0.85      0.86     30114
                      1       0.54      0.57      0.55      9202

               accuracy                           0.79     39316
              macro avg       0.70      0.71      0.71     39316
           weighted avg       0.79      0.79      0.79     39316

    roc_auc_score:  0.7108378403319289

#### RandomForestClassifier : 과적합 발생.

    train accuracy: 0.9999364122520873
    validation accuracy: 0.8544104181503713
    report               precision    recall  f1-score   support

                      0       0.88      0.94      0.91     30114
                      1       0.74      0.58      0.65      9202

               accuracy                           0.85     39316
              macro avg       0.81      0.76      0.78     39316
           weighted avg       0.85      0.85      0.85     39316

    roc_auc_score:  0.7581819528449286

#### XGBClassifier : roc_auc_score 성능이 가장 좋은 XGB 하이퍼파라미터 조정 진행.

    train accuracy: 0.8604694047550918
    validation accuracy: 0.8631091667514498
    report               precision    recall  f1-score   support

                      0       0.87      0.96      0.92     30114
                      1       0.82      0.53      0.64      9202

               accuracy                           0.86     39316
              macro avg       0.85      0.75      0.78     39316
           weighted avg       0.86      0.86      0.85     39316

    roc_auc_score:  0.7473335657617045

#### XGBClassifier 하이퍼파라미터 조정.

    best_params:  {'simpleimputer__strategy': 'most_frequent', 'xgbclassifier__max_depth': 5, 'xgbclassifier__n_estimators': 213}

### 최종 사용 모델 : XGBClassifier
 - 높은 병렬 처리로 학습과 처리가 빠른 XGBoost모델을 사용했다.



### 결과 

    train accuracy: 0.8284593324558224
    
    validation accuracy: 0.8224132668633635

    Report:     precision    recall  f1-score   support

              0       0.92      0.84      0.88     30114
              1       0.59      0.78      0.67      9202
           
    accuracy                               0.82     39316
    macro avg          0.76      0.81      0.78     39316
    weighted avg       0.85      0.82      0.83     39316

    roc_auc_score:  0.8064582219241158

### Feature Importance
<img src="https://user-images.githubusercontent.com/81462099/193683798-41233ca4-1247-4792-9724-8a4371e02f45.png"  width ="600" height="320">



### Permutation Importance
<img src="https://user-images.githubusercontent.com/81462099/193683805-b48f4732-be53-45e1-a991-fd90ff2b48dd.png" width ="450" height="320">


## 한계점 및 해결 방안.

#### 프로젝트 1차 완성 후

- 가설 검증에 필요한 데이터 분석이 매우 미흡했다고 생각한다. 대부분의 분석을 Target값과 다른 특성들의 절대값으로 비교했고, 특성별 비율을 고려하지 않은 분석의 오류가 많았다.

- ML 모델을 구현했지만 사용한 모델에 대한 이해도는 부족한 상태로 마무리했다.

- ML 모델의 interpretation 과정에서 Feature Importance를 분석하고 plot으로 그리는 부분에 이해도가 부족해 깔끔하게 마무리하지 못했다.

#### 프로젝트 개선 후 

- 프로젝트 초기 계획은 모델의 성능 향상까지 진행하는 것이었지만, 여러 번의 시도에도 성능을 올리지 못했다.

- 분석을 개선했지만 해당 데이터에 대해 기술적으로 더 잘 다루거나 좋은 인사이트를 뽑지 못한 점이 아쉽다.

- 개선의 궁극적인 목표는 데이터 분석을 더 구체적으로, 가설 검증을 조금 더 구체적이고 비지니스 측면에서 해보는 것이다. 이후에는 ML모델 성능의 개선을 진행해보고 싶다.

- 데이터 특성 분석 시, p-value나 상관계수를 구해 좀 더 구체적인 분석이 되도록 한다.

