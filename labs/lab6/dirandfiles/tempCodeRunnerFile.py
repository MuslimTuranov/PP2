import os

location1 = r'C:\'
print([name for name in os.listdir(location1)]) 
print([name for name in os.listdir(location1) if os.path.isdir(os.path.join(location1, name))]) 
print([name for name in os.listdir(location1) if not os.path.isdir(os.path.join(location1, name))]) 
