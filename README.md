# Signopedia

## Links to access the app

* http://ec2-43-204-47-110.ap-south-1.compute.amazonaws.com/
* http://43.204.47.110/

<br>

## Table of Content
- [Signopedia](#signopedia)
  - [Links to access the app](#links-to-access-the-app)
  - [Table of Content](#table-of-content)
  - [Demo](#demo)
  - [Samples Gallery](#samples-gallery)
  - [Overview](#overview)
  - [Motivation/Purpose](#motivationpurpose)
  - [Technical Aspect](#technical-aspect)
      - [This project is divided into Four major parts](#this-project-is-divided-into-four-major-parts)
  - [Data collection](#data-collection)
  - [Run](#run)
  - [Technologies Used](#technologies-used)

## Demo

<br>
<br>
<img src="./screenshots/landing_page.jpeg" width="100%">
<br>
<br>
<img src="./screenshots/try_it_now.jpeg" width="100%">
<br>
<br>
<img src="./screenshots/result_page.jpeg" width="100%">

<br>
<div display="flex" >

![](https://forthebadge.com/images/badges/made-with-python.svg) <img src="made-with-next.js.svg">
![](https://forthebadge.com/generator/?plabel=Deployed+on&sbg=%235D9741&slabel=aws+ec2)

</div>

## Samples Gallery

* You can also try some of our own images
  
<br>
<img src="./screenshots/samples_gallery.jpeg" width="100%">



## Overview

* **Simple Web app fitted with Deep Convolutional neural network model which is able to distinguish between 43 different types of Traffic signs used worldwide with high accuracy.**<br><br>
- **Data to train this DNN is collected in (`/processed data`) folder, the images are taken from GTSRB - <u><b>German Traffic Sign Recognition Benchmark</b></u> which is a public dataset on Kaggle.**

<br>

## Motivation/Purpose

After completing the Deep learning specialization course. I was super excited to implement the knowledge I gained in practical and productional way by doing an **end to end project** with following purposes.

1. This application/technique can be applied to **motion planning** to make self driving cars.<br>  
2. Want to give enlightenment to beginners in learning Tkinter as well as to train DNN and hypertune it to get better performance !<br>
3. Want to make more advancement in this project to serve people on the road and help them recognize different signs of which they are not aware about.

## Technical Aspect

#### This project is divided into Four major parts

1. Organising the images in a clear way and removing low-quality images and outliers from the dataset.
2. Training the model on the images and setting up a benchmark model to improve upon.
3. Fine Tuning the model by improving the architecture and doing hyperparameter search.
4. Building a Web application with the help of NextJS and Django.
5. Deployed the Website on AWS EC2 with the help on Nginx,  Docker and Kuberbetes
   
## Data collection

As we know *data* is building block of Data science!<br>
I had collected the images from a public dataset on Kaggle. You can download it for your project from
(`/processed data`) folder.<br>
<div class="row">
  <div class="col">
     <img target="_blank" src="dataset-cover.jpg" alt="Cover image" class="sc-cHcdSN hOWCHl">
  </div>
</div>

<br>

## Run

Go to the following URL to try out our app:


* http://ec2-43-204-47-110.ap-south-1.compute.amazonaws.com/
* http://43.204.47.110/

## Technologies Used
<div style="display:grid,grid-template-column:repeat(2,1fr); grid-gap:1000px">


<img src="https://www.sketchappsources.com/resources/source-image/python-logo.png" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb" alt="Python Logo Sketch freebie - Download free resource for Sketch - Sketch App  Sources" data-noaft="1" style="width: 434px; height: 200px; margin: 0px;">
<img style="padding:20px" target="_blank" src="https://blog.keras.io/img/keras-tensorflow-logo.jpg" width=400>
<img style="padding:20px" target="_blank" src="screenshots\next-JS-framework.png" width=400>
<img style="padding:20px" target="_blank" src="screenshots\DjangoFeaturedImage.jpeg" width=400>
<img style="padding:20px" target="_blank" src="screenshots\aws.avif" width=400>
<img style="padding:20px" target="_blank" src="screenshots\Amazon-EC2.jpg" width=400>
<img style="padding:20px" target="_blank" src="screenshots\Docker.png" width=400>
<img style="padding:20px" target="_blank" src="screenshots\Nginx.jpg" width=400>
<img style="padding:20px" target="_blank" src="https://images.prismic.io/qovery/6f51c703-9e24-49e8-a462-abe2b2c08991_kubernetes.png?ixlib=gatsbyFP&auto=compress%2Cformat&fit=max&q=50" width=400>

</div>

