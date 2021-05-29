### EXTENSIVE VISION AI PROGRAM 

Name :  Raajesh Laguduva Rameshbabu

Batch Number :  W6

Registered email address : raajesh.lr2@gmail.com

------------



![My Image](https://avatars1.githubusercontent.com/u/37265950?s=400&u=08820314a828b6b340c21ece5619dadd4d848b4e&v=4)

------

#### SESSION 4 - **Architectural Basics**

#### TOPICS IN ORDER AND THE THOUGHT BEHIND IT

##### 1. IMAGE NORMALIZATION 

On starting the program, we will be first normalizing the image.

For this MNIST Dataset : We have grayscale image and we have pixel values ranges from 0 to 255 and we have divided each pixel values by 255 and so it gets normalized and comes in the range 0 to 1.

We are giving equal importance to all the pixels, so the kernels would be able to extract well when it convolutes.

-------

##### 2. RECEPTIVE FIELD

For MNIST Dataset, I have the thought process of arriving at the receptive field of 24x24 as its enough to see the entire object. It is the one which the kernels extracting(seeing) when we convolute.

We have to probably have a look at our dataset and see how many layers we have to go ahead to reach the receptive field.

-----

##### 3. HOW MANY LAYERS

For reaching the target receptive field of 24x24, I have accordingly constructed my architecture with the required number of layers.

We will be using 3x3 kernel (there is a reduction of n-2 and n-2 in length and width and the receptive field of 3x3 at start and increases by n+2 n+2 on addition) in the layers.

We will be using 1x1 kernel (there is no reduction in resolution and also there in no increment in receptive field, just to reduce the number of channels).

Max pooling (Only one max pooling we have used and the resolution halves and the receptive field doubles).

-------

##### 4. 3x3 Convolutions

We have been using 3x3 Convolutions where each 9pixels in kernel have an element wise multiplication and it has always local receptive field of 3x3 and the global receptive field gradually increases on addition. 

We use it to increase the number of channels in the Convolution block. 

We usually increase the channels gradually using 3x3 kernels and it is effective. 

We can reach any global receptive field on increasing the count of kernels.

-------

##### 5. 1x1 Convoltions

We have been using 1x1 convolutions where it combines the features and it creates magic. 

we use it to decrease the channels unless we have a proper reason to increase it. 

We have been using it together with Max pooling in Transition block.

-------

##### 6. CONCEPT OF TRANSITION LAYERS

We usually call this transition layer in between convolution layers.

-  We have one Maxpooling which halves the image resolution.
- We have 1x1 (Bottleneck) which usually combines the features from different channels and creates magic.	

------

##### 7. POSITION OF TRANSITION LAYERS

Images go this way.

- One convolution outside, then
- Convolution block, then
- Transition block, then

-------

##### 8. Max Pooling

Max pooling usually takes 4 pixels (pool size = 2,2) and results the maximum value.

So it decreases the image resolution by half.

------

##### 9. POSITION OF MAX POOLING

We have to do max pooling only after 2-3 convolutions in the beginning stage as we should not corrupt the image just by doing maxpooling in the initial stages. 

Also its better to avoid Maxpooling at the final layers as we will be loosing many spatial information. Maxpooling will take care of the invariances in the image, we usually do it in the Transition layer.

-----

##### 10. The distance of MaxPooling from Prediction,

We have to maintain a distance of 2-3 convolutions before the last layer for doing max pooling. 

Model do starts backpropagation from the last layer output and it needs all the information about the image.

-------

##### 11. Kernels and how do we decide the number of kernels?

Kernels - The number of kernels we use is proportional to the number of channels we get in the next layer, It is the feature extractor.

Number of kernels - It depends on how hard the dataset is - how many categories are there (more the categories more the kernels is preferred), if there is also the difference between the images, more the kernels is preferred.

Also depends on the GPU constraint.

------

##### 12. Softmax

We will be using softmax at the end which will bring the sum of values equals to 1. 

It is not the probability and it is probability like. 

So we have to very careful while we are dealing with medical datasets.

------

##### 13. Number of Epochs and when to increase them

There is no specific number of epochs we should use and we usually increase it when we see there is a sign of accuracies improving. 

If we use LR Schedular, number of epochs matters as it schedules the values based on the number of epochs.

Just increasing the number of epochs will not be useful if our architecture is not good.

------

## PROBLEMS WE HAVE TO LOOK

-------

##### 14. How do we know our network is not going well, comparatively, very early

Once a network does not starts well, it wont ends well.

So we have to look our network and see the values in validation accuracy and compare with the best network and we have to change architecture or introduce other features if the accuracies are not good.

------

##### 15. When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

-  When we reach required receptive field - it will be around 24x24 for MNIST dataset. In our case we use large kernel 7x7 at the end to convolute.
- We usually add padding at the last layers and we will maintain the size, but we also do convolutions. We use Global average pooling and bring the size to 1*1 *(no of channels)

------

##### 16. When to add validation checks

We have to add validation checks at every epochs so to track the accuracies else it is very difficult to see the end. 

Usually we add it in the fit method.

------

##### 17. Batch Size, and effects of batch size

- Usually bigger the batch size better the performance considering there is no gpu constraint. 
- Training time is inversely proportional to the batch sizes.
- It is a good practice to maintain the batch size more than the number of classes in the dataset.

------

## TO IMPROVE ACCURACY

--------

##### 18. Batch Normalization

It will bring the pixel values between -1 to +1 and it can/may be applied both before and after the convolutions.

If we do batch normalization, kernels will be able to see the better receptive field.

--------

##### 19. The distance of Batch Normalization from Prediction,

We usually not apply "Relu" at the last layer as it blocks the negative values.

If we apply Batch Normalization, it will bring the values from -1 to +1.

So it is recommended to apply Batch Normalization before 1x1 kernel which we usually do to bring the image to 10 pixel values.

------

##### 20. DropOut

- It is a regularizer for our model when there is overfitting.
- It has be used when we don't have image augmentation.
- It usually makes the kernels values as 0 depends on the dropout percentage we have given.
- We should never use dropout at the end as it will make very very hard for the model when it trains.
- Dropouts wont be effective when we use the model to predict.

-------

##### 21. When do we introduce DropOut, or when do we know we have some overfitting

- we introduce dropout when we have large number of kernels and that is not required.
- Overfitting is when our model mugged up all the training images and its performing well but its failing on validation dataset, hence we introduce dropout which makes the kernel values as 0.

----------

##### 22. Learning Rate

It is the parameter which is used on the optimizer. 

new theta = theta - (alpha)(derived weights - theta)

alpha is the learning rate parameter. It helps us to take out from the local minima where our model usually gets stuck. 

It is speed our model is learning.

smaller the learning rate larger the time takes to converge.

Larger the learning rate - it converges faster and sometimes it may fail to reach minima as it oscillates.

-----------

##### 23. LR schedule and concept behind it

It will schedule the values for every epoch.

If we have given the start value as 0.003, it will just schedules the values no matter whether the accuracies are increasing/decreasing/saturated. It is meaningless. So we usually prefer CLR which swifts between the intervals of LRPlateau which changes the learning rate when saturates.

---------------

##### 24. Adam vs SGD

stochastic gradient descent usually takes one image at a time and iterates the weight.

Adam optimizer actually takes the batch size number of images and to that much number of forward propagation and do one back propagation. 

---------------

