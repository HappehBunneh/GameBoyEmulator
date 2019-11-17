class Bin:
	def __init__(self, value, bitLength = None):
		self.bitLength = bitLength if bitLength != None else len(value)
		self.value = value if len(value) == self.bitLength else "0"*(self.bitLength-len(value))+value

	def __getitem__(self, key):
		return Bin(self.value[self.bitLength - key - 1])

	def __setitem__(self, key, value):
		self[key] = value
		return self

	def toHex(self):
		string = ""
		for i in range(self.bitLength//4):
			a = 0
			for j in range(4):
				if self.value[(i*4)+j] == "1":
					a += 2**(3-j)
			if a == 10:
				a = "A"
			elif a == 11:
				a = "B"
			elif a == 12:
				a == "C"
			elif a == 13:
				a = "D"
			elif a == 14:
				a = "E"
			elif a == 15:
				a = "F"
			else:
				a = str(a)
			string += a
		return string

	def __lshift__(self, other):
		return Bin(self.value + "0"*other)

	def __rshift__(self, other):
		return Bin("0"*other + self.value)

	def __xor__(self, other):
		if self.bitLength > other.bitLength:
			other = other >> (self.bitLength - other.bitLength)
		elif self.bitLength < other.bitLength:
			self = self >> (other.bitLength - self.bitLength)
		r = ""
		for i in range(self.bitLength):
			if self[i] != other[i]:
				r = "1" + r
			else:
				r = "0" + r
		return Bin(r)

	def __or__(self, other):
		if self.bitLength > other.bitLength:
			other = other >> (self.bitLength - other.bitLength)
		elif self.bitLength < other.bitLength:
			self = self >> (other.bitLength - self.bitLength)
		r = ""
		for i in range(self.bitLength):
			if self[i] == "1":
				r = "1" + r
			elif other.value[i] == "1":
				r = "1 + r"
			else:
				r = "0" + r
		return Bin(r)

	def __and__(self, other):
		if self.bitLength > other.bitLength:
			other = other >> (self.bitLength - other.bitLength)
		elif self.bitLength < other.bitLength:
			self = self >> (other.bitLength - self.bitLength)
		r = ""
		for i in range(self.bitLength):
			if self[i] == other[i] == "1":
				r = "1" + r
			else:
				r = "0" + r
		return Bin(r)

	def __invert__(self):
		r = ""
		for i in self.value:
			if i == "1":
				r = "0" + r
			else:
				r = "1" + r
		return Bin(r)

	def __ne__(self, other):
		if isinstance(other, str):
				if other == self.value:
					return False
		else:
			if other.value == self.value:
				return False
			else:
				return True

	def __eq__(self, other):
		if isinstance(other, str):
			if other == self.value:
				return True
		else:
			if other.value == self.value:
				return True
			else:
				return False

	def __str__(self):
		return self.value

	def __repr__(self):
		return self.value

	def __add__(self, other):
		if self.bitLength > other.bitLength:
			other = other >> (self.bitLength - other.bitLength)
		elif self.bitLength < other.bitLength:
			self = self >> (other.bitLength - self.bitLength)
		r = ""
		carry = 0
		for i in range(self.bitLength):
			if carry:
				if self[i] ^ other[i] == "1":
					r = "0" + r
				else:
					r = "1" + r
					carry = 0
			else:
				if self[i] ^ other[i] == "1":
					r = "1" + r
				else:
					r = "0" + r
			carry += 1 if self[i] & other[i] == "1"  else 0
		return Bin(r)
