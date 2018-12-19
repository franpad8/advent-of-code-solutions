current_freq = 0

File.open("in.txt", "r").each do |line|
	freq_change = Integer(line)
	current_freq += freq_change
end

puts current_freq
