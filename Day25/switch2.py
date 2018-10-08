class switch_case(object):

    def case_to_function(self, case):
        fun_name = "case_fun_" + str(case)
        method = getattr(self, fun_name, self.case_fun_other)
        return method

    def case_fun_1(self, msg):
        print(msg)

    def case_fun_2(self, msg):
        print(msg)

    def case_fun_other(self, msg):
        print(msg)


if __name__ == "__main__":
    cls = switch_case()
    cls.case_to_function(1)("case_fun_1")
    cls.case_to_function(2)("case_fun_2")
    cls.case_to_function(3)("case_fun_not_found")
