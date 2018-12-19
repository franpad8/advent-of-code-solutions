freq_historic = [0]
freq_changes = []
File.open("in.txt", "r").each do |line|
	freq_changes << Integer(line)
end

i = 0
current_freq = 0
while(true)
	pos = i % freq_changes.length
	current_freq += freq_changes[pos]
	puts current_freq
	if freq_historic.include? current_freq
		puts current_freq
		break
	end
	freq_historic << current_freq
	i = i + 1
end
