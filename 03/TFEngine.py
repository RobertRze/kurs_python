tc_data = [["tc_name:Test 1","first_name:Tim", "last_name:Tam", "birthday:2021-01-01", "doc_number:YY001", "city:Warszawa", "street:Długa"],
["tc_name:Test 2","first_name:John", "last_name:Test", "birthday:2020-01-01", "doc_number:XX001", "city:Gdynia", "street:Tuwima"],
["tc_name:Test 3","first_name:Ann", "last_name:Czecia", "birthday:2022-01-01", "doc_number:ZZ001", "city:Gdańsk", "street:Krótka"]]
def get_data(v_name):
    for test_data in tc_data[n]:
        test_data = test_data.split(":")
        if test_data[0] == v_name:
            v_value = test_data[1]
            return v_value

def hello(first_name, last_name):
    print(f"Cześć {first_name} {last_name}")

def addres(street, city):
    print(f"Mieszkasz na ulicy {street} w {city}")

for n in range(int(len(tc_data))):
    print(f"------ {get_data('tc_name')} ------")
    print(f"Obywatel {get_data('first_name')} {get_data('last_name')} urodzony {get_data('birthday')}")
    hello(get_data("first_name"), get_data("last_name"))
    addres(get_data('street'), get_data('city'))



