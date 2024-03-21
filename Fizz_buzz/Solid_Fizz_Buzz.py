#SOLID 

class Rule:
    def applies(self, number):
        raise NotImplementedError
    
    def action(self):
        raise NotImplementedError
    
class FizzRule(Rule):
    def applies(self,number):
        return number % 3 == 0 
    
    def action(self): 
        return "Fizz" 
    

class BuzzRule(Rule):
    def applies(self, number):
        return number % 5 == 0
    
    def action(self):
        return "Buzz"
    
class FizzBuzzRule(Rule):
    def applies(self, number):
        return number % 3 == 0 and number % 5 == 0
    
    def action(self):
        return "FizzBuzz"
    

class NumberRule(Rule):
    def __init__(self, number):
        self.number = number 

    def applies(self, number):
        return self.number == number
    
def action(self):
        return str(self.number)


class FizzBuzzGame:
    def __init__(self, rules):
        self.rules = rules

    def play(self, number):
        result = ''
        for rule in self.rules:
            if rule.applies(number):
                result += rule.action()
        return result or str(number)

    def print_result(self, start, end):
        for num in range(start, end + 1):
            print(self.play(num))



if __name__ == "__main__":
    rules = [FizzBuzzRule(), FizzRule(), BuzzRule()]
    game = FizzBuzzGame(rules)
    game.print_result(1, 30)
#end of code
