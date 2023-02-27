<h1 align="center">
  Hand Sign Detection
</h1>
<p align="center">A Prove of Concept using computer vision that show the alphabet letters of sign language.</p>

# Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
</br>
</br>

## Prerequisites

After cloning this repository, you will need install the Anaconda. <a target="blanck" href="https://docs.anaconda.com/anaconda/install/index.html">Click here</a> and follow the documentaion.
</br>
</br>

## Installing

- Open a terminal window and type the following commands.

1. Create a environment in anaconda.

```
conda create -n hand-sign-detection
```

2. Activate the environment created in anaconda.

```
conda activate hand-sign-detection
```

3. Install tensorflow.

```
conda install -c conda-forge tensorflow
```

4. Install opencv.

```
conda install -c conda-forge opencv
```

5. Install the requirements.

```
pip install -r requirements.txt
```

# Usage

## Train the Model

Inside the folder "data" has the data that was used to train the model, there you will see a folder by letter.

</br>

### To capture more data follow this steps

1. Type the follow command on terminal.

```
python data_collection.py
```

2. To capture the image type <b>"s"</b>

3. Train the model with the new classes and data on this plataform <a href="https://teachablemachine.withgoogle.com/train/image">Teachable Machine</a>

4. Download the model and past here on the folder "Model"

</br>

## Initialize

To initialize the application you need type the follow comand on terminal on the project root, inside the environment created in anaconda

```
python index.py
```
