# PROJECT EULER PROBLEM 1 SOLUTION IN PYTHON 2.7.3
nums= range(1,1000)
Sumofmultiples = 0
for i in nums:
    if i % 3 == 0 or i % 5 == 0 :
        Sumofmultiples = i + Sumofmultiples
print Sumofmultiples