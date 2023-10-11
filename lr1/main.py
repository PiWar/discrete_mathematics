import matplotlib.pyplot as plt

operations = ['A', 'B', 'A∧B', 'A∨B', 'A/B', 'B/A', 'A\\B']
operations_colors = ['orange', 'blue', 'green', 'purple', 'red', 'slategray', 'cyan']
operations_colors.reverse()
y_len = len(operations)
y_ticks = [i for i in range(7, 0, -1)]
x_lim = (-15, 15)
x_ticks = [i for i in range(x_lim[0], x_lim[1] + 1, 5)]
axis_margin = 0.1


def create_set(start_x, end_x, start_type='filled', end_type='filled'):
    return {
        'start': {
            'x': start_x,
            'type': start_type
        },
        'end': {
            'x': end_x,
            'type': end_type
        }
    }


sets = [
    [
        create_set(-2, 12)
    ],
    [
        create_set(-15, 3, 'hollow', 'hollow')
    ],
    [
        create_set(-2, 3, end_type='hollow')
    ],
    [
        create_set(-15, 12, 'hollow')
    ],
    [
        create_set(3, 12)
    ],
    [
        create_set(-15, -2, 'hollow', 'hollow')
    ],
    [
        create_set(-15, 2, 'hollow', 'hollow'),
        create_set(3, 12)
    ]
]


def setup_x_axis(axes):
    for index, color in enumerate(operations_colors):
        plt.plot(x_lim, [index + 1, index + 1], color=color)

        plt.plot((x_lim[1] - 0.25, x_lim[1]), [index + 0.9, index + 1], color=color)
        plt.plot((x_lim[1] - 0.25, x_lim[1]), [index + 1.1, index + 1], color=color)

    axes.set_xticks(x_ticks)


def setup_y_axis(axes):
    axes.set_yticks(y_ticks)
    axes.set_yticklabels(operations, fontsize=16, color='darkorange')


def setup_plt():
    fig, axes = plt.subplots()

    setup_y_axis(axes)
    setup_x_axis(axes)

    plt.margins(axis_margin)


def show_plt():
    plt.show()


def draw_set_point(x, y, color, point_type):
    plt.plot(x, y, 'o', c=color, mfc=color if point_type == 'filled' else 'white')


def float_range(start, end, step):
    while start < end:
        yield start
        start += step


def draw_fill_between_points(start_x, end_x, y, color):
    step = 0.75
    for x in float_range(start_x + step, end_x, step):
        plt.plot(
            [x, x],
            [y, y + 0.2],
            color=color
        )


def show_sets():
    for index, set_value in enumerate(sets):
        y = y_len - index
        color = operations_colors[y - 1]
        for line in set_value:
            start, end = [line['start'], line['end']]
            start_x, end_x = [start['x'], end['x']]

            draw_fill_between_points(start_x, end_x, y, color)

            draw_set_point(start_x, y, color, start['type'])
            draw_set_point(end_x, y, color, end['type'])


def main():
    setup_plt()
    show_sets()
    show_plt()


if __name__ == '__main__':
    main()
