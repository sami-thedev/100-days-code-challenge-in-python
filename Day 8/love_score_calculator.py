def calculate_love_score(name1, name2):
     # Combine both names into one string
    combined_names = name1 + name2
    lower_names = combined_names.lower()

     # Calculate the number of times letters in "TRUE" occur
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    # Calculate the number of times letters in "LOVE" occur
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

     # Combine the first_digit and second_digit scores to form the  score
    score = int(str(first_digit) + str(second_digit))
      # Print the  score
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")