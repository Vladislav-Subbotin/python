class StringVar:
    value = ''
    def set(self):
        self.value = input()

    def get(self):
        print(self.value)
obj = StringVar()
obj.set()
obj.get()