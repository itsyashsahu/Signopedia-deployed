import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras


def load_images_with_labels(train_image_path:str,train_label_path:str,test_images_path:str):
    
    train_images=np.load(train_image_path)
    train_labels=np.load(train_label_path)
    test_images=np.load(test_images_path)
    
    return train_images, train_labels, test_images


def split_train(train_images_full,train_labels,validation_size:int=0.2,random_state=None):
    
    return train_test_split(train_images_full,train_labels,test_size=validation_size,random_state=random_state)

def make_model_functional()->keras.models.Model:
    
    inputs=keras.layers.Input(shape=[30,30,3])
    x=keras.layers.Conv2D(filters=32,kernel_size=(5,5),activation="relu",kernel_initializer="he_normal")(inputs)
    x=keras.layers.Conv2D(filters=32,kernel_size=(5,5),activation="relu",kernel_initializer="he_normal")(x)
    x=keras.layers.MaxPool2D(pool_size=(2,2))(x)
    x=keras.layers.Dropout(rate=0.25)(x)
    x=keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu",kernel_initializer="he_normal")(x)
    x=keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu",kernel_initializer="he_normal")(x)
    x=keras.layers.MaxPool2D(pool_size=(2,2))(x)
    x=keras.layers.Dropout(rate=0.25)(x)
    x=keras.layers.Flatten()(x)
    x=keras.layers.Dense(units=256,activation="relu",kernel_initializer="he_normal")(x)
    x=keras.layers.Dropout(rate=0.5)(x)
    outputs=keras.layers.Dense(units=43,activation="softmax")(x)
    
    model=keras.models.Model(inputs=[inputs],outputs=[outputs])
    
    return model

def make_model_sequential()->keras.models.Model:
    
    model=keras.models.Sequential([
        keras.layers.Conv2D(filters=32,kernel_size=(5,5),activation="relu",input_shape=[30,30,3]),
        keras.layers.Conv2D(filters=32,kernel_size=(5,5),activation="relu"),
        keras.layers.MaxPool2D(pool_size=(2,2)),
        keras.layers.Dropout(rate=0.25),
        keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu"),
        keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu"),
        keras.layers.MaxPool2D(pool_size=(2,2)),
        keras.layers.Dropout(rate=0.25),
        keras.layers.Flatten(),
        keras.layers.Dense(units=256,activation="relu"),
        keras.layers.Dropout(rate=0.5),
        keras.layers.Dense(units=43,activation="softmax")
    ])
    
    return model

def final_model():
    
    model=keras.models.Sequential([
        keras.layers.Input(shape=[30,30,3]),
        keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation="relu",padding="same"),
        keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation="relu",padding="same"),
        keras.layers.MaxPool2D(pool_size=(2,2)),
        keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu",padding="same"),
        keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu",padding="same"),
        keras.layers.MaxPool2D(pool_size=(2,2)),
        keras.layers.Conv2D(filters=128,kernel_size=(3,3),activation="relu",padding="same"),
        keras.layers.Conv2D(filters=128,kernel_size=(3,3),activation="relu",padding="same"),
        keras.layers.MaxPool2D(pool_size=(2,2)),
        keras.layers.Flatten(),
        keras.layers.Dense(units=256,activation="relu",kernel_initializer="he_normal"),
        keras.layers.Dense(units=256,activation="relu",kernel_initializer="he_normal"),
        keras.layers.Dropout(rate=0.3),
        keras.layers.Dense(units=43,activation="softmax")
    ])
    
    return model

    