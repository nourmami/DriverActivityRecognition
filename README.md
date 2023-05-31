# Introduction 
Distracted driving is a major concern, as it is the cause of many accidents, injuries and deaths. These distractions can significantly impair a driver's ability to focus on the road, react quickly to potential hazards, and make safe driving decisions. Statistical data from the CDC's Motor Vehicle Safety Division shows that about one in five car accidents is caused by driver distraction. 
With the emergence of artificial intelligence, we can now detect various human behavior in public spaces (streets, parks, ...) or closed spaces (malls, houses, cars, ...). 

In this context, we propose a new method to study the driver's behavior by detecting his distractions. The proposed solution relies on advanced technologies such as computer vision and machine learning to mitigate accident risks and enhance road safety.
Since it is a critical task that affects people's lives, the proposed solution need to be precise and fast when predicting behavior so we can later generate alerts as soon as an unsafe action happens.
The project aims to explore different computer vision approaches  to recognize the activity of the driver with the highest accuracy and as near as possible to real-time.

# DataSet 
The StateFarm distraction-detection dataset is selected for our human activity project.This dataset is obtained from Kaggle : ``State Farm Distracted Driver Detection competition``
| Class | Driver Behavior            | Number of images |
|-------|---------------------------|-----------------|
| C0    | Safe Driving              | 2489            |
| C1    | Texting-Right             | 2267            |
| C2    | Talking on the Phone-Right| 2317            |
| C3    | Texting Left              | 2346            |
| C4    | Talking on the Phone-Left | 2326            |
| C5    | Operating the radio       | 2312            |
| C6    | Drinking                  | 2325            |
| C7    | Reaching Behind           | 2002            |
| C8    | Hair and Makeup           | 1911            |
| C9    | Talking to Passenger      | 2129            |

![Classes image examples](images/images-classes.png)
