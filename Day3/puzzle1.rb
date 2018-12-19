require 'matrix'

fabric = []
for _ in 1..1500
	fabric << [nil]*1500
end

counts = 0
File.open('in.txt', 'r').each do |line|
	m = line.match(/#(?<id>\d+) @ (?<left>\d+),(?<top>\d+): (?<width>\d+)x(?<height>\d+)/)
	id = Integer(m[:id])
	top = Integer(m[:top])
	width = Integer(m[:width])
	left = Integer(m[:left])
	height = Integer(m[:height]) 
	#puts id,top,width,left,height
	start_y = top
	finish_y = top + height - 1
	start_x = left
	finish_x = left + width - 1
	for i in start_y..finish_y
		for j in start_x..finish_x
			if fabric[i][j] == nil
				fabric[i][j] = id
			elsif fabric[i][j] != 'X'
				fabric[i][j] = 'X'
				counts += 1
			end
		end
	end
end

puts counts