

def count_recurrences(word)
	dic = {}
	word.each_char do |ch|
		if dic.has_key? ch
			dic[ch] += 1
		else
			dic[ch] = 1
		end
	end
	has_exactly_two_count = 0
	has_exactly_three_count = 0
	dic.values.each do |rec|
		if rec == 2
			has_exactly_two_count = 1
		elsif rec == 3
			has_exactly_three_count = 1
		end
		if has_exactly_two_count != 0 and has_exactly_three_count != 0
			break
		end
	end
	return [has_exactly_two_count, has_exactly_three_count]
end

number_of_word_exactly_2 = 0
number_of_word_exactly_3 = 0
File.open('in.txt', 'r').each do |line|
	word = line
	counts = count_recurrences(word)
	number_of_word_exactly_2 += counts[0]
	number_of_word_exactly_3 += counts[1]
end

puts number_of_word_exactly_2 * number_of_word_exactly_3