# Official Implementation of: Handwritten Mathematical Expression Recognition Using Multi-Scale Features and Attention-Based Model

This repository contains the official implementation of the paper "Handwritten Mathematical Expression Recognition Using Multi-Scale Features and Attention-Based Model." The code is designed for training and testing a model on the CROHME datasets.

## How to Run the Training Script

1. **Setup Environment**:
   Ensure you have all the required dependencies installed. Use the following command to install them:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**:
   Ensure the dataset is placed in the `data/` directory and preprocessed appropriately as described in the `README.md` of the `data/` folder.

3. **Run Training**:
   Use the command below to start training:
   ```bash
   python train.py --config configs/train_config.yaml
   ```

   - Replace `configs/train_config.yaml` with the path to your configuration file if it is located elsewhere.
   - Key hyperparameters such as learning rate, batch size, and model architecture can be adjusted in the configuration file.

4. **Monitor Training**:
   Training logs, including loss and accuracy metrics, will be saved to the `logs/` directory. Use TensorBoard to visualize the training process:
   ```bash
   tensorboard --logdir logs/
   ```

## How to Run the Testing Script

1. **Ensure Pretrained Model Availability**:
   - Download the pretrained model weights (if available) and place them in the `weights/` directory.
   - Alternatively, use the model checkpoint from your training process.

2. **Run Testing**:
   Use the following command to evaluate the model:
   ```bash
   python test.py --config configs/test_config.yaml --weights weights/model_checkpoint.pth
   ```

   - Replace `configs/test_config.yaml` with the appropriate testing configuration file.
   - Replace `weights/model_checkpoint.pth` with the path to your trained model weights.

3. **Results**:
   - The results, including recognition accuracy and detailed metrics, will be saved in the `results/` directory.
   - For visual evaluation, recognized mathematical expressions and ground truths will be logged in the `results/logs/` folder.

## Additional Notes

- For more information about configuration file settings, refer to the `configs/` directory.
- Ensure the proper CUDA environment is set up for training and testing on GPU.
- Contributions and issues are welcome. Please submit them through the GitHub issue tracker.
