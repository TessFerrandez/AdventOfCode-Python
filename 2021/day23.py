"""
Based on solution from zmerlynn
"""
import heapq


HALL_LEN = 11
NUM_ROOMS = 4

ROOM_POS = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
ROOMS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
ROOM_AT = [(2, 'A'), (4, 'B'), (6, 'C'), (8, 'D')]
MOVE_COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
NO_STOP = (2, 4, 6, 8)


class State:
    @classmethod
    def from_string(cls, state_str):
        hall_str = state_str[:HALL_LEN]
        hall = [room if room != '.' else None for room in hall_str]

        room_str = state_str[HALL_LEN + 1:]
        rooms = []
        for i in range(4):
            room0 = room_str[i * 2] if room_str[i * 2] != '.' else None
            room1 = room_str[i * 2 + 1] if room_str[i * 2 + 1] != '.' else None
            rooms.append((room0, room1))

        return State(hall, rooms)

    def __init__(self, hall, rooms) -> None:
        self.hall = hall
        self.rooms = rooms

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other):
        return False

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        hall_str = ''.join(hall if hall else '.' for hall in self.hall)
        room_str = ''
        for room in self.rooms:
            room_str += ''.join(section if section else '.' for section in room)
        return hall_str + "|" + room_str

    def final(self) -> bool:
        return str(self) == '...........|AABBCCDD'

    def moves_from_hall(self, hall_i):
        pod = self.hall[hall_i]

        # if there is no pod in the hall
        # there is no move
        if not pod:
            return[]

        pod_room = ROOM_POS[pod]

        # if there is a pod between us and the room
        # we can't move there
        for hall_idx in between(hall_i, pod_room):
            if self.hall[hall_idx]:
                return []

        # check if we can get to the room
        room_move = self.moves_into_wanted_room(pod)
        if not room_move:
            return []

        # we can move to the room
        cost, new_rooms = room_move
        cost += dist(hall_i, pod_room) * MOVE_COSTS[pod]
        hall = self.hall[:]
        hall[hall_i] = None
        return [(cost, State(hall, new_rooms))]

    def moves_from_room(self, room_i):
        possible_moves_from_room_to_hall = self.moves_from_room_to_hall(room_i)
        if not possible_moves_from_room_to_hall:
            return []

        cost, pod, room_pos, new_rooms = possible_moves_from_room_to_hall

        possible_stops = []
        for pos in between(room_pos, HALL_LEN):
            if self.hall[pos]:
                # There is a pod in the way.
                break
            possible_stops.append(pos)
        for pos in between(room_pos, -1):
            if self.hall[pos]:
                # There is a pod in the way.
                break
            possible_stops.append(pos)
        possible_stops = [stop for stop in possible_stops if stop not in NO_STOP]

        out = []
        for stop in possible_stops:
            new_hall = self.hall[:]
            new_hall[stop] = pod
            out.append((cost + MOVE_COSTS[pod] * dist(room_pos, stop), State(new_hall, new_rooms)))
        return out

    def moves_from_room_to_hall(self, room_i):
        room_pos, room_pod = ROOM_AT[room_i]
        front, back = self.rooms[room_i]

        # if there is nothing in the room
        if not back and not front:
            return None

        if back == room_pod:
            # back already in the right place
            if not front or front == room_pod:
                # either empty or already in the right place
                return None
            # back is set, but front pod does not belong to room
            # so it can move
            steps = 1
        elif not front:
            # there is a pod in the back of the room
            steps = 2
        else:
            steps = 1

        rooms = [list(room[:]) for room in self.rooms]
        pod = rooms[room_i][steps - 1]
        rooms[room_i][steps - 1] = None
        return [MOVE_COSTS[pod] * steps, pod, room_pos, rooms]

    def moves_into_wanted_room(self, pod):
        """
        Assuming you stand right outside the room
        what valid moves are there?
        returns: None or (cost, new rooms array)
        """
        room_idx = ROOMS[pod]
        room = self.rooms[room_idx]
        steps = 2

        if room[0]:
            # Room is full.
            return None
        if room[1]:
            # Back of room has a pod.
            if room[1] != pod:
                # But not `pod`.
                return None
            steps = 1

        # Create a new room array usable for State()
        rooms = [list(room[:]) for room in self.rooms]
        rooms[room_idx][steps - 1] = pod
        return (MOVE_COSTS[pod] * steps, [tuple(room) for room in rooms])

    def valid_moves(self):
        out = []

        for i in range(HALL_LEN):
            out += self.moves_from_hall(i)

        for i in range(NUM_ROOMS):
            out += self.moves_from_room(i)

        return sorted(out)


def between(i1, i2):
    if i1 < i2:
        return range(i1 + 1, i2)
    return range(i1 - 1, i2, -1)


def dist(i1, i2):
    return abs(i1 - i2)


def tests():
    # final state
    assert State.from_string('...........|AABBCCDD').final()
    assert not State.from_string('...........|ABBACCDD').final()
    assert not State.from_string('A..........|.BBACCDD').final()
    assert not State.from_string('A..........|.ABBCCDD').final()
    assert not State.from_string('AA.........|..BBCCDD').final()

    # positions between
    assert list(between(5, 9)) == [6, 7, 8]
    assert list(between(9, 5)) == [8, 7, 6]

    # distance
    assert dist(9, 5) == 4

    # moves from hall
    print(State.from_string('B..........|AA.BCCDD').moves_from_hall(0))
    print(State.from_string('AB.........|.A.BCCDD').moves_from_hall(1))
    print(State.from_string('BA.........|.A.BCCDD').moves_from_hall(1))
    print(State.from_string('.....D.....|AABBCC.D').moves_from_hall(5))

    # moves from room to hall
    print(State.from_string('...........|.A.BCCDD').moves_from_room_to_hall(1))
    print(State.from_string('...........|.B.ACCDD').moves_from_room_to_hall(1))
    print(State.from_string('...........|.BBACCDD').moves_from_room_to_hall(1))

    # moves from room
    print(State.from_string('.C.........|BBAACCDD').moves_from_room(1))

    # valid moves
    print(State.from_string('...........|BACDBCDA').valid_moves())
    print(State.from_string('...B.......|BACD.CDA').valid_moves())
    print(State.from_string('...B.C.....|BA.D.CDA').valid_moves())
    print(State.from_string('...B.......|BA.DCCDA').valid_moves())
    print(State.from_string('...B.D.....|BA..CCDA').valid_moves())
    print(State.from_string('.....D.....|BA.BCCDA').valid_moves())
    print(State.from_string('.....D.D...|BA.BCC.A').valid_moves())
    print(State.from_string('...B.D.D...|.A.BCC.A').valid_moves())
    print(State.from_string('...B.D.D.A.|.A.BCC..').valid_moves())
    print(State.from_string('...B.D...A.|.A.BCC.D').valid_moves())
    print(State.from_string('...B.....A.|.A.BCCDD').valid_moves())
    print(State.from_string('.........A.|.ABBCCDD').valid_moves())

    # verify hash
    state1 = State.from_string('...........|BBAACCDD')
    state2 = State.from_string('...........|BBAACCDD')
    state_set = {state1, state2}
    assert len(state_set) == 1


def solve(input_state):
    start = State.from_string(input_state)
    visited = set()

    todo = [(0, start, ())]
    while todo:
        cost, state, path = heapq.heappop(todo)
        if state in visited:
            # print("already visited", state)
            continue

        print("cost", cost, "state", state)
        visited.add(state)

        if state.final():
            print("final", cost)
            for step in path:
                print(step)
            return cost

        for move_cost, move_to_state in state.valid_moves():
            heapq.heappush(todo, (cost + move_cost, move_to_state, tuple(list(path) + [state])))


# tests()
# solve("...........|BACDBCDA")
print("Part 1:", solve("...........|ACDCADBB"))
