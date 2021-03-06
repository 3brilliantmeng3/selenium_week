import  unittest
if __name__ == '__main__':
    # 默认的测试用例加载器,用于需找符合一定规则的测试用例
    # discover 发现
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    # unittest.defaultTestLoader.discover(start_dir, pattern='test*.py')
    # 执行suite中的所有测试用例
    # TextTestRunner 文本用例运行器
    # 首字母大写,说明TextTestRunner 是一个类,类不能直接调用方法,必须要实例化对象才能调用
    # python中实例化不需要new关键字,直接在类后面加一对小括号就可以了
    unittest.TextTestRunner().run(suite)