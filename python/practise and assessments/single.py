class company:
    __moto="moto: strive for excellence"
    _aim=" aim: to be at the top"
    profit=" profit: 200%"
    @classmethod
    def c_class(cls):
        cls.profit="profit: 100%"
        cls.c_stat()
        # cls.c_display()

    @staticmethod
    def c_stat():
        print("about the company")
        print("common privilages")

    def c_display(self):
        print(self)
        print(self._aim)
        print(self.__class__.__moto)
        print(self.profit)
        self.c_class()
        print (self.profit)


class employee(company):
    __emp_name="xxxx"
    __emp_id=1212121
    _emp_level=12

    @staticmethod
    def e_stat():
        print("common employee privilages")

    def e_display(self):
        print(self)
        company.c_display(self)
        print ("employee details")
        self.e_stat()
        print("level: ",self._emp_level)
        print("id: ",self.__emp_id)
        print("name: ",self.__emp_name)

a=employee()
a.e_display()
