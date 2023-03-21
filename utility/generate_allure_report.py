import os
def generate_allure_report():
    """Bu yöntem, allure-behave sonuçlarından allure-behave raporu oluşturur"""
    os.chdir(os.path.abspath(__file__+"/../../"))
    os.popen(r'allure generate target/allure-results -o target/allure_report --clean').read()


generate_allure_report()