require 'date'
require 'pp'

$shifts = {}

def main()
	
	lines = File.open("in.txt", "r").readlines().sort()
	guard_counts = {}
	guard = nil
	start = nil
	finish = nil
	lines.each do |line|
		if !line.nil?
			time, event = parse_event(line)
			if event.include? "#"
				guard = event.match(/Guard#(\d+)beginsshift/).captures[0].to_i()
			elsif event.include? "asleep"
				start = time

			elsif event.include? "wakes"
				finish = time
				for i in start..finish-1
					if !guard_counts.key? "#{guard}-#{i}"
						guard_counts["#{guard}-#{i}"] = 0	
					end
					guard_counts["#{guard}-#{i}"] += 1

				end
			end
		end
	end
	pp guard_counts.sort()
	puts calc_max(guard_counts)
	#calculate_guard_max_asleep()
	#calculate_minute_most_asleep()

end

def parse_event(line)
	words = line.split()
	date, time = [words[0][1,words[0].length], words[1][0,5]]
	return [time.split(":")[1].to_i(), words[2..-1].join()]
end

def parse_event_type(str)
	if str.match(/wakes up/)
		return "wakes"
	elsif str.match(/falls asleep/)
		return "asleep"
	else
		Integer(str.match(/Guard #(?<guard_id>\d+) begins shift/)[:guard_id])
	end
end

def calculate_minute_most_asleep()
	minutes = [0]*60
	minutes_counts = {}
	$shifts.each_value do |shift|
		if !minutes_counts.key? shift[:guard_id]
			minutes_counts[shift[:guard_id]] = 0
		end
		events = shift[:events].sort_by! { |a| a[:date].minute }
		i = 0
		while i < events.length
			start = events[i][:date].minute
			finish = events[i+1][:date].minute
			for i in start..finish-1
				minutes[i] += 1
				minutes_counts[shift[:guard_id]] += 1
			end
			i += 2
		end

	end
	puts calc_max(minutes_counts)

end

def calc_max(d)
	max = nil
	d.each_pair do |key, value|
		if max.nil? or value > d[max]
			max = key
		end
	end
	return [max, d[max]]
end	

def calculate_guard_max_asleep()
	
	counts_guards = {}
	$shifts.each_value do |shift|
		guard_id = shift[:guard_id]
		if !counts_guards.key? shift[:guard_id]
			counts_guards[guard_id]= 0
		end
		counts_guards[guard_id] += calculate_sum_asleep_in_shift(shift)
	end
	pp counts_guards
end

def calculate_sum_asleep_in_shift(shift)
	sum = 0
	events = shift[:events]
	events = events.sort_by! { |a| a[:date].minute }
	pp events
	i = 0
	while i < events.length
		sum += events[i+1][:date].minute - events[i][:date].minute
		i += 2
	end
	return sum
end

def add_event(event)

	if event[:event_type].is_a? Integer and event[:date].hour > 0
		event_date = event[:date].to_date + 1
	else
		event_date = event[:date].to_date
	end

	if !$shifts.key?(event_date)
		$shifts[event_date] = {:guard_id => nil, :events => []}
	end
	if event[:event_type].is_a? Integer
		$shifts[event_date][:guard_id] = event[:event_type]
	else
		$shifts[event_date][:events] << event
	end
end

main()

