require 'pp'

# read lines
lines = File.open('in.txt', 'r').readlines.map { |e| e.strip.split.map { |f| f.to_i }  }.flatten
#lines = File.open('test.txt', 'r').readlines.map { |e| e.strip.split.map { |f| f.to_i }  }.flatten


def sum_of_metadata_entries(list)
	return rec(list, 0)
end

def rec(list, i)
	result = 0

	num_children = list[i]
	i += 1
	num_metadata = list[i]
	i += 1
	for _ in 0..(num_children-1)
		i, sum = rec(list, i)
		result += sum
	end

	for _ in 0..(num_metadata-1)
		result += list[i]
		i += 1
	end

	return i, result
end


pp sum_of_metadata_entries(lines)
