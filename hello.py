def greet():
    print("Hello, GitHub Actions!")
    
def test_greet():
    assert greet() is None

if __name__ == "__main__":
    greet()
    test_greet()
    print("Hello, CI Pipeline !")
