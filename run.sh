#### -- Print Header -- ####
printf "\E[H\E[2J"
echo "\x1b[1mLaunching Linear Regression...\x1B[0m"
echo

#### -- Cleanup -- ####
if [ -e Theta.csv ]
then
	echo "Deleting old model..."
    rm Theta.csv
	echo
fi

#### -- Train -- ####
echo "Training model..."
python3 train.py -v
echo "Model saved to Theta.csv"
echo

#### -- Predict -- ####
echo "Predict..."
python3 predict.py
echo

#### -- Cleanup -- ####
# rm Theta.csv
