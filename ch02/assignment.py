x=5  #指定x變數值為常值5
y=x  #指定y變數值為x變數的值
print(id(x),id(y))  #顯示變數x,y的記憶體位置
x=3+y  #指定x變數值為常值3+y的結果 y變數值為常值3
print(id(x))
a,b=2,3  
print(id(a),id(b))
a,b=b,a  #交換a,b變數值交換
print(id(a),id(b))