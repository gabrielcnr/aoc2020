def get_seat_id(encoded_seat):
	row, col = decode_seat(encoded_seat)
	return row * 8 + col


def decode_seat(encoded_seat):
	s = encoded_seat.translate(
        {ord("F"): "0", ord("B"): "1", ord("L"): "0", ord("R"): "1"})
	return int(s[:7], 2), int(s[7:], 2)


def part1():
	return max(get_seat_id(encoded_seat)
		for encoded_seat in open("day05_input.txt"))


def test_part1():
	assert (44, 5) == decode_seat("FBFBBFFRLR")
	assert 357 == get_seat_id("FBFBBFFRLR")

	assert (70, 7) == decode_seat("BFFFBBFRRR")
	assert 567 == get_seat_id("BFFFBBFRRR")

	assert (14, 7) == decode_seat("FFFBBBFRRR")
	assert 119 == get_seat_id("FFFBBBFRRR")

	assert (102, 4) == decode_seat("BBFFBBFRLL")
	assert 820 == get_seat_id("BBFFBBFRLL")


if __name__ == "__main__":
	print(f"Max seat ID: {part1()}")
