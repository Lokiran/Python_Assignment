get_sla_hours() – Summary

The get_sla_hours(priority) function returns the SLA (Service Level Agreement) target hours based on a given priority value in IBM Maximo.
How It Works

A simple dictionary (sla_mapping) stores the SLA hours for each priority:

1 → 4 hours
2 → 8 hours
3 → 24 hours
4 → 72 hours

The function looks up the priority in the dictionary and returns the matching SLA hours.
If an invalid or unknown priority is passed (e.g., 99), the function safely returns -1.



count_log_levels() – Summary

Function Purpose
The count_log_levels(logs) function analyzes a list of server log entries and counts how many times each log level (INFO, WARN, ERROR) appears.
How It Works

Each log line begins with a log level followed by a colon
Example: "ERROR: disk full"
The function extracts the level using:
line.split(':')[0]

A dictionary named counts keeps track of how many times each level occurs.
For every line, the appropriate counter is increased.
The function finally returns a dictionary with the totals.
