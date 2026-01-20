import numpy as np

arr = np.array([[1, 5, 3, 2], [1 / 5, 1, 2, 1 / 3], [1 / 3, 1 / 2, 1, 2], [1 / 2, 3, 1 / 2, 1]])
print(arr)
n = arr.shape[0]
elv_vals, elg_vecs = np.linalg.eig(arr)
max_val = max(elv_vals)
CI = (max_val - n) / (n - 1)
RI_dic = [0, 0.0001, 0.52, 0.89, 1.11, 1.23, 1.32, 1.41, 1.45, 1.49]

CR = CI / RI_dic[n - 1]
if CR < 0.1:
    print("一致性检验通过")
else:
    print("一致性检验未通过")
print("一致性检验数值为：", CR)

arr_produced = np.prod(arr, axis=1)
arr_root = np.power(arr_produced, 1 / n)
weight = arr_root / arr_root.sum()
print(weight)

arr_guiyi = arr / arr.sum(axis=0)
score = np.dot(arr_guiyi, weight)
print("各方案得分为：", score)
best_index = np.argmax(score)
print(f"最佳方案为第{best_index + 1}个方案，得分为{score[best_index]}")

# topsis法
