import ast
filepath = r"C:\Users\DELL\Desktop\naoum\tp1\policy.txt"
# read the dic from the filepath into the variable policy 
policy = {}
with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = line.strip()
        key = line.split(":")[0]
        value = line.split(":")[1]
        policy[key] = value
        line = fp.readline()

# print(policy)
# I want to convert the key of the policy from chaine of caractere to tuple of two binary string from this "('111100000', '000000111')" to this ('111100000', '000000111')
policy = {ast.literal_eval(key): value for key, value in policy.items()}
policy = {tuple(reversed(key)): value for key, value in policy.items()}
print(policy)

