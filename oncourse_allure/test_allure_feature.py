import allure

def test_feature():
    print("这是一个大模块")
@allure.feature("看看登录功能")
def test_log():
    print("测试登录")

@allure.story("登录失败")
def test_logfail():
    print("测试登录失败")

@allure.step("第一步输入用户名")
def test_write_usr():
    print("001输入usr")

@allure.step("第二步输入密码")
def test_write_prd():
    print("002输入密码")

@allure.story("登录成功01")
def test_logsucc():
    print("测试登录成功")
    assert 1 ==2