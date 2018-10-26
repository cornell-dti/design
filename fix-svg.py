import os

# The offending bit of SVG code
# that Sketch doesn't import right.
# In the SVG object with the "Arc" id,
# the last "L" should be an "M"
needle = "L392.829255,118.184594 Z"

replacement = "M"

def fix_svg(file_name):

	# Read file
	with open(file_name, 'r') as txt:
		lines = txt.readlines()
		processed_lines = []
		did_change_file = False

		# If needle (in haystack) exists,
		# replace with `replacement` string.
		for line in lines:
			index = line.find(needle)
			if index > -1:
				line = list(line)
				line[index] = replacement
				line = "".join(line)
				did_change_file = True
			processed_lines.append(line)

	# Write a new file with the same name
	# if anything has changed
	if did_change_file:
		with open(file_name, "w", newline="") as modified_file:
			for line in processed_lines:
				modified_file.write(line)


if __name__ == '__main__':

	# Recurse through directory
	file_queue = ["Branding"]
	while not len(file_queue) == 0:
		directory = file_queue.pop(0)
		for filename in os.listdir(directory):
			filename = directory + "/" + filename

			# Add directory to queue
			if os.path.isdir(filename):
				file_queue.append(filename)

			# Process all SVG Files
			if filename.endswith(".svg"):
				fix_svg(filename)

