# Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b .
# A @classmethod called description(cls) that prints "This is a utility class for math operations."

# Call both methods without creating an object


class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def add(a,b):
        return a + b
    
    @ classmethod
    def descripltion(cls):
        print("this is a utility class for math operations.")


print(MathUtils.add(9, 7))
MathUtils.descripltion()