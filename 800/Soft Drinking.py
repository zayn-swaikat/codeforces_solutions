line = list(map(int, input().split()))
n_friends = line[0]
k_bottles = line[1]
l_milliliters = line[2]
c_limes = line[3]
d_slices = line[4]
p_salt = line[5]
nl_need = line[6]
np_salt = line[7]
drink = (k_bottles * l_milliliters)//nl_need
limes = c_limes * d_slices
salt = p_salt//np_salt
print((min(drink, limes, salt))//n_friends)