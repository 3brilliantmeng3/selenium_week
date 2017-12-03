
class LoginPage:
    # 构造方法的作用
    # 实例化LoginPage对象的时候,需要把driver作为参数传进来
    # 便于别的属性和方法使用driver
    def __init__(self,driver):
        self.driver = driver
        # 构造方法里面定义变化的内容

    title ="用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"
    from selenium.webdriver.common.by import By
        # 小括号表示元组,第一类元素是控件的定位方式
        # 第二个元素,控件定位方式的具体值
    username_input_loc =(By.ID,"username")
    password_input_loc =(By.ID,"password")
    login_button_loc =(By.CSS_SELECTOR,"body > div.login_main.w1180.clearfix > div.login.fr > form > ul > li:nth-child(5) > input")


    def open (self):
        self.driver.get(self.url)
    def input_username(self,username):
        # self.driver.find_element_by_id("username").send_keys(username)
        #self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
        # *号的作用,把一个元组中的元素分别传入方法参数中
        # 前面加一个*号,表示传入的就不是元组,而是元组中的2个元素

    def input_password(self,password):
        # self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def  click_login_button(self):
        self.driver.find_element( *self.login_button_loc).click()

