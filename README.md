# Signopedia
## Table of Content
  - [Demo](#demo)
  - [Overview](#overview)
  - [Motivation/Purpose](#motivationpurpose)
  - [Technical Aspect](#technical-aspect)
  - [Data collection](#data-collection)
  - [Installation](#installation) 
  - [Run](#run)

## Demo
<br>
<br>
<img src="demo.gif" width="100%">

<br>
<div display="flex" >

![](https://forthebadge.com/images/badges/made-with-python.svg) <img src="made-with-tkinter.svg">

</div>


## Overview
* **Simple Tkinter app fitted with Deep Convolutional neural network model which is able to distinguish between 43 different types of Traffic signs used worldwide with high accuracy.**<br><br>
* **Data to train this DNN is collected in (`/processed data`) folder, the images are taken from GTSRB - <u><b>German Traffic Sign Recognition Benchmark</b></u> which is a public dataset on Kaggle.**

<br>

## Motivation/Purpose
After completing the Deep learning specialization course. I was super excited to implement the knowledge I gained in practical and productional way by doing an **end to end project** with following purposes.
1. This application/technique can be applied to **motion planning** to make self driving cars.<br>  
2.  Want to give enlightenment to beginners in learning Tkinter as well as to train DNN and hypertune it to get better performance !<br>
3. Want to make more advancement in this project to serve people on the road and help them recognize different signs of which they are not aware about.

## Technical Aspect
#### This project is divided into Four major parts:
1. Organising the images in a clear way and removing low-quality images and outliers from the dataset.
2. Training the model on the images and setting up a benchmark model to improve upon.
3. Fine Tuning the model by improving the architecture and doing hyperparameter search.
4. Building a Tkinter GUI.
   
## Data collection
As we know *data* is building block of Data science!<br>
I had collected the images from a public dataset on Kaggle. You can download it for your project from 
(`/processed data`) folder.<br>
<div class="row">
  <div class="col">
     <img target="_blank" src="https://storage.googleapis.com/kaggle-datasets-images/82373/191501/4f9f4f59d288718705ff67449bbc8e66/dataset-cover.jpg?t=2018-11-25-18-48-30" alt="Cover image" class="sc-cHcdSN hOWCHl">
  </div>
</div>

<br>

## Installation
The Code is written in Python 3.8 in an anaconda environment. For anaconda instalation click <a href="https://www.anaconda.com/products/individual">here</a>.To make new environment in anaconda run following commands in your **Anaconda Prompt**.
```
conda create -n your_env_name python=3.8.x
```

## Run
After successfully creating anaconda environment, install the required packages and libraries by running this command in the project directory after cloning the repository:
```
pip install -r requirements.txt
```
then by running the following command, it will open a dialog box  containing the GUI for using the application.
```
python gui.py
```

## Technologies Used

<img src="https://www.sketchappsources.com/resources/source-image/python-logo.png" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb" alt="Python Logo Sketch freebie - Download free resource for Sketch - Sketch App  Sources" data-noaft="1" style="width: 434px; height: 325.5px; margin: 0px;">
<br><br><br>
<img target="_blank" src="https://blog.keras.io/img/keras-tensorflow-logo.jpg" width=400>
<br><br><br>
<img src="https://camo.githubusercontent.com/d77950366264c0a9b95cbaa3968ff4cd61f4703bae284b482d833c65bd3fd259/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d53657979567162317156302f575a496f694b6a306e63492f41414141414141414175632f6b4a544e615575575a306f3073735f36547a4a41636e4a794b58634d52622d4941434c63424741732f73313630302f475549253242707974686f6e253242546b696e7465722e706e67" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb" alt="GitHub - Mehulagrawal710/Tkinter-desktop-attendance-application: This is an  attendance calculation system developed for e-Time Office machine." data-noaft="1" style="width: 434px; height: 257.952px; margin: 0px;">

