from base_change import to_10

def main():
    test_10()

def test_8():
    assert to_10(75, 8) == 61
    assert to_10(127, 8) == 87
    assert to_10(1275, 8) == 701

def test_4():
    assert to_10(32, 4) == 14 
    assert to_10(33333333, 4) == 65535

def test_2():
    assert to_10(101, 2) == 5
    assert to_10(11111111111111, 2) == 16383

if __name__ == "__main__":
    main()
