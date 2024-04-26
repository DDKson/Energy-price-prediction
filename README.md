![image](https://github.com/DDKson/Energy-price-prediction/assets/92723196/ef27da5f-2a9c-4e35-a101-32baf4031de9)# Energy-price-prediction
Result summary: 

|           | 2023 test result |             |             |             |             |             |
|-----------|------------------|-------------|-------------|-------------|-------------|-------------|
|           |        MAE       |     MAPE    |    SMAPE    |     RMSE    |   MAE_peak  | MAE_nonpeak |
|           | 16.97973589      | 1.28209E+14 | 0.157511512 | 22.42016772 | 24.62805557 | 14.62947749 |
| Precision |       0.88       |     0.85    |     0.87    |     0.87    |     0.87    |     0.88    |
|   Recall  |       0.83       |     0.79    |     0.90    |     0.87    |     0.8     |     0.89    |
| F-measure |       0.85       |     0.82    |     0.88    |     0.87    |     0.83    |     0.88    |

Daily evaluation:
|                       | Back-testing result |             |             |             |             |             |
|-----------------------|---------------------|-------------|-------------|-------------|-------------|-------------|
|  PREDICTION_TIME_END  |         MAE         |     MAPE    |    SMAPE    |     RMSE    |   MAE_peak  | MAE_nonpeak |
| 2023-01-31   00:00:00 | 27.73381554         | 7.67165E+14 | 0.224942041 | 34.62252461 | 30.42135774 | 20.85422189 |
| 2023-02-28   00:00:00 | 14.37652377         | 0.099160019 | 0.104405694 | 18.07296449 | 13.52520409 | 15.61311221 |
| 2023-03-31   00:00:00 | 14.42630866         | 0.126385734 | 0.118207241 | 18.61698626 | 17.29377547 | 12.74136556 |
| 2023-04-30   00:00:00 | 11.0951017          | 0.092040211 | 0.093314681 | 14.96284662 | 13.84456794 | 10.57787537 |
| 2023-05-31   00:00:00 | 11.07812366         | 0.113095923 | 0.105754257 | 13.67025316 | 26.98833553 | 10.72844868 |
| 2023-06-30   00:00:00 | 13.87934909         | 0.111912451 | 0.1157058   | 21.58070442 | 38.024381   | 10.07514792 |
| 2023-07-31   00:00:00 | 13.37520613         | 0.546158145 | 0.170326678 | 18.01573484 | 43.29214101 | 12.54877147 |
| 2023-08-31   00:00:00 | 10.89966689         | 0.113644053 | 0.109983331 | 13.91735377 | 19.85794884 | 10.44416103 |
| 2023-09-30   00:00:00 | 15.67726953         | 9.07297E+14 | 0.188909499 | 23.0923661  | 38.35049459 | 12.43823738 |
| 2023-10-31   00:00:00 | 14.80715921         | 1.92093E+14 | 0.1325835   | 20.31478127 | 21.85276449 | 12.73636391 |
| 2023-11-30   00:00:00 | 13.79460813         | 0.18334865  | 0.125663225 | 18.32845695 | 20.39823921 | 12.29838507 |

Streamlit Dashboard snapshot:
![image](https://github.com/DDKson/Energy-price-prediction/assets/92723196/c84ef0f6-5632-4f77-b0f5-cae896bdd626)
