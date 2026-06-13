import string

def check_pass():
    print(" --- Defensive Gatekeeper Activated --- ")

    #User raw feed input loop
    while True:
        pwd = input("Enter Password to validate (or type 'exit'):").strip()

        if pwd.lower() == 'exit':
            print("Gatekeeper Offline.")
            break
        #1. Length constraint check 
        if len(pwd) < 8:
            print("Status: WEAK (Under 8 characters - Brute Force Risk)\n")
            continue

        #2. Pattern entropy validation using C- optimized built- ins 
        has_up = any(c.isupper() for c in pwd )
        has_num = any(c.isdigit() for c in pwd )
        has_sym = any(c in string.punctuation for c in pwd)

        #3.Risk classification matrix
        if has_up and has_num and has_sym:
            print ("Status: STRONG (Entropy Verified. Gatekeeper Pass)\n")
        elif (has_up and has_num) or (has_num and has_sym) or (has_up and has_sym):
            print("Status: MEDIUM (Increase character variety)\n")
        else:
            print("Status: WEAK (Missing mandatory character complexity)\n")


if __name__ == "__main__":
    check_pass()
