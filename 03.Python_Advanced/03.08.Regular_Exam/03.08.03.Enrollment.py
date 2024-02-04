def gather_credits(num, *args):
    min_credits = num
    current_credits = 0

    enrolled = []

    for arg in args:
        subject = arg[0]
        num_credits = arg[1]

        if min_credits > current_credits and subject not in enrolled:
            enrolled.append(subject)
            current_credits += num_credits

    enrolled.sort()

    result = ""

    if min_credits > current_credits:
        credits_shortage = min_credits - current_credits
        result += f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

    else:
        result += f"Enrollment finished! Maximum credits: {current_credits}.\n"
        result += f"Courses: {', '.join(x for x in enrolled)}"

    return result.strip()


print(gather_credits(
    80,
    ("Basics", 27),
    ("Basics_01", 53),
))

print()

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Fundamentals", 27),
    ("Fundamentals", 27),
    ("Basics", 27),
))

print()

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
