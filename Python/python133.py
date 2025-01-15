class reverse:
    def __init__(self, s):
        self.s = s
    def reverse(self):
        a=self.s[::-1]
        print("reversed string is:",a)
        if a==self.s:
            print("it is palindrome")
        else:
            print("it is not palindrome")

obj=reverse("malayalam")
obj.reverse()