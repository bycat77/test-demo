import allure
def test_attach():
    print("这是个附件")

@allure.step("第一步输入用户名")
def test_write_usr():
    print("001输入usr")

@allure.step("第二步输入密码")
def test_write_prd():
    print("002输入密码")
    allure.attach.file("/Users/sam/Desktop/素材/素材02.png",
                        name ="附件图",
    attachment_type=allure.attachment_type.PNG,
                       extension=".PNG")
