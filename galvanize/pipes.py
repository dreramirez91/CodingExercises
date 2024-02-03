def pipe_outputs(num_pipes, steps):
    pipes = [8 for pipe in range(num_pipes)]
    print(pipes)
    for step in steps:
        if len(step) == 1:
            pipe = step[0] - 1
            pipes[pipe : pipe + 2] = [pipes[pipe] + pipes[pipe + 1]]
        else:
            pipe_to_split = step[0] - 1
            left = step[1]
            right = pipes[pipe_to_split] - step[1]
            pipes[pipe_to_split : pipe_to_split + 1] = [left, right]
    return pipes


print(pipe_outputs(3, [[2, 4], [1], [1], [1, 2]]))
