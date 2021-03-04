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


class Ferry:
    def __init__(self, layout):
        grid = [list(r) for r in sample_layout.splitlines()]
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
        self.add_adjacent_seats_to_each_seat(self.seat_list)

    def __str__(self):
        return "\n".join(
            [
                "".join([c.state if isinstance(c, Seat) else "." for c in row])
                for row in self.grid
            ]
        )

    def add_adjacent_seats_to_each_seat(self, seat_list):
        def ranger(z, max_z):
            return range(max(0, z - 1), min(z + 2, max_z))

        for seat in seat_list:
            for ri in ranger(seat.row, self.rows):
                for ci in ranger(seat.col, self.cols):
                    if ri != seat.row or ci != seat.col:
                        if isinstance(self.grid[ri][ci], Seat):
                            seat.adjacent_seats.append(self.grid[ri][ci])

    def calculate_update_all_seats(self):
        for seat in self.seat_list:
            seat.calculate_state_update()
        self.seats_stable = all(not seat.will_change for seat in self.seat_list)

    def do_update_all_seats(self):
        for seat in self.seat_list:
            seat.do_state_update()

    def start_chaos(self):
        while True:                         # infinite loop, ho!
            ferry.calculate_update_all_seats()
            if ferry.seats_stable:
                return self
            else:
                ferry.do_update_all_seats()

    def count_occupied(self):
        return sum(1 for s in self.seat_list if s.state == '#')


class Seat:
    def __init__(self, state, grid_position):
        self.state = state
        self.next_state = None
        self.will_change = None
        self.row, self.col = grid_position
        self.adjacent_seats = []

    def calculate_state_update(self):
        # check adjacent seats against rules
        if self.state == "L" and all(
            adj_s.state == "L" for adj_s in self.adjacent_seats
        ):
            self.next_state = "#"
        elif (
            self.state == "#"
            and sum(1 for adj_s in self.adjacent_seats if adj_s.state == "#") > 3
        ):
            self.next_state = "L"
        else:
            self.next_state = self.state

        # update future change flag
        self.will_change = True if self.next_state != self.state else False

    def do_state_update(self):
        self.state = self.next_state
        self.next_state = None
        self.will_change = None


ferry = Ferry(sample_layout)
num_occupied = ferry.start_chaos().count_occupied()

print(f'After stablization, the number of occupied seats is:\n>>> {num_occupied}')