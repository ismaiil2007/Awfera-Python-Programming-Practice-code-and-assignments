text = input("Please enter Text: ")
vowels = ["A","E","I","O","U"]

if text:
 reversed_text = []
 length = len(text) - 1
 while length >= 0:
    reversed_text.append(text[length])
    length -= 1
 new_text = ''.join(reversed_text)
 print(f"The string in reverse order is: {new_text}")

 vowels_found = []
 for i in text:

    for j in vowels:
        if i == j or i == j.lower():
            # print(i)
            vowels_found.append(i)
 print(f"The vowels found in the input are: {', '.join(vowels_found)}")
else:
   print("No Input Given")          