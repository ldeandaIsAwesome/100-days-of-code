from data import us_state_abbrev, states_list

convert = list(us_state_abbrev)

def tenth_entry_of_each():
    print("tenth item of abbrev is: " + convert[9] + ", " + us_state_abbrev[convert[9]])
    print("tenth item of states is: " + states_list[9])

def fourty_fifth_key_dictionary():
    print("The fourty fifth key is: " + convert[44])

def twenty_seventh_value_dictionary():
    print("The twenty seventh item is: " + us_state_abbrev[convert[26]])

def replace_key_with_list_item():
    us_state_abbrev[convert[14]] = states_list[27]
    print("After replacing, the 15th key is now: " + us_state_abbrev[convert[14]])

def main():
    tenth_entry_of_each()
    fourty_fifth_key_dictionary()
    twenty_seventh_value_dictionary()
    replace_key_with_list_item()

if __name__ == "__main__":
    main()
