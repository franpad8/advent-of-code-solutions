require 'pp'



def main()
	#lines = File.open("in.txt", "r").readlines()
	lines = File.open("in.txt", "r").readlines()

	coordinates = lines.map { |l| [l.split(',')[0].to_i, l.split(',')[1].to_i] }
	# 338 max X
	# 353 max Y
	grid_length = find_maximum_of_each_coordinates(coordinates) + 1
	grid = []
	for _ in 0..grid_length-1
		grid << [-1]*(grid_length)
	end

	puts calculate_safe_region_length(grid, coordinates)

	# initialize grid with given coordinates
	#i = 0
	#coordinates.each do |coord|
	#	grid[coord[1]][coord[0]] = i
	#	i += 1
	#end

	#nearest_distances = calculate_min_distances(grid, coordinates)
	#calculate_finite_coords(grid, nearest_distances)
	#puts max_value_from_hash(nearest_distances)
end

def max_value_from_hash(h)
	max_k = nil
	max_v = nil
	h.each_pair do |k, v|
		if max_k.nil? or v > max_v
			max_k = k
			max_v = v
		end
	end
	return max_v
end

def calculate_safe_region_length(grid, coordinates)
	length = 0
	for j in 0..grid.length-1
		for k in 0..grid[j].length-1
			if safe?([k, j], coordinates)
				length += 1
			end
		end
	end
	return length
end

def safe?(location, coordinates)
	sum = 0
	coordinates.each do |coord|
		sum += distance(location, coord)
		if sum >= 10000
			return false
		end
	end
	return true
end

def calculate_finite_coords(grid, finites_coords)
	grid[0].each do |elem|
		if finites_coords.key? elem
			finites_coords.delete(elem)
		end
	end
	grid[-1].each do |elem|
		if finites_coords.key? elem
			finites_coords.delete(elem)
		end
	end
	grid.each do |row|
		if finites_coords.key? row[0]
			finites_coords.delete(row[0])
		end
		if finites_coords.key? row[-1]
			finites_coords.delete(row[-1])
		end
	end
end



def calculate_min_distances(grid, coordinates)
	num_nearest = {}
	for j in 0..grid.length-1
		for k in 0..grid[j].length-1
			nearest = nearest_coordinate([k, j], coordinates)
			grid[j][k] = nearest
			if nearest != "." 
				if !num_nearest.key? nearest
					num_nearest[nearest] = 1
				else
					num_nearest[nearest] += 1
				end
			end
		end
	end
	return num_nearest
end

def nearest_coordinate(location, coordinates)
	min_distance = nil
	min_i = nil
	i = 0
	coordinates.each do |coord|
		distance = distance(location, coord)
		if distance == 0
			return i
		elsif min_i.nil? or distance < min_distance
			min_i = i
			min_distance = distance
		elsif distance == min_distance
			min_i = "."
			min_distance = distance

		end
		i += 1
	end
	return min_i
end

def distance(coord1, coord2)
	return (coord1[1] - coord2[1]).abs + (coord1[0] - coord2[0]).abs
end

def print_grid(grid)
	grid.each do |row|
		row.each do |elem|
			print "#{elem} "
		end
		puts
	end
end


def find_maximum_of_each_coordinates(coordinates)
	max = nil
	coordinates.each do |coord|
		if max.nil? or coord[0] > max
			max = coord[0]
		end

		if max.nil? or coord[1] > max
			max = coord[1]
		end
	end
	return max
end

main()

