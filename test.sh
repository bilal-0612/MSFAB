#!/bin/bash

# Set the CUDA device
export CUDA_VISIBLE_DEVICES=0

# Define the model path
path='model.pkl'

# Get dataset and branch as arguments
dataset=$1
branch=$2

# Ensure both arguments are provided
if [ -z "$dataset" ] || [ -z "$branch" ]; then
    echo "Usage: $0 <dataset> <branch>"
    exit 1
fi

# Determine the decoder index based on the branch
if [ "$branch" == "L2R" ]; then                  
    idx_decoder=1
elif [ "$branch" == "R2L" ]; then
    idx_decoder=2
else
    echo "Error: Invalid branch. Use 'L2R' or 'R2L'."
    exit 1
fi

# Echo the decoder index
echo "Decoder Index: $idx_decoder"

# Iterate over the dataset and run the test script
for year in $dataset; do
    python test.py \
        -k 10 \
        -model_path "$path" \
        -dictionary_target "dictionary.txt" \
        -test_dataset "data/offline-${dataset}-test.pkl" \
        -label "data/test-caption-${dataset}.txt" \
        -saveto "result/${dataset}-branch_${branch}.txt" \
        -output "result/test_${dataset}-branch_${branch}.wer" \
        -idx_decoder $idx_decoder \
        -year $dataset
done
