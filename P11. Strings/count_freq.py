
def count_frequency(string):
    # Initialize an array of size 26 to count character frequencies
    count = [0] * 26

    # Update frequency for each character in the string
    for char in string:
        count[ord(char) - ord('a')] += 1

    # Print characters with their frequencies
    for i in range(26):
        if count[i] > 0:
            print(f"{chr(i + ord('a'))} : {count[i]}")

if __name__ == "__main__":
    string = "geeksforgeeks"
    count_frequency(string)
