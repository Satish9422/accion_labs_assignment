class DigitTransformation:
  def transform(x):
   if not (0<=x<=9):
    raise ValueError("Enter Single digit value")
   return(sum(int(str(x)*i) for i in range(1, 5)))
print(DigitTransformation.transform(3))
