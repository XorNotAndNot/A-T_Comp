# create password.txt file and make it appendable
with open ("password.txt", "a+") as passwords:

    # create the pass checking function
    def pass_checker():
        # password must be 8-32 characters
        for i in passwords:
            if i not in range(8, 32):
                print("Password is too long/short")
            else:
                continue
