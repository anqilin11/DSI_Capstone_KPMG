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

| Features                         | Type           |                                                                                                                                                 Description |
|----------------------------------|:-------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| gas_key                          | Numerical |                                                                                                                                             Gas station key |
| gas_name                         |    Categorical   |                                                                                                                                           Gas station namec |
| gas_lat                          |   Numerical    |                                                                                                                               Gas station location latitude |
| gas_long                         | Numerical |                                                                                                                              Gas station location longitude |
| attr_cnt_1mile                   | Numerical |                                                                                                        Number of tourism attractions within 1 mile distance |
| attr_cnt_5mile                   |  Numerical     |                                                                                                        Number of tourism attractions within 5 mile distance |    
| attr_name                        |   Categorical    |                                                                                                                              Name of the tourism attraction | 
| attr_lat                         | Numerical |                                                                                                                        Tourism attraction location latitude |                                                    
| attr_long                        | Numerical |                                                                                                                       Tourism attraction location longitude |  
| distance_to_nearest_attr         |    Numerical   |                                                                                                                 Distance to the nearest tourists attraction |                                                        
| crime_coord                      |   Categorical    |                                                                                                       Crime data location coordinate: (longitude, latitude) |
| crime_county                     | Categorical |                                                                                                                                 Crime happened county label |                                              
| crime_population                 | Numerical |                                                                                                                            Crime population in county label |                                                   
| violent_crime                    |   Numerical    |                                                                                                                               Number of violent crime cases |                                              
| murder_nonnegligent_manslaughter |   Numerical    |                                                                                                            Number of muder/non-negligent manslaughter cases |
| Rape1                            | Numerical |                                                                                                                                        Number of rape cases |
| Robbery                          | Numerical |                                                                                                                                     Number of robbery cases |
| aggravated_assault               |  Numerical     |                                                                                                                         Number of  aggravated assault cases |   
| property_crime                   |   Numerical    |                                                                                                                              Number of property crime cases |
| Burglary                         | Numerical |                                                                                                                                    Number of burglary cases |
| larceny_theft                    | Numerical |                                                                                                                               Number of larceny-theft cases | 
| motor_vehicle_theft              |   Numerical    |                                                                                                                             Number of vehicles stolen cases |   
| Arson                            |   Numerical    |                                                                                                                                    Number of arson offenses |
| total_crime                      | Numerical |                                                                                           Number of summed crimes (including theft, burglary, murder, etc.) |
| exit_name                        | Categorical |                                                                                                                                        Name of highway exit |
| exit_lat                         |   Numerical    |                                                                                                                              Highway exit location latitude |
| exit_long                        | Numerical |                                                                                                                             Highway exit location longitude |
| distance_to_nearest_exit         | Numerical |                                                                                                                        Distance to the nearest highway exit |
| highway                          |  Categorical     |                                                                                                                           Name of Highway, for example “I5” |   
| num_EV_in_2_miles_of_gas         |   Numerical    |                                                                                                 Number of EV stations within 2 mile distance of gas station |
| num_EV_in_5_miles_of_gas         | Numerical |                                                                                                 Number of EV stations within 5 mile distance of gas station |
| num_EV_in_10_miles_of_gas        | Numerical |                                                                                                Number of EV stations within 10 mile distance of gas station | 
| num_EV_in_20_miles_of_gas        |   Numerical    |                                                                                                Number of EV stations within 20 mile distance of gas station |   
| num_EV_in_50_miles_of_gas        |   Numerical    |                                                                                                Number of EV stations within 50 mile distance of gas station | 
| Closest_EV_Station_name          | Categorical |                                                                                                                              Name of the closest EV station |
| Closest_EV_Station_lat           | Numerical |                                                                                                                        Closest EV station location latitude |
| Closest_EV_Station_long          |   Numerical    |                                                                                                                      Closest EV station location longtitude |
| distance_to_closest_ev_station   | Numerical |                                                                                                                 Distance to the nearest EV charging station | 
| nri_geoid                        |   Categorical    |                                                                            Geographic identifiers that uniquely identify all administrative geographic area |   
| nri_county                       |   Categorical    |                                     County names that corresponds to the Geographic identifiers in the previous column, for example “King” as “King County” |
| nri_population                   | Numerical |                                                                                                                                                             |
| nri_build_value                  | Numerical |                                                                                                                                                             |
| nri_agri_value                   | Numerical |                                                                                                                                                             |
| nri_area                         | Numerical |                                                                                                                                                             |   
| nri_risk_score                   |   Numerical    |                                                  Relative risk of natural hazards at a location, higher value means higher risk, a number in range [0, 100] |  
| nri_risk_rating                  |   Categorical    | Relative rating of communities at the same level, categories include  “Very High”, “Relatively High”, “Relatively Moderate”,“Very Low” and “Relatively Low” |
| nri_intpt_lat                    | Numerical |                                                                                                                                                             | 
| nri_intpt_long                   | Numerical |                                                                                                                                                             | 
| nri_zipcode                      | Categorical |                                                                                                                                                             |   
| census_tract_area                |   Numerical |                                                                                                                                                             | 
| census_tract_category            | Categorical |                                                                                                                                                             |
| traff_cnt_10m_avg                | Numerical |                                                                                                                       Average traffic count within 10 miles |
| traff_cnt_10m_max                |   Numerical    |                                                                                                                       Maximum traffic count within 10 miles | 
| traff_cnt_5m_avg                 | Numerical |                                                                                                                        Average traffic count within 5 miles |
| traff_cnt_5m_max                 | Numerical |                                                                                                                        Maximum traffic count within 5 miles |
| zip                              | Categorical |                                                                                                                                      zipcode of gas station |
| zip_income                       | Numerical |                                                                                                                zipcode of gas station used for merge income |
| household_median_income          | Numerical |                                                                                                                Median income of household in zip code level |




