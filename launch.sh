#!/bin/bash
GREEN='\033[0;32m'
NC='\033[0m'

# if [[ "$VIRTUAL_ENV" != "" ]]; then 
#     echo "You are in a working virtualenv $VIRTUAL_ENV";
# fi

# echo -e "${GREEN}Installing packages from requirements.txt${NC}" 
# pip3 install -r flaskapp/requirements.txt

# echo -e "${GREEN}Installing spacy en model${NC}" 
# python -m spacy download en

# echo -e "${GREEN}Downloading required sentence embeddings${NC}" 
# gdown https://drive.google.com/uc?id=1l2liCZqWX3EfYpzv9OmVatJAEISPFihW
# unzip para-nmt-50m-demo.zip
# mv para-nmt-50m-demo data
# rm para-nmt-50m-demo.zip

echo -e "${GREEN}Downloading model checkpoint${NC}" 
gdown https://drive.google.com/uc?id=18uOQsosF4uVGvUgp6pB4BKrQZ1FktlmM
tar -xzf train-20180325-001253.tar.gz
mv train-20180325-001253 data
rm train-20180325-001253.tar.gz
