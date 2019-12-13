def read_lines(filename):
    with open(filename) as f:
        lines = list(f.readlines())
        lines = [x.strip() for x in lines]
        return lines

def read_lists(filename, separator):
    with open(filename) as f:
        output = []
        lines = read_lines(filename)
        for line in lines:
            line = line.split(separator)
            line = [x.strip() for x in line]
            output.append(line)
        return output
