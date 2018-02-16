# I-FeatExt-Vienneau

## Michael Vienneau

## Goals
I wanted to use the accelerometer from my phone -- and actually get something useful that was not buggy. I decided I would control a 'game' with my phone, tilting in different directions to control where the ball moved on the screen.

## Tools/Libraries
I used python-osc, processing, wekinator and TouchOSC. TouchOSC for the input, python for the feature extraction, wekinator for training, and processing for the output

## Accomplishments
I was able to do everything I set out in my goals. For feature extraction -- I removed unnessary data given my TouchOSC (about 6 featuers), and then smoothed the x,y,z accelerometer data using a simple average over the last 10 or so seen. This made for very smooth movement in the game, and allowed for less jittery bugs. 

## ML Stuff
I used knn for the algorithm, as I only had 3 features and they were all very geometrically different. With k = 3 to further smooth any results I was given. 
