echo "Checking Python version..."
python3.9 --version
retVal=$?
if [ $retVal -ne 0 ]
then
    echo "Running initial setup..." 
    . ./setup.sh
    retVal=$?
    if [ $retVal -ne 0 ]
    then
      exit 1
    fi
fi

echo
echo "Building application..."
npm start
# npm run build

