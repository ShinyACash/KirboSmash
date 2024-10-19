import poyo

while True:
    text = input('poyo> ')
    result, error = poyo.run('<stdin>', text)

    if error: 
        print(error.as_string())
        ext = input("Poyoooo.... Press Any Key to Exit.")
        break
    else: print(result)