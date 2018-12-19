require 'pp'

graph = {}

# Read file and store input data
#lines = File.open('test.txt', 'r').readlines.map do |line| 
lines = File.open('in.txt', 'r').readlines.map do |line| 
	striped = line.strip
	splited = striped.split
	[splited[1], splited[7]]
end

# Build precedence graph
lines.each do |pre|
	requisite, task = [pre[0], pre[1]]
	if !graph.key? requisite
		graph[requisite] = []
	end
	graph[requisite] << task
end

def is_available(elem, graph)
	return !graph.values.flatten.include?(elem)
end

# Find final task
initial_tasks = (graph.keys - graph.values.flatten)
puts initial_tasks



# Find path
visited = []
stack = []
stack = initial_tasks
while !stack.empty?
	stack = stack.sort.reverse
	current = stack.pop()
	if !visited.include?(current)
			#print current
			puts "#{graph[current]}"
			if !graph[current].nil?
				aux = graph[current].dup()
				graph[current] = []
				aux.each do |e|
					if is_available(e, graph)
						stack << e
					end
				end
				
			end
			visited << current	
	end
end

pp visited.join



# pp lines

