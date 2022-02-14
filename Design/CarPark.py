import heapq

class CarPark:
    def __init__(self, num_spaces) -> None:
        self.spaces = [None for i in range(num_spaces)]
        self.spaces_distance = {0: 17} # Looks like {space_idx: distance to space}
        # This can either be a map or a function but either way, we can assume the distances to each space is know a priori
        self.unnocupied_spaces = [(distance, space_id) for space_id, distance in self.spaces_distance] # looks like [(distance to space, spaceID)]
        self.heapify(self.unnocupied_spaces)
        self.occupied_spaces = []
        self.car_locations = {} # Looks like {car_reg: space_id}

    def park_in_nearest_space(self, car_reg):
        space_id = self.get_nearest_unnocupied_space()
        self.park_car(space_id, car_reg)

    def park_car(self, space_id, car_reg)
        self.car_locations[car_reg] = space_id
        self.occupied_spaces.heappush((self.spaces_distance[space_id], space_id))
        self.spaces[space_id] = car_reg

    def retrieve_car(self, car_reg):
        space_id = self.car_locations.get(car_reg, None)
        if space_id:
            self.unpark_car(space_id, car_reg)

    def upark_car(self, space_id, car_reg):
        del self.car_locations[car_reg]
        self.unnocupied_spaces.heappush((self.spaces_distance[space_id], space_id))
        self.spaces[space_id] = None

    def defrag(self):
        while self.peek_furthest_occupied() != self.peek_nearest_unoccupied() - 1:
            move_from_space = self.get_furthest_occupied_space()
            car_reg = self.spaces[move_from_space]
            self.retrieve_car(car_reg)
            self.park_car(car_reg)

    def peek_nearest_unoccupied(self):
        return self.unnocupied_spaces[0]

    def peek_furthest_occupied(self):
        return self.occupied_spaces[0]

    def get_nearest_unoccupied_space(self):
        _, space_id = self.unnocupied_spaces.heappop()
        return space_id

    def get_furthest_ocupied_space(self):
        _, space_id = self.unnocupied_spaces.heappop()
        return space_id