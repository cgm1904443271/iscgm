class Dog:
    def bark(self):
        print("咬不死你")
        return self   # 方法的连贯调用的基础是返回对象

    def eat(self):
        print("爱吃大骨头")
        return self

    def run(self):
        print("比兔子跑的快")
        return self

dog = Dog()
dog.bark().eat().run()