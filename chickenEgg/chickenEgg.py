
def chicken():
    return egg()

def egg():
    return chicken()

print("Which came first, the chicken or the egg?")

try:
    print(chicken() + " came first.")

except RuntimeError as e:
    print("No one knows.")