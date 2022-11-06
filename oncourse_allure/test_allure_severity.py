import allure
def test_logfail_severity():
    print("测试用例严重级别")

@allure.severity(allure.severity_level.BLOCKER)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass
