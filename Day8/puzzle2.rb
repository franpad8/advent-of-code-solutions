require 'pp'

# read lines
lines = File.open('in.txt', 'r').readlines[0].strip.split.map { |f| f.to_i }
#lines = File.open('test.txt', 'r').readlines[0].strip.split.map { |f| f.to_i }

def sum_of_metadata_entries(list)
	return rec(list, 0)
end

def rec(list, i)
	result = 0

	num_children = list[i]
	i += 1
	num_metadata = list[i]
	i += 1

	if num_children == 0
		for _ in 0..(num_metadata-1)
			result += list[i]
			i += 1
			
		end
		return i, result
	end
	
	children_values = []
	puts num_children
	for _ in 0..(num_children-1)
		i, sum = rec(list, i)
		children_values << sum
	end

	for _ in 0..(num_metadata-1)
		children_pos = list[i]-1
		if !children_values[children_pos].nil?
			result += children_values[children_pos]
		end
		i += 1
	end
	
	return i, result
end


pp sum_of_metadata_entries(lines)
