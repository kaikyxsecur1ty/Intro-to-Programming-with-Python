y_name = ''
course = "Python INE"

hello_msg = f"Welcome {y_name} in the {course}"
print(hello_msg)

def test_name_not_blank():
  assert y_name != ' ', "Your name can't be blank"

def test_name_is_long_enough():
  assert len(y_name) > 3, "Your name contain more 3 chars"

# Chamada das funções
test_name_is_long_enough()
test_name_not_blank()

print("Tests All Working")
