# single inheritance example

class GrandParent:
    key="abc@123"
    def Grand_parent_method(self):
        return "This is grand parent method"
class Father(GrandParent):
    def Parent_Method(self):
        return "This is Parent Method"

child_ref_obj=Father()
print(child_ref_obj.Parent_Method())
print(child_ref_obj.Grand_parent_method())
print(child_ref_obj.key)


# O/p=This is Parent Method
# This is grand parent method
# abc@123