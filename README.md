# Official Implementation of: Handwritten Mathematical Expression Recognition Using Multi-Scale Features and Attention-Based Model

This repository contains the official implementation of the paper "Handwritten Mathematical Expression Recognition Using Multi-Scale Features and Attention-Based Model." The code is designed for training and testing a model on the CROHME datasets.

## How to Run the Training Script

1. **Setup Environment**:
   Ensure you have all the required dependencies installed. Use the following command to install them:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**:
   Download the training and testing data from here https://drive.google.com/drive/folders/1vXQnSSKvQGPCXIp99aD0sSFLnsEWXOzn?usp=sharing
   Ensure the dataset is placed in the `data/` directory 

3. **Run Training**:
   Note that we train our model on one train set CROHME 2014 and test the model on three test sets CROHME 2014, CROHME 2016, and CROHME2019. Commands for training and testing the model with single decoder branch or two decoder branches respectively are as follows:

```bash
# for training on CROHME 2014  with one L2R branch (baseline model)
sh train.sh -L2R

# for training on CROHME 2014  with two branches (L2R and R2L) (our model, ABM)
sh train.sh -L2R-R2L


# for testing on CROHME 2014, 2016, 2019 with L2R branch
sh test.sh -2014  L2R


# for testing on CROHME 2014, 2016, 2019 with R2L branch
sh test.sh -2014  R2L

```

## How to Run the Testing Script

1. **Ensure Pretrained Model Availability**:
   - Download the pretrained model weights ([if available](https://drive.google.com/drive/folders/1vXQnSSKvQGPCXIp99aD0sSFLnsEWXOzn?usp=sharing)) and add the path to the test.sh file.

2. **Run Testing**:
   Use the following command to evaluate the model:
   ```bash
   test.sh 2014 L2R
   ```
3. **Results**:
   - The results, including recognition accuracy and detailed metrics, will be saved in the `results/` directory.
   - For visual evaluation, recognized mathematical expressions and ground truths will be logged in the `results/logs/` folder.

