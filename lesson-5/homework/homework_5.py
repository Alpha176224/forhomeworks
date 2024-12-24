# def convert_cel_to_far(temp_cel):
#     """Return the Celsius temperature temp_cel converted to Fahrenheit."""
#     temp_far = temp_cel * (9 / 5) + 32
#     return temp_far


# def convert_far_to_cel(temp_far):
#     """Return the Fahrenheit temperature temp_far converted to Celsius."""
#     temp_cel = (temp_far - 32) * (5 / 9)
#     return temp_cel

# temp_far = input("Enter a temperature in degrees F: ")

# temp_cel = convert_far_to_cel(float(temp_far))

# print(f"{temp_far} degrees F = {temp_cel:.2f} degrees C")

# temp_cel = input("\nEnter a temperature in degrees C: ")

# temp_far = convert_cel_to_far(float(temp_cel))

# print(f"{temp_cel} degrees C = {temp_far:.2f} degrees F")


# def invest(amount, rate, years):
#     """Display year on year growth of an initial investment"""
#     for year in range(1, years + 1):
#         amount = amount * (1 + rate)
#         print(f"year {year}: ${amount:,.2f}")


# amount = float(input("Enter a principal amount: "))
# rate = float(input("Enter an anual rate of return: "))
# years = int(input("Enter a number of years: "))

# invest(amount, rate, years)


# num = int(input("Enter a positive integer: "))
# for divisor in range(1, num + 1):
#     if num % divisor == 0:
#         print(f"{divisor} is a factor of {num}")


# def enrollment_stats(list_of_universities):
#     # Variables
#     total_students = []
#     total_tuition = []

#     # Iterate through lists, adding values
#     for university in list_of_universities:
#         total_students.append(university[1])
#         total_tuition.append(university[2])

#     # Return variables
#     return total_students, total_tuition


# def mean(values):
#     """Return the mean value in the list `values`"""
#     return sum(values) / len(values)


# def median(values):
#     """Return the median value of the list `values`"""
#     values.sort()
#     # If the number of values is odd,
#     # return the middle value of the list
#     if len(values) % 2 == 1:
#         # The value at the center of the list is the value
#         # at whose index is half of the length of the list,
#         # rounded down
#         center_index = int(len(values) / 2)
#         return values[center_index]
#     # Otherwise, if the length of the list is even, return
#     # the mean of the two center values
#     else:
#         left_center_index = (len(values) - 1) // 2
#         right_center_index = (len(values) + 1) // 2
#         return mean([values[left_center_index], values[right_center_index]])


# universities = [
#     ["California Institute of Technology", 2175, 37704],
#     ["Harvard", 19627, 39849],
#     ["Massachusetts Institute of Technology", 10566, 40732],
#     ["Princeton", 7802, 37000],
#     ["Rice", 5879, 35551],
#     ["Stanford", 19535, 40569],
#     ["Yale", 11701, 40500],
# ]

# totals = enrollment_stats(universities)

# print("\n")
# print("*****" * 6)
# print(f"Total students:   {sum(totals[0]):,}")
# print(f"Total tuition:  $ {sum(totals[1]):,}")
# print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
# print(f"Student median:   {median(totals[0]):,}")
# print(f"\nTuition mean:   $ {mean(totals[1]):,.2f}")
# print(f"Tuition median: $ {median(totals[1]):,}")
# print("*****" * 6)
# print("\n")


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
