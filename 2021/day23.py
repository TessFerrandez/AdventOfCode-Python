"""
Based on solution from zmerlynn
"""
import heapq
from alive_progress import alive_bar
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


HALL_LEN = 11
NUM_ROOMS = 4

ROOM_POS = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
ROOMS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
ROOM_AT = [(2, 'A'), (4, 'B'), (6, 'C'), (8, 'D')]
MOVE_COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
NO_STOP = (2, 4, 6, 8)


class State:
    @classmethod
    def from_string(cls, state_str, room_size=2):
        hall_str = state_str[:HALL_LEN]
        hall = [room if room != '.' else None for room in hall_str]

        room_str = state_str[HALL_LEN + 1:]
        rooms = []
        for i in range(NUM_ROOMS):
            pods_in_room = tuple(pod if pod != '.' else None for pod in room_str[i * room_size:(i + 1) * room_size])
            rooms.append(pods_in_room)

        return State(hall, rooms, room_size)

    def __init__(self, hall, rooms, room_size) -> None:
        self.hall = hall
        self.rooms = rooms
        assert room_size == 2 or room_size == 4
        self.room_size = room_size

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
        if self.room_size == 2:
            return str(self) == '...........|AABBCCDD'
        elif self.room_size == 4:
            return str(self) == '...........|AAAABBBBCCCCDDDD'
        else:
            return False

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
        return [(cost, State(hall, new_rooms, self.room_size))]

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
            out.append((cost + MOVE_COSTS[pod] * dist(room_pos, stop), State(new_hall, new_rooms, self.room_size)))
        return out

    def moves_from_room_to_hall(self, room_i):
        room_pos, room_pod = ROOM_AT[room_i]
        room = self.rooms[room_i]

        # check that we have occupants
        if not room[-1]:
            return None

        # check if room only has correct occupants
        only_correct = True
        for space in room:
            if space and space != room_pod:
                only_correct = False
                break
        if only_correct:
            return None

        # get the top occupant that can move
        steps = 1
        while not room[steps - 1]:
            steps += 1

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

        # check if room is full
        if room[0]:
            return None

        # check if room contains other pods
        for space in room:
            if space and space != pod:
                return None

        # get steps to bottom-most empty space
        steps = 0
        for space in room:
            if space:
                break
            steps += 1

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
    logging.debug(State.from_string('B..........|AA.BCCDD').moves_from_hall(0))
    logging.debug(State.from_string('AB.........|.A.BCCDD').moves_from_hall(1))
    logging.debug(State.from_string('BA.........|.A.BCCDD').moves_from_hall(1))
    logging.debug(State.from_string('.....D.....|AABBCC.D').moves_from_hall(5))

    # moves from room to hall
    logging.debug(State.from_string('...........|.A.BCCDD').moves_from_room_to_hall(1))
    logging.debug(State.from_string('...........|.B.ACCDD').moves_from_room_to_hall(1))
    logging.debug(State.from_string('...........|.BBACCDD').moves_from_room_to_hall(1))

    # moves from room
    logging.debug(State.from_string('.C.........|BBAACCDD').moves_from_room(1))

    # valid moves
    logging.debug(State.from_string('...........|BACDBCDA').valid_moves())
    logging.debug(State.from_string('...B.......|BACD.CDA').valid_moves())
    logging.debug(State.from_string('...B.C.....|BA.D.CDA').valid_moves())

    # verify hash
    state1 = State.from_string('...........|BBAACCDD')
    state2 = State.from_string('...........|BBAACCDD')
    state_set = {state1, state2}
    assert len(state_set) == 1


def solve(input_state, room_size=2):
    start = State.from_string(input_state, room_size)
    visited = set()

    todo = [(0, start, ())]

    # this is only for the progress bar
    last_cost = 0
    if room_size == 2:
        max_cost = 13495
    else:
        max_cost = 53767

    with alive_bar(max_cost) as bar:
        while todo:
            cost, state, path = heapq.heappop(todo)

            if state in visited:
                logging.debug("already visited", state)
                continue

            # this is only for the progress bar
            bar(cost - last_cost)
            last_cost = cost
            logging.debug("cost", cost, "state", state)

            visited.add(state)

            if state.final():
                logging.debug("final", cost)
                for step in path:
                    logging.debug(step)
                return cost

            for move_cost, move_to_state in state.valid_moves():
                heapq.heappush(todo, (cost + move_cost, move_to_state, tuple(list(path) + [state])))


# RUN TESTS
# tests()

# TEST DATA
# print("Part 1:", solve("...........|BACDBCDA", 2))
# print("Part 2:", solve("...........|BDDACCBDBBACDACA", 4))

# REAL DATA
print("Part 1:", solve("...........|ACDCADBB", 2))
print("Part 2:", solve("...........|ADDCDCBCABADBACB", 4))
