#Example of Monkey Patching

class normal(object):
    def will_be_assigned(self):
        return "Normal"

def monkey(self):
    return "Monkey-Patched"

# Before Patching
obj = normal();
print('''class normal(object):
    def will_be_assigned(self):
        return "Normal"

def monkey(self):
    return "Monkey-Patched"

# Before Patching
obj = normal();

print("After Patching : " + obj.will_be_assigned())
\n#Out put will be Normal
Before Patching is : ''' + obj.will_be_assigned())

#After Patching

normal.will_be_assigned = monkey
obj = normal();
print('''\n\nnormal.will_be_assigned = monkey
obj = normal();
print("After Patching :  + obj.will_be_assigned())
\n#Out put will be Normal
After Patching : ''' + obj.will_be_assigned())
