

#kirjutate algteksti
#Küste sisendinfo
#Kontrollite sisendinfo üle
#loote algmuutujad
#Genereerite graafika

def print_instructions():
    print("see on eeltekst")


def check_if_correct_info():
    print("kontrollime üle, kas on õige")

def ask_for_information():
    print("siin on input asi üks")
    check_if_correct_info()
    print("siin on input asi kaks")
    check_if_correct_info()
    return False
    
def generate_graph():
    print("#####")
    print("#####")
    print("#####")
    print("#####")

def main_function():
    print_instructions()
    if ask_for_information():
        generate_graph()
    else:
        print("something went wrong")
    
    

main_function()