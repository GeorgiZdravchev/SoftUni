volume = int(input())
pipe_a = int(input())
pipe_b = int(input())
hours = float(input())

pipe_a_output = pipe_a * hours
pipe_b_output = pipe_b * hours
both_pipes = pipe_b_output + pipe_a_output
pipe_a_percent = pipe_a_output / both_pipes * 100
pipe_b_percent = pipe_b_output / both_pipes * 100
both_pipes_percent = (both_pipes * 100) // volume
formatted_pipe_a = "{:.2f}".format(pipe_a_percent)
formatted_pipe_b = "{:.2f}".format(pipe_b_percent)
formatted_both_pipes = "{:.2f}".format(both_pipes)
if both_pipes <= volume :
    print(f"The pool is {both_pipes_percent}% full. Pipe 1: {formatted_pipe_a}%. Pipe 2: {formatted_pipe_b}%.")
elif both_pipes > volume :
    overflow = both_pipes - volume
    formatted_overflow = "{:.2f}".format(overflow)
    print(f"For {hours} hours the pool overflows with {formatted_overflow} liters.")