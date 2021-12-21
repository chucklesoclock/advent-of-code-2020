class Ferry:
    def __init__(self, layout, part):
        grid = [list(r) for r in layout.splitlines()]
        self.seat_list = []
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char != ".":
                    seat = Seat(char, (r, c))
                    grid[r][c] = seat
                    self.seat_list.append(seat)
                else:
                    grid[r][c] = None
        self.grid = grid
        self.seats_stable = False
        self.rows = len(grid)
        self.cols = len(row)
        self.part = part
        if self.part == 1:
            self.add_adjacent_seats_to_each_seat()
        elif self.part == 2:
            self.add_visible_seats_to_each_seat()

    def __str__(self):
        return "\n".join(
            [
                "".join([c.state if isinstance(c, Seat) else "." for c in row])
                for row in self.grid
            ]
        )

    def add_adjacent_seats_to_each_seat(self):
        def ranger(z, max_z):
            return range(max(0, z - 1), min(z + 2, max_z))

        for seat in self.seat_list:
            for ri in ranger(seat.row, self.rows):
                for ci in ranger(seat.col, self.cols):
                    if (ri != seat.row or ci != seat.col) and isinstance(
                        self.grid[ri][ci], Seat
                    ):
                        seat.adjacent_seats.append(self.grid[ri][ci])

    def add_visible_seats_to_each_seat(self):
        for seat in self.seat_list:
            # look down
            for ri in range(seat.row + 1, self.rows):
                if isinstance(self.grid[ri][seat.col], Seat):
                    seat.visible_seats.append(self.grid[ri][seat.col])
                    break
            # look up
            for ri in range(seat.row - 1, -1, -1):
                if isinstance(self.grid[ri][seat.col], Seat):
                    seat.visible_seats.append(self.grid[ri][seat.col])
                    break
            # look right
            for ci in range(seat.col + 1, self.cols):
                if isinstance(self.grid[seat.row][ci], Seat):
                    seat.visible_seats.append(self.grid[seat.row][ci])
                    break

            def inside_ferry(r, c):
                return 0 <= r < self.rows and 0 <= c < self.cols 

            # look left
            for ci in range(seat.col - 1, -1, -1):
                if isinstance(self.grid[seat.row][ci], Seat):
                    seat.visible_seats.append(self.grid[seat.row][ci])
                    break
            a, z = [f(seat.row, seat.col) for f in [min, max]]
            # look down-right
            i, j = seat.row, seat.col
            while True:
                i += 1
                j += 1
                if not inside_ferry(i, j):
                    break
                if isinstance(self.grid[i][j], Seat):
                    seat.visible_seats.append(self.grid[i][j])
                    break
            # look up-left
            i, j = seat.row, seat.col
            while True:
                i -= 1
                j -= 1
                if not inside_ferry(i, j):
                    break
                if isinstance(self.grid[i][j], Seat):
                    seat.visible_seats.append(self.grid[i][j])
                    break
            # look down-left
            i, j = seat.row, seat.col
            while True:
                i += 1
                j -= 1
                if not inside_ferry(i, j):
                    break
                if isinstance(self.grid[i][j], Seat):
                    seat.visible_seats.append(self.grid[i][j])
                    break
            # look up-right
            i, j = seat.row, seat.col
            while True:
                i -= 1
                j += 1
                if not inside_ferry(i, j):
                    break
                if isinstance(self.grid[i][j], Seat):
                    seat.visible_seats.append(self.grid[i][j])
                    break

    def calculate_update_all_seats(self):
        check_type = "adjacent" if self.part == 1 else "visible"
        for seat in self.seat_list:
            seat.calculate_state_update(check_type)
        self.seats_stable = all(not seat.will_change for seat in self.seat_list)
        return self

    def do_update_all_seats(self):
        for seat in self.seat_list:
            seat.do_state_update()

    def start_chaos(self):
        while True:  # infinite loop, ho!
            self.calculate_update_all_seats()
            if self.seats_stable:
                return self
            else:
                self.do_update_all_seats()

    def count_occupied(self):
        return sum(1 for s in self.seat_list if s.state == "#")


class Seat:
    def __init__(self, state, grid_position):
        self.state = state
        self.next_state = None
        self.will_change = None
        self.row, self.col = grid_position
        self.adjacent_seats = []
        self.visible_seats = []

    def __repr__(self) -> str:
        return f"Seat({self.state}, ({self.row},{self.col}))"

    def calculate_state_update(self, check_type="adjacent"):
        if check_type == "adjacent":
            neighbors = self.adjacent_seats
            tolerance = 3
        elif check_type == "visible":
            neighbors = self.visible_seats
            tolerance = 4

        # check neighbor seats against rules
        if self.state == "L" and all(neighbor.state == "L" for neighbor in neighbors):
            self.next_state = "#"
        elif (
            self.state == "#"
            and sum(1 for neighbor in neighbors if neighbor.state == "#") > tolerance
        ):
            self.next_state = "L"
        else:
            self.next_state = self.state

        # update future change flag
        self.will_change = self.next_state != self.state

    def do_state_update(self):
        self.state = self.next_state
        self.next_state = None
        self.will_change = None


if __name__ == "__main__":
    with open("input/data11.txt") as f:
        layout = f.read()
    print(Ferry(layout, part=1).start_chaos().count_occupied())
    print(Ferry(layout, part=2).start_chaos().count_occupied())

sample_layout = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def test_part_1_sample():
    assert Ferry(sample_layout, part=1).start_chaos().count_occupied() == 37


def test_part_2_sample_individual_states():
    ferry = Ferry(sample_layout, part=2)
    for i in range(2):
        ferry.calculate_update_all_seats().do_update_all_seats()
    given_third_iteration = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
    assert str(ferry) == given_third_iteration



def test_part_2_sample():
    assert Ferry(sample_layout, part=2).start_chaos().count_occupied() == 26