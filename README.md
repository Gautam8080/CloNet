## CloNet
A novel concept of Personalized Clothing Recommendations from Closet using Neural Networks. 

![CloNet - initially published as styleAI](https://github.com/Gautam8080/Pet-Portal/blob/master/pet-portal.jpg?raw=true)

# Overview
CloNet is an intelligent AI system that provides daily recommendations to users with deep learning, based on personal preferences and fashion trends, using regular photos of the user wearing the clothes or photos of user clothes in general. Thus, the system will require minimum effort on a user’s end. Recommendations are drawn from the user-owned garments, and not from outside. The method broadly involves two algorithms - preparation of user inventory using clothing detection on user photos and recommendation of outfit from the wardrobe. At a minimum, the user is required to upload his photos, and the rest is taken care of by the algorithm which can yield convincing outfit recommendations based on fashion trends every day. The system further learns from user outfit styles and patterns every day.

# What problem does it solve?
The System addresses the following problems:
- According to The Telegraph, a recent study found that an average person spends almost a year in a lifetime in deciding what to wear.
- Even if the time taken each day is justified, frustrations associated with picking an outfit cannot be ignored.
- According to the chief design officer in California Closets, people repeat 20% of the clothes they own every day while ignoring the rest, therefore wasting the money and space in the closet.
- Given ten items in each category of pants, shirt, jacket, shoes, watch and accessories, the total number of possible combinations turn out to be 1 million which is something humans cannot wrap their minds around. 

# Stage of development
1)	Clothing Categorization

In the first part of the work, we categorize user’s clothes into different categories of clothing items using a classifying 50-layer Residual (ResNet50) pre-trained ImageNet Model. It is computationally expensive to train a network this large from scratch. For that reason, we only train last 12 layers of the pre-trained model, which learn more complex features and patterns, while freezing the parameters associated with remaining layers. The network is trained on Deep Fashion dataset.

2)	Compatibility Training

In the second part of the work, we build a machine learning model that picks the combinations generated from the results in the previous section and outputs a compatibility score. The combinations are then ranked based off scores. Each item in an outfit is passed through a pre-trained Encoder to generate a feature vector. Feature vectors of different items in one outfit are combined to create a matrix representing the outfit. The matrix outfit representation is passed through a simple neural network which gives an output score based on the information learned during the training of the model. If the user rejects the outfit produced by the algorithm, the algorithm is retrained giving the outfit a negative score, thus representing user preferences in the model in the long term. The model is trained on Polyvore dataset and follows the same procedure. 

The next steps involve commercialization of the product into a user-centric application to facilitate the lives of people with an intelligent fashion assistant. The project proposes a futuristic approach to solve the problems with clear implications on the lives of people. Therefore, it has the potential of commercialization to make the lives of people more comfortable.

# Dataset
We used the public Deep Fashion data that has over 161000 images with a domain of 51 categories of clothes in every possible environment. We performed the data cleaning on the same. We also tried to reduce the categories to make it more generalised instead. 
Model – 
The prepared dataset was trained on the inception network implemented with the help of Tensorflow with pretrained weights for object detection. The outcome of network were bounding boxes on images. The bounding boxes around images are cropped and saved in different directories based on their predicted categories.

*The code has not been updated since 2018. Contact me on Github for more info.
