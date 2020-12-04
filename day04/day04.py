import re


fields = {
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    "cid",  # (Country ID)
}


class Validator:
	"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
	"""

	@classmethod
	def _validate_year(cls, year, ndigits, min_year, max_year):
		try:
			return (len(year) == ndigits) and (min_year <= int(year) <= max_year)
		except Exception:
			return False

	@classmethod
	def validate_byr(cls, year):
		return cls._validate_year(year, 4, 1920, 2002)

	@classmethod
	def validate_iyr(cls, year):
		return cls._validate_year(year, 4, 2010, 2020)

	@classmethod
	def validate_eyr(cls, year):
		return cls._validate_year(year, 4, 2020, 2030)

	@classmethod
	def validate_pid(cls, pid):
		return re.match(r"^\d{9}$", pid) is not None

	@classmethod
	def validate_ecl(cls, ecl):
		return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

	@classmethod
	def validate_hcl(cls, hcl):
		return re.match(r"^#[0-9a-f]{6}$", hcl) is not None

	@classmethod
	def validate_hgt(cls, hgt):
		m = re.match(r"^(\d+)(cm|in)$", hgt)
		if m is not None:
			height = int(m.group(1))
			unit = m.group(2)
			if unit == "cm":
				return 150 <= height <= 193
			else:
				return 59 <= height <= 76
		return False

	@classmethod
	def validate_cid(cls, cid):
		return True


def iter_passports(batch):
	passport = {}
	for line in batch.split("\n"):
		if not line.strip():
			yield passport
			passport = {}
		else:
			passport.update(dict(part.split(":") for part in line.split()))
	if passport:
		yield passport


def is_valid(passport):
	""" validation for part 1 """
	diff = set(passport) ^ fields
	return diff <= {"cid"}


def is_valid_2(passport):
	""" validation for part 2 """
	if not is_valid(passport):
		return False
	for field, value in passport.items():
		validate_func = getattr(Validator, f"validate_{field}")
		if not validate_func(value):
			return False
	return True


def part1(batch):
	return sum(1 for p in iter_passports(batch) if is_valid(p))


def part2(batch):
	return sum(1 for p in iter_passports(batch) if is_valid_2(p))


TEST_PART_1 = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


def test_part1():
	assert [True, False, True, False] == [is_valid(p) for p in iter_passports(TEST_PART_1)]
	assert 2 == part1(TEST_PART_1)


TEST_PART_2_INVALID_PASSPORTS = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""


TEST_PART_2_VALID_PASSPORTS = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


def test_part2_invalid():
	assert not any(is_valid_2(p) for p in iter_passports(TEST_PART_2_INVALID_PASSPORTS))


def test_part2_valid():
	assert all(is_valid_2(p) for p in iter_passports(TEST_PART_2_VALID_PASSPORTS))


def test_validators():
	assert Validator.validate_byr("2002")
	assert not Validator.validate_byr("2003")

	assert Validator.validate_hgt("60in")
	assert Validator.validate_hgt("190cm")
	assert not Validator.validate_hgt("190in")
	assert not Validator.validate_hgt("190")

	assert Validator.validate_hcl("#123abc")
	assert not Validator.validate_hcl("#123abz")
	assert not Validator.validate_hcl("123abc")

	assert Validator.validate_ecl("brn")
	assert not Validator.validate_ecl("wat")

	assert Validator.validate_pid("000000001")
	assert not Validator.validate_pid("0123456789")



if __name__ == "__main__":
	batch = open("day04_input.txt").read()
	print("Part 1 - total valid passports:", part1(batch))
	print("Part 2 - total valid passports:", part2(batch))
