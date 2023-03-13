VERT = "║"
VERT_LEFT = "╣"
VERT_RIGHT = "╠"
UPPER_RIGHT_CORNER = "╗"
UPPER_LEFT_CORNER = "╔"
LOWER_RIGHT_CORNER = "╝"
LOWER_LEFT_CORNER = "╚"
HORIZ_UP = "╩"
HORIZ_DOWN = "╦"
HORIZ = "═"
BLANK = " "
ALL = [
    VERT_LEFT,
    VERT,
    VERT_RIGHT,
    UPPER_RIGHT_CORNER,
    UPPER_LEFT_CORNER,
    LOWER_RIGHT_CORNER,
    LOWER_LEFT_CORNER,
    HORIZ_UP,
    HORIZ_DOWN,
    HORIZ,
    BLANK,
]
dirs = [
    # R, C
    (0, -1),  # West
    (0, 1),  # East
    (1, 0),  # North
    (-1, 0),  # South
]
rules = {
    BLANK: {
        "w": {LOWER_RIGHT_CORNER, UPPER_RIGHT_CORNER, VERT, VERT_LEFT, BLANK},
        "e": {LOWER_LEFT_CORNER, UPPER_LEFT_CORNER, VERT_RIGHT, VERT, BLANK},
        "n": {HORIZ, HORIZ_UP, LOWER_LEFT_CORNER, LOWER_RIGHT_CORNER, BLANK},
        "s": {HORIZ, HORIZ_DOWN, UPPER_LEFT_CORNER, UPPER_RIGHT_CORNER, BLANK},
    },
    VERT_LEFT: {
        "w": {
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "e": {VERT, VERT_RIGHT, UPPER_LEFT_CORNER, LOWER_LEFT_CORNER, BLANK},
        "n": {VERT, VERT_RIGHT, UPPER_RIGHT_CORNER, UPPER_LEFT_CORNER, HORIZ_DOWN},
        "s": {VERT, VERT_RIGHT, LOWER_RIGHT_CORNER, LOWER_LEFT_CORNER, HORIZ_UP},
    },
    VERT: {
        "w": {
            VERT_LEFT,
            VERT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            BLANK,
        },
        "e": {
            VERT,
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
            BLANK,
        },
        "n": {
            VERT_LEFT,
            VERT_RIGHT,
            VERT,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
        },
        "s": {
            VERT_LEFT,
            VERT_RIGHT,
            VERT,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
        },
    },
    VERT_RIGHT: {
        "w": {
            BLANK,
            VERT_LEFT,
            VERT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
        },
        "e": {
            VERT_LEFT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "n": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
        },
        "s": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
        },
    },
    UPPER_RIGHT_CORNER: {
        "w": {
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "e": {
            BLANK,
            VERT,
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
        },
        "n": {
            BLANK,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ,
        },
        "s": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
        },
    },
    UPPER_LEFT_CORNER: {
        "w": {
            BLANK,
            VERT_LEFT,
            VERT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
        },
        "e": {
            VERT_LEFT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "n": {
            BLANK,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ,
        },
        "s": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
        },
    },
    LOWER_RIGHT_CORNER: {
        "w": {
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "e": {
            BLANK,
            VERT,
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
        },
        "n": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
        },
        "s": {
            BLANK,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
            HORIZ,
        },
    },
    LOWER_LEFT_CORNER: {
        "w": {
            BLANK,
            VERT_LEFT,
            VERT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
        },
        "e": {
            VERT_LEFT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "n": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
        },
        "s": {
            BLANK,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
            HORIZ,
        },
    },
    HORIZ_UP: {
        "w": {
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "e": {
            VERT_LEFT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "n": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
        },
        "s": {UPPER_LEFT_CORNER, UPPER_RIGHT_CORNER, HORIZ_DOWN, HORIZ, BLANK},
    },
    HORIZ_DOWN: {
        "w": {
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "e": {
            VERT_LEFT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "n": {
            BLANK,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ,
        },
        "s": {
            VERT_LEFT,
            VERT,
            VERT_RIGHT,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
        },
    },
    HORIZ: {
        "w": {
            VERT_RIGHT,
            UPPER_LEFT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "e": {
            VERT_LEFT,
            UPPER_RIGHT_CORNER,
            LOWER_RIGHT_CORNER,
            HORIZ_UP,
            HORIZ_DOWN,
            HORIZ,
        },
        "n": {
            BLANK,
            LOWER_RIGHT_CORNER,
            LOWER_LEFT_CORNER,
            HORIZ_UP,
            HORIZ,
        },
        "s": {
            BLANK,
            UPPER_RIGHT_CORNER,
            UPPER_LEFT_CORNER,
            HORIZ_DOWN,
            HORIZ,
        },
    },
}
