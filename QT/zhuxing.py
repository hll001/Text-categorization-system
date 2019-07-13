
# 关于生成柱形图的测试文件

import matplotlib.pyplot as plt

name_list = ['IT','Motion','Healthy','Military','Recruit','Education','Culture','Tourism','Car','Finance']
num_list = [0.01757630832943132, 0.001984890734110339, 0.012663621520055814, 0.003497250461047665, 0.030737691222397664, 0.026634191397701394, 0.010933284505104056, 0.8560780687377516, 0.004799839739453212, 0.03509485335294704]
plt.barh(range(len(num_list)), num_list, tick_label=name_list)
print(name_list)
plt.savefig("1.png",dpi=80)
# plt.show()
# plt.close()