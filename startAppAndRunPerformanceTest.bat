pip install -r requirements.txt
start python swapiDevApplication.py &
timeout /t 5
cd performanceSuite/jmeter/bin
call jmeter -n -t "../../perfTest.jmx" -l "../../output.jtl"
cd ../lib/ext
java -jar CMDRunner.jar --tool Reporter --generate-csv "../../../aggregateReport.csv" --input-jtl "../../../output.jtl" --plugin-type AggregateReport
cd ../../../
timeout /t 5
python -u performanceTestSuite.py
pause
echo "Press any key to terminate server"
taskkill /IM python.exe