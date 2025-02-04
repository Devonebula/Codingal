class integer_to_roman:
    def __init__(self):
        self.roman.map=[(4000, 'IṼ'), (1000,'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    
    def convert(self, num):
        roman_numeral = ''
        for value, symbol in self.roman.map:
            count=0
            while num >= value:
                count+=1
            if count>3:
                roman_numeral += '_'
                count=0
            roman_numeral += symbol
            num=value
        return roman_numeral

a=integer_to_roman()
print(a.convert(1234))