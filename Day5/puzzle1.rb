def react?(ch1, ch2)
	if ch1 == ch1.upcase and ch2 == ch2.downcase()
		if ch1.downcase() == ch2.downcase()
			return true
		end
	elsif ch2 == ch2.upcase and ch1 == ch1.downcase()
		if ch1.downcase() == ch2.downcase()
			return true
		end
	end

	return false
end


input = File.open("in.txt", "r").readline().strip()
#input = "dabAcCaCBAcCcaDA".split("")


def react_polymers(input)
	buf = []
	input.each_char do |c|
	    if !buf.empty? and react?(c, buf[-1])
	        buf.pop()
	    else
	        buf << c
	    end
	end
	return buf.length
end

def find_shortest_polymer_after_remove(input)
	min = input.length
	for upper in "A".."Z"
		lower = upper.downcase
		reduction = react_polymers(input.delete(lower).delete(upper))
		if reduction < min
			min = reduction
		end
	end

	puts min
end

find_shortest_polymer_after_remove(input)