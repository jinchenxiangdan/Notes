class MyPrint:

    def __init__(self):
        super().__init__()

    def my_print(self,s):
        print(s,end='')
    
    def my_println(self, s):
        print(s)

def test_my_print(s):
    print('test: ', s)