pool_volume = int(input())

pipe_one_debit = int(input())
pipe_two_debit = int(input())

hours_away = float(input())

pipe_one_debit_volume = pipe_one_debit * hours_away
pipe_two_debit_volume = pipe_two_debit * hours_away
pipe_total_volume = pipe_one_debit_volume + pipe_two_debit_volume

if pool_volume >= pipe_total_volume:
    pipe_total_volume_percent = (pipe_total_volume / pool_volume) * 100
    pipe_one_debit_percent = (pipe_one_debit_volume / pipe_total_volume) * 100
    pipe_two_debit_percent = (pipe_two_debit_volume / pipe_total_volume) * 100

    print(f"The pool is {pipe_total_volume_percent:.2f}% full. "
          f"Pipe 1: {pipe_one_debit_percent:.2f}%. "
          f"Pipe 2: {pipe_two_debit_percent:.2f}%.")
else:
    pool_overflow = pipe_total_volume - pool_volume

    print(f"For {hours_away} hours the pool overflows with {pool_overflow:.2f} liters.")
