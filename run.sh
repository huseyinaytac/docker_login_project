export Browser=firefox
behave -f allure_behave.formatter:AllureFormatter -o target/allure-results -D browser=$Browser
allure serve target/allure-results
#python Utility/generate_allure_report.py

