your_name = "Kaiky"
course = "RMOTR Python"

greeting_message = "Welcome {} to the {} course!".format(your_name, course)
print(greeting_message)

def test_name_not_blank():
    assert your_name != ' ', "Your name can't be blank"

def test_name_is_long_enough():
    assert len(your_name) > 3, "Your name contain more 3 characters"

print("Tests All Working")
