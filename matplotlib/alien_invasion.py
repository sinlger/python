import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
input_value = [1,2,3,4,5]
plt.plot(input_value ,squares,lineWidth=5)
plt.title('Test',fontsize=20)
plt.xlabel('Value',fontsize=10)
plt.ylabel('Squares',fontsize=10)
# plt.tick_params(axis='both',labelsize=14)
plt.show()