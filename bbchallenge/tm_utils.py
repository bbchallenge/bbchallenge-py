R, L = 0, 1


def ithl(i):
    return chr(ord("A") + i)


def g(move):
    if move == R:
        return "R"
    return "L"


def to_bbchallenge_format(tm) -> str:
    to_ret = ""
    for i, b in enumerate(tm):
        if i % 6 == 0 and i != 0:
            to_ret += "_"

        if i % 3 == 0 and tm[i + 2] == 0:
            to_ret += "-"
            continue
        if i % 3 == 1 and tm[i + 1] == 0:
            to_ret += "-"
            continue

        if i % 3 == 0:
            to_ret += "0" if b == 0 else "1"
        elif i % 3 == 1:
            to_ret += "R" if b == 0 else "L"
        else:
            if b == 0:
                to_ret += "-"
            else:
                to_ret += ithl(b - 1)

    return to_ret


def from_bbchallenge_format(tm_str):
    """Creates a TM from the official bbchallenge format,
    see https://discuss.bbchallenge.org/t/standard-tm-text-format/.
    """
    to_ret = []
    for i, c in enumerate(tm_str.replace("_", "")):
        if i % 3 == 0:
            if c == "1":
                to_ret.append(1)
            elif c == "0":
                to_ret.append(0)
            else:
                to_ret.append(0)
        elif i % 3 == 1:
            if c == "R":
                to_ret.append(0)
            elif c == "L":
                to_ret.append(1)
            else:
                to_ret.append(0)
        else:
            if c == "-":
                to_ret.append(0)
            else:
                to_ret.append((ord(c) - ord("A")) + 1)
    return to_ret


def pptm(machine, return_repr=False):
    from tabulate import tabulate

    headers = ["s", "0", "1"]
    table = []

    nb_states = len(machine) // 6

    for i in range(nb_states):
        row = [ithl(i)]
        for j in range(2):
            write = machine[6 * i + 3 * j]
            move = machine[6 * i + 3 * j + 1]
            goto = machine[6 * i + 3 * j + 2] - 1

            if goto == -1:
                row.append("???")
                continue

            row.append(f"{write}{g(move)}{ithl(goto)}")
        table.append(row)

    if not return_repr:
        print(tabulate(table, headers=headers))
    else:
        return tabulate(table, headers=headers)


def step(machine, curr_state, curr_pos, tape):
    if not curr_pos in tape:
        tape[curr_pos] = 0

    write = machine[curr_state * 6 + 3 * tape[curr_pos]]
    move = machine[curr_state * 6 + 3 * tape[curr_pos] + 1]
    goto = machine[curr_state * 6 + 3 * tape[curr_pos] + 2] - 1

    if goto == -1:
        return None, None

    tape[curr_pos] = write
    next_pos = curr_pos + (-1 if move else 1)
    return goto, next_pos


def tm_trace_to_image(
    machine, width=900, height=1000, origin=0.5, show_head_direction=False
):
    from PIL import Image

    img = Image.new("RGB", (width, height), color="black")
    pixels = img.load()

    tape = {}
    curr_time = 0
    curr_state = 0
    curr_pos = 0
    tape = {}

    for row in range(1, height):
        last_pos = curr_pos
        curr_state, curr_pos = step(machine, curr_state, curr_pos, tape)

        if curr_state is None:  # halt
            return img

        for col in range(width):
            pos = col - width * (origin)

            if pos in tape:
                pixels[col, row] = (255, 255, 255) if tape[pos] == 1 else (0, 0, 0)
                # pixels[col,row-1] = colors[curr_state-1]

            if pos == curr_pos and show_head_direction:
                pixels[col, row] = (255, 0, 0) if curr_pos > last_pos else (0, 255, 0)

    # img = zoom_at(img,*zoom)
    return img


def zoom_at(img, x, y, zoom):
    from PIL import Image

    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)
