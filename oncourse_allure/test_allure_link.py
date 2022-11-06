import allure
test_case_link = "https://ceshiren.com/t/topic/14033"

@allure.link("https://blog.csdn.net/gaomingjian218/article/details/121071149")
def test_with_link():
    print("这是csdn链接")

@allure.link('https://qilinhuicloud.com/login?redirect=%2Findex#/login', name='华隆科技')
def test_with_named_link():
    pass

@allure.issue('bug编号', 'https://ceshiren.com/t/topic/3386')
def test_with_issue_link():
    pass


@allure.testcase(test_case_link, 'Test case title：num1')
def test_with_testcase_link():
    pass