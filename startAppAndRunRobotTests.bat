pip install -r requirements.txt
start python swapiDevApplication.py &
timeout /t 5
cd robotTestSuite
robot testsuite.robot
pause
echo "Press any key to terminate server"
taskkill /IM python.exe