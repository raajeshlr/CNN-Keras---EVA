### EXTENSIVE VISION AI PROGRAM 

Name :  Raajesh Laguduva Rameshbabu

Batch Number :  W6

Registered email address : raajesh.lr2@gmail.com

------------



![My Image](https://avatars1.githubusercontent.com/u/37265950?s=400&u=08820314a828b6b340c21ece5619dadd4d848b4e&v=4)

------

#### ASSIGNMENT 1B

#### TOPICS AND EXPLANATIONS	

##### 1. What are Channels and Kernels (according to EVA)?

###### Channels (SIMILAR_FEATURE_BAGS)

Once kernels/filters are convoluted over an input image, the features of the image (Patterns, Objects, Edges, Backgrounds, Gradients, etc..) are bagged together respectively and so it forms called the channels. Suppose if we consider an RBG Image, it will be having three values at each pixel (lets say R = 0.11, B = 0.65, G = 0.33), and so we have three channels (R,B,G) for that image.

###### Kernels/Filters (FEATURE_EXTRACTOR)

Kernels are assigned with random numbers initially and it convolves over an input image and transforms the image to the newly encoded pixel. The number of kernels we are using to convolve (Should have the same number of channels as input image), corresponds to the number of output (Channels). So this gives us understanding that kernels are helping to increase/decrease the channels. It is fully mathematical where each pixel values in the filter will have an element-wise multiplication and produces a result. Usually the size of an image will be reduced by (n-2)*(n-2) after passing through 3x3 filters.

----------------------

##### 2. Why should we only (well mostly) use 3x3 Kernels?

Point 1 : Consider we have an input image of size 7x7, it can be convoluted in two ways (well many ways).

- If we use 7*7 kernel and convolute, it will give you the result 1x1 and it will take 49 parameters to do it.
- If we use 3*3 kernel thrice (Input size 7x7 to 5x5 to 3x3 to 1x1), it will give you the same result 1x1 but it will take only 27 parameters to do it, So the world prefers 3x3. **"TO DECREASE THE PARAMETERS !"**

Point 2 : It seems architectures like VGG uses only 3x3 kernels and its good for adapting to a wide variety of problems.

Point 3 : It is easy for the models to compute when we use 3x3 rather than other kernels sizes, as explained in EVA.

----------------

##### 3. How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199 (show calculations) 

It takes 99 times to convolve 199x199 to 1x1 in 3x3 convolution operation.

Calculations :

199x199 --> (3x3) --> 197x197 --> (3x3) --> 195x195 --> (3x3) --> 193x193 --> (3x3) --> 191x191 --> (3x3) --> 189x189 --> (3x3) --> 187x187 --> (3x3) --> 185x185 --> (3x3) --> 183x183 --> (3x3) --> 181x181 --> (3x3) --> 179x179 --> (3x3) --> 177x177 --> (3x3) --> 175x175 --> (3x3) --> 173x173 --> (3x3) --> 171x171 --> (3x3) --> 169x169 --> (3x3) --> 167x167 --> (3x3) --> 165x165 --> (3x3) --> 163x163 --> (3x3) --> 161x161 --> (3x3) --> 159x159 --> (3x3) --> 157x157 --> (3x3) --> 155x155 --> (3x3) --> 153x153 --> (3x3) --> 151x151 --> (3x3) --> 149x149 --> (3x3) --> 147x147 --> (3x3) --> 145x145 --> (3x3) --> 143x143 --> (3x3) --> 141x141 --> (3x3) --> 139x139 --> (3x3) --> 137x137 --> (3x3) --> 135x135 --> (3x3) --> 133x133 --> (3x3) --> 131x131 --> (3x3) --> 129x129 --> (3x3) --> 127x127 --> (3x3) --> 125x125 --> (3x3) --> 123x123 --> (3x3) --> 121x121 --> (3x3) --> 119x119 --> (3x3) --> 117x117 --> (3x3) --> 115x115 --> (3x3) --> 113x113 --> (3x3) --> 111x111 --> (3x3) --> 109x109 --> (3x3) --> 107x107 --> (3x3) --> 105x105 --> (3x3) --> 103x103 --> (3x3) --> 101x101 --> (3x3) --> 99x99 --> (3x3) --> 97x97 --> (3x3) --> 95x95 --> (3x3) --> 93x93 --> (3x3) --> 91x91 --> (3x3) -->                   89x89 --> (3x3) --> 87x87 --> (3x3) --> 85x85 --> (3x3) --> 83x83 --> (3x3) --> 81x81 --> (3x3) -->                         79x79 --> (3x3) --> 77x77 --> (3x3) --> 75x75 --> (3x3) --> 73x73 --> (3x3) --> 71x71 --> (3x3) -->                    69x69 --> (3x3) --> 67x67 --> (3x3) --> 65x65 --> (3x3) --> 63x63 --> (3x3) --> 61x61 --> (3x3) -->                            59x59 --> (3x3) --> 57x57 --> (3x3) --> 55x55 --> (3x3) --> 53x53 --> (3x3) --> 51x51 --> (3x3) -->                           49x49 --> (3x3) --> 47x47 --> (3x3) --> 45x45 --> (3x3) --> 43x43 --> (3x3) --> 41x41 --> (3x3) -->                       39x39 --> (3x3) --> 37x37 --> (3x3) --> 35x35 --> (3x3) --> 33x33 --> (3x3) --> 31x31 --> (3x3) -->                              29x29 --> (3x3) --> 27x27 --> (3x3) --> 25x25 --> (3x3) --> 23x23 --> (3x3) --> 21x21 --> (3x3) -->                            19x19 --> (3x3) --> 17x17 --> (3x3) --> 15x15 --> (3x3) --> 13x13 --> (3x3) --> 11x11 --> (3x3) -->                                9x9 --> (3x3) --> 7x7 --> (3x3) -->                                                                                                                                        5x5 --> (3x3) -->3x3 --> (3x3) -->                                                                                                                                                                                 1x1

---------------

