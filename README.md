# Columbia DSI x KPMG Lighthouse Capstone Project Fall 2022
## Optimization on EV Charging Station Locations in Washington Shate

This is the GitHub repository for Fall 2022 Columbia University MS in Data Science Capstone project collaborating with KPMG.

* Note that the path in .ipynb files may need to manually adjust case by case becasue we've done all the works on Google Drive.

## Team members
  - **Yu-Chieh Elvy Chen** - [GitHub](https://github.com/elvychen), [LinkedIn](https://www.linkedin.com/in/elvychen/)
  - **Anne Lin** - [GitHub](https://github.com/anqilin11), [LinkedIn](https://www.linkedin.com/in/anqil/)
  - **Clarissa Tai** - [GitHub](https://github.com/clarissarjtai) , [LinkedIn](https://www.linkedin.com/in/clarissarjtai/)
  - **Mengchen Xu** - [GitHub](https://github.com/Helen962), [LinkedIn](https://www.linkedin.com/in/mengchen-xu/)
  - **Yue Zhang** - [GitHub](https://github.com/stellazhangyue)


### The Final Data File we used is:
- "DSI_Capstone_KPMG/4_Preprocessing/Data/main_dataset_all_interstate_all_route_10mi_w_income.csv"

The data schema is as follows:

| Features                        | Data Type           | 
|---------------------------------|:-------------:| 
| gas_key                         | Numerical |  
| gas_name                        |    Categorical   |    
| gas_lat                         |   Numerical    | 
| gas_long                        | Numerical |
| attr_cnt_1mile                  | Numerical |  
| attr_cnt_5mile                  |  Numerical     |    
| attr_name                       |   Categorical    | 
| attr_lat                        | Numerical |
| attr_long                         | Numerical |  
| distance_to_nearest_attr        |    Numerical   |    
| crime_coord                         |   Categorical    | 
| crime_county                        | Categorical |
| crime_population                         | Numerical |  
| violent_crime                        |   Numerical    |    
| murder_nonnegligent_manslaughter      |   Numerical    | 
| Rape1                         | Numerical |
| Robbery                   | Numerical |  
| aggravated_assault                  |  Numerical     |    
| property_crime                       |   Numerical    | 
| Burglary                        | Numerical |
| larceny_theft                         | Numerical |  
| motor_vehicle_theft         |   Numerical    |    
| Arson                          |   Numerical    | 
| total_crime                        | Numerical |
| exit_name | Categorical |
| exit_lat                         |   Numerical    | 
| exit_long                        | Numerical |
| distance_to_nearest_exit                  | Numerical |  
| highway                   |  Categorical     |    
| num_EV_in_2_miles_of_gas     |   Numerical    | 
| num_EV_in_5_miles_of_gas         | Numerical |
| num_EV_in_10_miles_of_gas           | Numerical |  
| num_EV_in_20_miles_of_gas          |   Numerical    |    
| num_EV_in_50_miles_of_gas               |   Numerical    | 
| Closest_EV_Station_name                        | Categorical |
| Closest_EV_Station_lat | Numerical |
| Closest_EV_Station_long      |   Numerical    | 
| distance_to_closest_ev_station             | Numerical |
| num_EV_in_10_miles_of_gas             | Numerical |  
| nri_geoid                        |   Categorical    |    
| nri_county                         |   Categorical    | 
| nri_population                        | Numerical |
| nri_build_value | Numerical |
| nri_agri_value                        | Numerical |
| nri_area                         | Numerical |  
| nri_risk_score                        |   Numerical    |    
| nri_risk_rating                         |   Categorical    | 
| nri_intpt_lat                        | Numerical |
| nri_intpt_long | Numerical |
| nri_zipcode                         | Categorical |  
| census_tract_area                         |   Numerical    | 
| census_tract_category                        | Categorical |
| traff_cnt_10m_avg | Numerical |
| traff_cnt_10m_max                       |   Numerical    | 
| traff_cnt_5m_avg                        | Numerical |
| traff_cnt_5m_max                         | Numerical |
| zip | Categorical |
| zip_income                        | Numerical |
| household_median_income                         | Numerical |            




