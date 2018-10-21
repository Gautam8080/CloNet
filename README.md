## StyleAI
Introducing Fashion Sense - a novel concept of daily clothing recommendation based on current market fashion.

#How it works. 
1.	Upload the images – Images from Instagram, selfies, your private ugly pictures. We accept everything. Our fashion detection algorithm automatically takes out and prepares a virtual wardrobe based on your data.
2.	Wait! That’s it. You are all set.

###Project Description-
##Part 1 – Category Detection

#Preparation of Dataset
We used the public Deep Fashion data that has over 161000 images with a domain of 51 categories of clothes in every possible environment. We performed the data cleaning on the same. We also tried to reduce the categories to make it more generalised instead. 
Model – 
The prepared dataset was trained on the inception network implemented with the help of Tensorflow with pretrained weights for object detection. The outcome of network were bounding boxes on images. The bounding boxes around images are cropped and saved in different directories based on their predicted categories.

##Part 2 – 
#Preparation of dataset
The previous network acts as a data generating stream for this network that will be used for testing purpose of Fashion Sense algorithm. For the training, we fed the program  a number of fashion styles that were compatible with current fashion. Based on the training data, the network generates a universal embedding that has learned the fashion style. All possible matches of users clothing are tested against the universal style embedding. With a basic L2 norm, the difference is calculated. The matches are stored in an ascending order of L2 norm values. 
User is given choice to select number of recommendations he wants that will be applied to the same number of days and reshuffled for next cycle. 
##A Step Beyond*
The clothes that do not make the cut in users’ wardrobe are suggested to be donated a local homeless welfare organization.
##Future Work
We plan to constantly improve the fashion embedding by providing it a better training data to predict better and better results for the user. Since we understand there always has been a difference in fashion styles among different genders, age groups and other factors, we plan to generate user specific that would only take in regard features that he is involved with.
