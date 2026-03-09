from dataclasses import dataclass


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


@dataclass
class GameLayout:
    width: int
    height: int

    road_width: int
    left_border: int
    right_border: int
    lane_x: list[int]

    car_size: tuple[int, int]
    nyan_car_size: tuple[int, int]
    obstacle_size: tuple[int, int]

    score_y: int
    road_segments: list[tuple[int, int, int]]


def build_game_layout(width: int, height: int) -> GameLayout:
    road_width = int(width * 0.78)
    road_width = clamp(road_width, 260, width - 40)

    left_border = (width - road_width) // 2
    right_border = left_border + road_width

    lane_count = 3
    lane_step = road_width // lane_count
    lane_x = []

    car_width = clamp(int(width * 0.18), 60, 110)
    car_height = clamp(int(height * 0.18), 110, 190)

    nyan_width = clamp(int(width * 0.17), 58, 100)
    nyan_height = clamp(int(height * 0.17), 105, 180)

    obstacle_width = clamp(int(width * 0.18), 60, 110)
    obstacle_height = clamp(int(height * 0.10), 45, 90)

    for i in range(lane_count):
        lane_left = left_border + i * lane_step
        x = lane_left + (lane_step - car_width) // 2
        lane_x.append(x)

    segment_width = clamp(int(width * 0.025), 10, 22)
    segment_height = clamp(int(height * 0.18), 90, 170)
    gap = clamp(int(height * 0.08), 35, 80)

    road_segments = []
    divider_positions = [
        left_border + lane_step - segment_width // 2,
        left_border + 2 * lane_step - segment_width // 2,
        ]

    for x in divider_positions:
        y = 0
        while y < height + segment_height:
            road_segments.append((x, y, segment_height))
            y += segment_height + gap

    return GameLayout(
        width=width,
        height=height,
        road_width=road_width,
        left_border=left_border,
        right_border=right_border,
        lane_x=lane_x,
        car_size=(car_width, car_height),
        nyan_car_size=(nyan_width, nyan_height),
        obstacle_size=(obstacle_width, obstacle_height),
        score_y=clamp(int(height * 0.045), 20, 50),
        road_segments=road_segments,
    )