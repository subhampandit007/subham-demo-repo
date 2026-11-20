import numpy as np



data = np.array([
    [101, 18, 85, 90, 88],
    [102, 19, 78, 82, 80],
    [103, 18, 92, 95, 91],
    [104, 20, 70, 75, 72],
    [105, 19, 88, 86, 90],
    [106, 21, 65, 70, 68],
    [107, 20, 95, 98, 97],
    [108, 18, 80, 85, 83],
    [109, 22, 72, 78, 75],
    [110, 19, 89, 91, 87]
])
shape=np.shape(data)
print(shape)
sz=np.size(data)
print("\n",sz)
te=data.dtype
print("\n",te)

print("\n",data[:,2])
print("\n",data[0])
print("\n",data[:,1])
print("\n",data[7:10])
print("\n",data[:,3:5])

maths=np.array(data[:,2])
print("\n",maths)
avg=np.average((maths))
print("\n",avg)

min_sci=np.min((data[:,3]))
print("\n",min_sci)
max_sci=np.max((data[:,3]))
print("\n",max_sci)


sum_math=np.sum((maths))

print("\n",sum_math)
overall_avg=np.average((data[:,0:]))
print("\n",overall_avg)
i=2
for i in range(2,5):
    avg_score=np.average((data[:,i:]))
    print("\n",avg_score)


student_ids = data[data[:, 2] > 85][:, 0]
print(student_ids)