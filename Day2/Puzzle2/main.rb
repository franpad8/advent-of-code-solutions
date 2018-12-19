
def are_close(word1, word2)
	differents_chars_count = 0
	for i in 0..word1.length
		if word1[i] != word2[i]
			if differents_chars_count == 1
				return false
			end
			differents_chars_count = 1
		end
	end
	return true
end

words = []
File.open('in.txt', 'r').each do |line|
	words << line
end

for i in 0..words.length-1
	for j in i+1..words.length-1
		if are_close(words[i], words[j])
			puts words[i]
			puts words[j]
			exit
		end
	end
end

