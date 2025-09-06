a = 10 # 변수
PI = 3.141592 # 상수
def randint(x): # 함수
  return 3 * x + 6
class Calculator: # 클래스
  def __init__(self, first, second): 
    self.first = first
    self.second = second
  def add(self): # 메서드
    self.result = self.first + self.second
  def div(self):
    self.result = self.first / self.second

b = Calculator(3, 5) # 객체