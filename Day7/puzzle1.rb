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

def get_task_total_time(task)
	return task.ord()- 4
end

def add_task(task, current_second, workers)
	if workers.length >= 5
		return false
	end
	workers[task] = current_second + get_task_total_time(task)
	return true
end

def working_on(task, workers)
	return workers.key? task
end

def update(graph, seconds, workers, completed, stack)
	workers = workers.select do |k, v|
		if seconds < v
			true
		else
			completed << k
			if !graph[k].nil?
				aux = graph[k].dup()
				graph[k] = []
				aux.each do |e|
					if !completed.include?(e) and is_available(e, graph) and !working_on(e, workers)
						stack << e
					end
				end
			end
			false
		end
	end
	return workers
end

# Find final task
initial_tasks = (graph.keys - graph.values.flatten)

# Find path
completed = []
stack = []
stack = initial_tasks
seconds = 0
workers = {}
begin
	workers = update(graph, seconds, workers, completed, stack)

	stack = stack.sort
	i = 0
	while i < stack.length
		current = stack[i]
		if !current.nil? and !completed.include?(current) and is_available(current, graph) and !working_on(current, workers)
				if add_task(current, seconds, workers)
					stack.delete_at(i)
				else
					i+=1
				end
		end
		
	end
	puts "second: #{seconds} => #{workers}"
	
	seconds += 1
end while !workers.empty?

pp completed.join
pp seconds