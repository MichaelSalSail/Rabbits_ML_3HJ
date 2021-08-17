# Forecasting Invasive Species
## Team Name: Beware Bunnies
## Team Members: Asma Sadia, Dor Ulman, Michael Salamon, Nahin Imtiaz  

### Problem Description  
Invasive species include any animal, plant, or disease that negatively 
impacts the environment because of its high population growth. Australia 
is overrun by wild rabbits. Predators introduced to new areas, such as 
the Burmese python in Florida, lead to sharp declines in prey populations 
and are thereby viewed as more harmful invasive species. Although rabbits 
are classified as pests, their impact has been devastating. They lead to 
the opposite problem of inflated predator populations. Furthermore, rabbit 
homes erode the soil leading to desertification while crop destruction has 
impacted the economy. Australia has used controlled virus outbreaks and 
dogs to keep rabbit populations in check, but this costs money and resources. 
Being able to predict areas in Australia that see the highest rabbit 
population growth will allow the Australian government to combat the problem 
more effectively.  

![Ominous rabbits](https://user-images.githubusercontent.com/47184848/129650949-aa2c4d2f-c4df-4a93-9f6e-90077dea90bb.jpg)


### Implementation  
Using machine learning to predict the future using past data is called **time series forecasting**. 
The data used includes two datasets accompanying the research paper *The Australian National Rabbit Database: 50 years of population monitoring of an invasive species*. The first dataset is called 
**occurence**: each row is a reported sighting of a rabbit(s) from someone in Australia. The second 
dataset is called **abundance**: each row is a headcount of rabbits spotted by researchers from going 
through a path at night. We used this second dataset to train our models.

One common problem in forecasting is getting a high accuracy model because the features used in training 
didn't have continous time intervals... one of the inputs already had information about the 
future. We made sure to identify such problem features and remove them before training. Other challenges 
the team faced in this project was making sure we were interpreting the dataset features correctly and creating relevant data visualizations.  

Improvements could be made by creating a baseline model to make comparisons with our forecasting 
models. Our methods for evaluating classification can also be improved.  

### For more information, look at Rabbit Forecasting . ipynb

